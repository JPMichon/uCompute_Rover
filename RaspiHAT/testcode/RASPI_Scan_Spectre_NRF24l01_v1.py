#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from pyrf24 import RF24, RF24_PA_LOW, rf24_crclength_e

# --- Configuration des broches (GPIO BCM natifs de votre HAT) ---
_NRF_24L01_CE  = 22
_NRF_24L01_CSN = 0   # SPI0 CE0 (GPIO 8)

def init_scanner():
    """Initialise le module nRF24L01 sur le Pi en mode écoute brute"""
    print("Initialisation du module nRF24L01 via pyrf24...")
    
    # Création de l'instance radio
    nrf = RF24(_NRF_24L01_CE, _NRF_24L01_CSN)
    
    if not nrf.begin():
        raise RuntimeError("Le matériel nRF24L01 ne répond pas. Vérifiez le câblage.")
    
    # Configuration minimale pour le scan
    nrf.payload_size = 32
    nrf.dynamic_payloads = False
    
    # Désactive l'ACK automatique
    nrf.set_auto_ack(False)            
    
    # --- Disable CRC ---
    nrf.crc_length = rf24_crclength_e.RF24_CRC_DISABLED
    
    # Ouverture d'un canal fictif obligatoire pour passer en mode écoute
    nrf.open_rx_pipe(1, b"\x00\x00\x00\x00\x00")
    return nrf

def scan_spectrum(nrf, nb_echantillons=40):
    """Balaye les canaux 1 à 100 et mesure le taux d'occupation via le RPD"""
    resultats = {}
    canaux_a_tester = range(1, 101)

    for channel in canaux_a_tester:
        nrf.channel = channel
        hits = 0
        
        for _ in range(nb_echantillons):
            nrf.start_listening()
            time.sleep(0.00013) # Pause de 130µs pour laisser la radio se caler sur la fréquence
            
            # Lecture native du registre RPD (Received Power Detector)
            # pyrf24 possède un attribut booléen .rpd qui renvoie True si un signal > -64dBm est capté
            if nrf.rpd:
                hits += 1
                
            nrf.stop_listening()
        
        # Calcul du pourcentage d'occupation
        pourcentage = int((hits / nb_echantillons) * 100)
        resultats[channel] = pourcentage

    return resultats

def afficher_graphique(spectre):
    """Affiche l'intégralité des canaux dans la console Linux sans aucun filtre"""
    # Efface l'écran de la console pour créer un effet d'animation fluide
    print("\033[H\033[J", end="") 
    
    print("=============================================")
    print("   RASPBERRY PI 3B : ANALYSEUR DE SPECTRE    ")
    print("=============================================")
    
    for channel, occupation in spectre.items():
        barre = "#" * (occupation // 4)
        print("CH {:03d} [{:3d}%] | {}".format(channel, occupation, barre))

# --- Boucle Principale ---
try:
    nrf_module = init_scanner()
    print("Scanner prêt ! Lancement de l'analyse...")
    time.sleep(1)
    
    while True:
        # Exécute un balayage complet des fréquences
        donnees_spectre = scan_spectrum(nrf_module, nb_echantillons=40)
        
        # Affiche le rendu graphique dans la console
        afficher_graphique(donnees_spectre)
        
        # Courte pause avant le prochain balayage
        time.sleep(0.1)  # Réduit à 0.1s pour un rafraîchissement beaucoup plus dynamique sous Linux

except KeyboardInterrupt:
    print("\nScanner arrêté proprement par l'utilisateur.")
except Exception as e:
    print(f"\nErreur d'exécution : {e}")