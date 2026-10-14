import time
import random
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas

# 1. Initialisation directe du périphérique SSD1306 (Adresse 0x3C, Bus I2C 1)
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, width=128, height=64)

# 2. Paramètres de l'animation
FONT_WIDTH = 8
FONT_HEIGHT = 8
COLS = device.width // FONT_WIDTH

CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ*#$@%&+-=<>:?"

y_positions = [random.randint(-FONT_HEIGHT * 4, 0) for _ in range(COLS)]
speeds = [random.randint(2, 5) for _ in range(COLS)]

print("Animation Matrix (Luma Direct) lancée... Ctrl+C pour quitter.")

try:
    while True:
        # L'instruction 'canvas' de Luma verrouille l'accès direct au buffer de l'écran
        with canvas(device) as draw:
            for col in range(COLS):
                x_pos = col * FONT_WIDTH
                y_pos = y_positions[col]
                
                if y_pos >= 0:
                    # 1. Caractère du haut
                    if y_pos - (FONT_HEIGHT * 2) < device.height:
                        draw.text((x_pos, y_pos - (FONT_HEIGHT * 2)), random.choice(CHARS), fill="white")
                        
                    # 2. Caractère du milieu
                    if y_pos - FONT_HEIGHT < device.height:
                        draw.text((x_pos, y_pos - FONT_HEIGHT), random.choice(CHARS), fill="white")
                        
                    # 3. Tête de la goutte
                    if y_pos < device.height:
                        draw.text((x_pos, y_pos), random.choice(CHARS), fill="white")
                
                # Descente
                y_positions[col] += speeds[col]
                
                # Réinitialisation en haut
                if y_positions[col] >= device.height + (FONT_HEIGHT * 2):
                    y_positions[col] = random.randint(-FONT_HEIGHT * 4, 0)
                    speeds[col] = random.randint(2, 5)
                    
        # Pause très courte (Luma gère le rafraîchissement de manière beaucoup plus fluide)
        time.sleep(0.01)

except KeyboardInterrupt:
    device.clear()
    print("\nAnimation arrêtée.")
