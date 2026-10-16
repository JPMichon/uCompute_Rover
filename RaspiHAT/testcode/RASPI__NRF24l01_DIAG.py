#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import board
import busio
import digitalio
from circuitpython_nrf24l01.rf24 import RF24

# Configuration de vos broches réelles
_NRF_24L01_CSN = board.D8
_NRF_24L01_CE  = board.D22

print("=== DIAGNOSTIC DES REGISTRES VIA LA BIBLIOTHÈQUE ===")

try:
    # 1. Initialisation SPI et création de l'objet
    spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
    ce_pin = digitalio.DigitalInOut(_NRF_24L01_CE)
    csn_pin = digitalio.DigitalInOut(_NRF_24L01_CSN)
    
    nrf = RF24(spi, csn_pin, ce_pin)
    
    # 2. Application de configurations de base pour tester l'écriture dans les registres
    nrf.channel = 1
    nrf.payload_size = 20
    nrf.open_tx_pipe(b"\xd2\xf0\xf0\xf0\xf0")
    nrf.open_rx_pipe(1, b"\xe1\xf0\xf0\xf0\xf0")

    # --- AJOUT INDISPENSABLE POUR PASSER EN RÉCEPTION ---
    nrf.listen = True 

    # 3. Appel de la fonction de diagnostic officielle
    # Elle va lire TOUS les registres de la puce et les formater proprement à l'écran
    print("\n--- État actuel de la puce nRF24L01 : ---\n")
    nrf.print_details()

except Exception as e:
    print(f"\n❌ Erreur lors de l'accès au module : {e}")

