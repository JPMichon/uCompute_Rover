import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# 1. Dimensions de l'écran OLED du module RetroPico
WIDTH = 128
HEIGHT = 64

# 2. Initialisation du bus I2C et de l'écran
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)

# 3. Effacer l'écran au démarrage
oled.fill(0)
oled.show()

# 4. Création d'une image vierge en noir et blanc (mode '1') pour dessiner
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# 5. Chargement de la police de caractères par défaut
font = ImageFont.load_default()

# 6. Dessiner le texte sur l'image virtuelle
# Syntaxe : draw.text((coordonnée_X, coordonnée_Y), "Votre texte", font=font, fill=255)
draw.text((0, 0), "RoverBot OS", font=font, fill=255)
draw.text((0, 20), "Hello World !", font=font, fill=255)
draw.text((0, 45), "I2C en ligne...", font=font, fill=255)

# 7. Envoyer l'image finale sur l'écran OLED physique
oled.image(image)
oled.show()

print("Affichage 'Hello World' réussi sur l'écran OLED !")
