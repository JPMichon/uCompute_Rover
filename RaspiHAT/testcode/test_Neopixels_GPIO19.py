import time
import board
import neopixel

# Configuration du bandeau
PIXEL_PIN = board.D19   # Connecté sur le GPIO 19
NUM_PIXELS = 8          # Vos 8 NeoPixels
BRIGHTNESS = 0.2        # Luminosité à 20% pour ne pas éblouir

# Initialisation
pixels = neopixel.NeoPixel(
    PIXEL_PIN, 
    NUM_PIXELS, 
    brightness=BRIGHTNESS, 
    auto_write=True
)

print("Début du test NeoPixel sur le GPIO 19... Appuyez sur Ctrl+C pour quitter.")

try:
    while True:
        # Étape 1 : Tout en Rouge
        pixels.fill((255, 0, 0))
        time.sleep(1)

        # Étape 2 : Tout en Vert
        pixels.fill((0, 255, 0))
        time.sleep(1)

        # Étape 3 : Tout en Bleu
        pixels.fill((0, 0, 255))
        time.sleep(1)

        # Étape 4 : Chenillard jaune LED par LED
        pixels.fill((0, 0, 0))
        for i in range(NUM_PIXELS):
            pixels[i] = (255, 255, 0)
            time.sleep(0.15)
            pixels[i] = (0, 0, 0)

except KeyboardInterrupt:
    # Éteint proprement toutes les LED en quittant
    pixels.fill((0, 0, 0))
    print("\nTest arrêté, LED éteintes.")
