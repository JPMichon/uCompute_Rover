#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Optimized for Raspberry Pi 3B (Python 3) using pyrf24 & luma.oled

import time
import struct
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import ImageFont

# Importation native de pyrf24 (Gestion GPIO/SPI sans dépendance board)
from pyrf24 import RF24, RF24_PA_MAX, rf24_datarate_e, rf24_crclength_e
import RPi.GPIO as GPIO

# --- Configuration des broches GPIO (Raspberry Pi 3B / Numérotation BCM) ---
_NRF_24L01_CE  = 22  # GPIO22
_NRF_24L01_CSN = 0   # SPI0 CE0 (GPIO8)
_Led_System    = 25  # GPIO25

# --- Paramètres de communication du module NRF24L01 ---
payload_size = 20
_NRF24l01_Channel = 1

# Configuration du rôle
role = "receive"  

if role == "send":
    send_pipe = b"\xe1\xf0\xf0\xf0\xf0"
    receive_pipe = b"\xd2\xf0\xf0\xf0\xf0"
else:
    send_pipe = b"\xd2\xf0\xf0\xf0\xf0"
    receive_pipe = b"\xe1\xf0\xf0\xf0\xf0"

# --- Initialisation de la LED Système (Via RPi.GPIO natif) ---
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(_Led_System, GPIO.OUT)

def flash_led(times=1):
    for _ in range(times):
        GPIO.output(_Led_System, GPIO.HIGH)
        time.sleep(0.01)
        GPIO.output(_Led_System, GPIO.LOW)
        time.sleep(0.01)

# --- Initialisation de l'OLED SSD1306 avec Luma ---
# Luma s'interface directement avec le bus I2C matériel /dev/i2c-1 du Pi
serial_i2c = i2c(port=1, address=0x3C)
oled = ssd1306(serial_i2c, width=128, height=64)

# Police par défaut
font = ImageFont.load_default()

# --- Émulation du Terminal TTY ---
WrapScreen = int(oled.height / 10)
TTY_Pointer = 0
TTY = [''] * WrapScreen

def PrintTTY(texte):
    global TTY_Pointer
    texte_propre = texte[:15]
    
    if TTY_Pointer < WrapScreen:
        TTY[TTY_Pointer] = texte_propre
        TTY_Pointer += 1
    else:
        for i in range(WrapScreen - 1):
            TTY[i] = TTY[i + 1]
        TTY[TTY_Pointer - 1] = texte_propre

    # Rendu ultra-rapide propre à Luma à l'aide d'un gestionnaire de contexte (canvas)
    with canvas(oled) as draw:
        for i in range(TTY_Pointer):
            line_ptr = i * 10
            draw.text((0, line_ptr), TTY[i], font=font, fill=255)

def SplashScreen():
    with canvas(oled) as draw:
        draw.text((0, 0),  '----------------', font=font, fill=255)
        draw.text((10, 10), 'NRF24L01', font=font, fill=255)
        draw.text((50, 20), 'RECEIVER (LUMA)', font=font, fill=255)
        draw.text((0, 30),  '----------------', font=font, fill=255)

# --- Démarrage de l'interface ---
flash_led(1)
SplashScreen()
time.sleep(1)

try:
    # Initialisation de la Radio (Le bus SPI matériel est géré de façon transparente)
    nrf = RF24(_NRF_24L01_CE, _NRF_24L01_CSN)
    
    if not nrf.begin():
        raise RuntimeError("Le matériel nRF24L01 ne répond pas. Vérifiez le câblage.")
    
    # --- Alignement strict des registres avec le protocole du RP2040 ---
    nrf.payload_size = payload_size            
    nrf.channel = _NRF24l01_Channel            
    
    nrf.data_rate = rf24_datarate_e.RF24_1MBPS 
    nrf.pa_level = RF24_PA_MAX                 
    nrf.crc_length = rf24_crclength_e.RF24_CRC_16  
    
    nrf.set_retries(6, 8)                      
    nrf.set_auto_ack(True)                     
    nrf.dynamic_payloads = False                

    # Gestion des pipes de communication
    nrf.stop_listening(send_pipe)              
    nrf.open_rx_pipe(1, receive_pipe)          

except Exception as e:
    print("NRF24l01 not found:", e)
    with canvas(oled) as draw:
        draw.text((0, 0), 'err Comm. Module', font=font, fill=255)
        draw.text((0, 10), '-----------------', font=font, fill=255)
        draw.text((25, 30), "nRF24L0+", font=font, fill=255)
        draw.text((20, 40), "not found", font=font, fill=255)
    while True:
        time.sleep(0.1)

# Effacement de l'écran (Un canvas vide avec luma efface automatiquement)
with canvas(oled) as draw:
    pass

# Passage en mode écoute
nrf.start_listening()
PrintTTY("Waiting")
PrintTTY("------------")

# --- Boucle principale de réception ---
try:
    while True:
        if nrf.available():
            while nrf.available():
                package = nrf.read(nrf.payload_size)
                
                if package:
                    try:
                        msg = package.decode('utf-8', errors='ignore').replace('\x00', '')
                        clean_msg = msg.strip(" \n\r\t")
                        
                        if len(clean_msg) > 0:
                            print("Message Reçu :", clean_msg)
                            PrintTTY("MSG:" + clean_msg)
                            flash_led(1)
                    except Exception as decoding_error:
                        print("Erreur de décodage du paquet :", decoding_error)
                
        time.sleep(0.005)

except KeyboardInterrupt:
    print("\nArrêt du script.")
    with canvas(oled) as draw:
        pass  # Efface l'écran à la fermeture
    GPIO.cleanup()