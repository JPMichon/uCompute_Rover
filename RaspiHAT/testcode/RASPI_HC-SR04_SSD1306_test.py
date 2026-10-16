#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# uCompute_Rover - HC-SR04 & SSD1306 Test Script (luma.oled)

import time
import RPi.GPIO as GPIO
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import ImageFont

# --- Configuration des Broches (Mapping de vos corrections) ---
GPIO_TRIG = 23  # Broche Physique 16
GPIO_ECHO = 24  # Broche Physique 18

# --- Initialisation de l'OLED SSD1306 via Luma ---
try:
    serial_i2c = i2c(port=1, address=0x3C)
    oled = ssd1306(serial_i2c, width=128, height=64)
    font_large = ImageFont.load_default() # Vous pouvez utiliser une police TTF pour agrandir
    print("Écran OLED initialisé avec succès.")
except Exception as e:
    print(f"Erreur d'initialisation de l'OLED : {e}")
    oled = None

# --- Initialisation du Télémètre HC-SR04 ---
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(GPIO_TRIG, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# Forcer le Trigger à l'état BAS au démarrage pour stabiliser le capteur
GPIO.output(GPIO_TRIG, GPIO.LOW)
time.sleep(0.5)

def mesurer_distance():
    """ Envoie une impulsion ultrason et calcule la distance en cm """
    # 1. Déclenchement : impulsion de 10 microsecondes à l'état HAUT
    GPIO.output(GPIO_TRIG, GPIO.HIGH)
    time.sleep(0x00000A / 1000000.0) # 10 µs
    GPIO.output(GPIO_TRIG, GPIO.LOW)

    debut_impulsion = time.time()
    fin_impulsion = time.time()

    # 2. Capture du temps de début (quand l'ECHO passe à 1)
    # On ajoute une sécurité temporelle (timeout) pour éviter le blocage du script
    timeout = time.time() + 0.1
    while GPIO.input(GPIO_ECHO) == 0:
        debut_impulsion = time.time()
        if debut_impulsion > timeout:
            return -1

    # 3. Capture du temps de fin (quand l'ECHO repasse à 0)
    timeout = time.time() + 0.1
    while GPIO.input(GPIO_ECHO) == 1:
        fin_impulsion = time.time()
        if fin_impulsion > timeout:
            return -1

    # 4. Calcul de la distance
    # Durée de l'aller-retour en secondes
    duree_signal = fin_impulsion - debut_impulsion
    
    # Distance = (Vitesse du son (34300 cm/s) * Temps) / 2
    distance = (duree_signal * 34300) / 2
    
    return round(distance, 1)

# --- Boucle Principale de Test ---
print("Test du HC-SR04 démarré. Appuyez sur Ctrl+C pour quitter.")

try:
    while True:
        dist = mesurer_distance()
        
        # Formatage de l'affichage console
        if dist == -1:
            texte_console = "Erreur de lecture"
            texte_oled = "Erreur Capteur"
        else:
            texte_console = f"Distance : {dist} cm"
            texte_oled = f"Dist: {dist} cm"
            
        print(texte_console)

        # Mise à jour graphique sur le SSD1306 via Luma
        if oled:
            with canvas(oled) as draw:
                # Dessin d'un cadre décoratif
                draw.rectangle((0, 0, oled.width - 1, oled.height - 1), outline=255, fill=0)
                
                # Entête du widget
                draw.text((10, 8), "uCompute Rover", font=font_large, fill=255)
                draw.text((10, 20), "----------------", font=font_large, fill=255)
                
                # Affichage de la mesure au centre
                draw.text((20, 38), texte_oled, font=font_large, fill=255)
                
        # Pause de 200ms entre deux mesures pour éviter l'écho résiduel dans la pièce
        time.sleep(0.2)

except KeyboardInterrupt:
    print("\nTest arrêté par l'utilisateur.")
    if oled:
        with canvas(oled) as draw:
            pass # Efface l'écran proprement à la fermeture
    GPIO.cleanup()
