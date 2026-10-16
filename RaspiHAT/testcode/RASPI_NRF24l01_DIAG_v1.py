#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
# board et busio ne sont plus nécessaires pour le SPI avec pyrf24
from pyrf24 import RF24, RF24_PA_LOW

# Configuration de vos broches CE et CSN (Numéros GPIO Broadcom)
# Sur le Pi 3B, board.D22 correspond au GPIO 22 et board.D8 au GPIO 8 (CE0)
_NRF_24L01_CE  = 22
_NRF_24L01_CSN = 0  # 0 correspond au canal SPI0 CE0 (broche physique 24 / GPIO 8)

print("=== DIAGNOSTIC DES REGISTRES VIA LA BIBLIOTHÈQUE PYRF24 ===")

try:
    # 1. Création de l'objet et initialisation automatique du SPI
    # pyrf24 prend (broche_ce, broche_csn). Pour le CSN, 0 utilise le SPI matériel CE0.
    nrf = RF24(_NRF_24L01_CE, _NRF_24L01_CSN)
    
    if not nrf.begin():
        raise RuntimeError("Le matériel nRF24L01 ne répond pas. Vérifiez le câblage.")
    
    # 2. Application de configurations de base (équivalentes à votre code CircuitPython)
    nrf.channel = 1                        # nrf.channel = 1
    nrf.payload_size = 20                  # nrf.payload_size = 20

    # Configuration de la puissance
    # ---------------------------------------
    # RF24_PA_MIN : Puissance minimale
    # RF24_PA_LOW : Puissance basse
    # RF24_PA_HIGH : Puissance élevée.
    # RF24_PA_MAX : Puissance maximale
    # ---------------------------------------
    nrf.pa_level = nrf.pa_level = RF24_PA_LOW  # Aligne la puissance sur une valeur basse 
    # ---------------------------------------

    nrf.stop_listening(b"\xd2\xf0\xf0\xf0\xf0") 
    nrf.open_rx_pipe(1, b"\xe1\xf0\xf0\xf0\xf0")

    # --- AJOUT INDISPENSABLE POUR PASSER EN RÉCEPTION ---
    nrf.start_listening()                  # nrf.listen = True

    # 3. Appel de la fonction de diagnostic officielle
    print("\n--- État actuel de la puce nRF24L01 : ---\n")
    nrf.print_details()

except Exception as e:
    print(f"\n❌ Erreur lors de l'accès au module : {e}")

