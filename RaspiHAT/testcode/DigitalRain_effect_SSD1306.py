import time
import random
import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# 1. Configuration de l'écran SSD1306 (I2C)
WIDTH = 128
HEIGHT = 64

# Initialisation du bus I2C matériel du Raspberry Pi 3B et de l'écran (Adresse 0x3C)
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)

# Effacer l'écran au démarrage
oled.fill(0)
oled.show()

# 2. Paramètres de l'animation Matrix
FONT_WIDTH = 8    # Largeur estimée d'un caractère de la police par défaut
FONT_HEIGHT = 8   # Hauteur estimée d'un caractère de la police par défaut
COLS = WIDTH // FONT_WIDTH  # Nombre de colonnes de texte possibles (16 colonnes)

# Liste des caractères à afficher
CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ*#$@%&+-=<>:?"

# Initialisation des pistes de gouttes
y_positions = [random.randint(-FONT_HEIGHT * 4, 0) for _ in range(COLS)]
# Note : Les pas de déplacement en pixels sont réduits (1 à 3) pour garder une vitesse fluide
speeds = [random.randint(1, 3) for _ in range(COLS)]

# Chargement de la police de caractères par défaut de Pillow
font = ImageFont.load_default()

print("Animation Matrix lancée sur l'OLED... Appuyez sur Ctrl+C pour quitter.")

try:
    # Boucle principale d'animation
    while True:
        # Création d'une image vierge en noir et blanc (mode '1') à chaque frame
        image = Image.new("1", (oled.width, oled.height))
        draw = ImageDraw.Draw(image)
        
        for col in range(COLS):
            # Position X en pixels pour la colonne actuelle
            x_pos = col * FONT_WIDTH
            y_pos = y_positions[col]
            
            # On affiche une traînée verticale de 3 caractères pour simuler l'effet Matrix
            if y_pos >= 0:
                # 1. Le caractère du haut (le plus ancien)
                if y_pos - (FONT_HEIGHT * 2) < HEIGHT:
                    char_top = random.choice(CHARS)
                    draw.text((x_pos, y_pos - (FONT_HEIGHT * 2)), char_top, font=font, fill=255)
                    
                # 2. Le caractère du milieu
                if y_pos - FONT_HEIGHT < HEIGHT:
                    char_mid = random.choice(CHARS)
                    draw.text((x_pos, y_pos - FONT_HEIGHT), char_mid, font=font, fill=255)
                    
                # 3. La tête de la goutte (le caractère le plus récent en bas)
                if y_pos < HEIGHT:
                    char_lead = random.choice(CHARS)
                    draw.text((x_pos, y_pos), char_lead, font=font, fill=255)
            
            # Fait descendre la goutte selon sa vitesse propre
            y_positions[col] += speeds[col]
            
            # Si la goutte a complètement quitté l'écran, on la réinitialise en haut
            if y_positions[col] >= HEIGHT + (FONT_HEIGHT * 2):
                y_positions[col] = random.randint(-FONT_HEIGHT * 4, 0)
                speeds[col] = random.randint(1, 3)
                
        # Envoyer l'image construite en mémoire tampon à l'écran OLED physique
        oled.image(image)
        oled.show()
        
        # Petite pause pour contrôler la fluidité globale
        time.sleep(0.01)

except KeyboardInterrupt:
    # Nettoyage propre de l'écran en quittant avec Ctrl+C
    oled.fill(0)
    oled.show()
    print("\nAnimation arrêtée, écran effacé.")
