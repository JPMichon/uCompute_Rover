from nrf24l01 import NRF24L01
from machine import SPI, Pin, I2C
from time import sleep
from ssd1306 import SSD1306_I2C
import struct
import utime
import os


#Configuration des Ports pour le uCompute V1.x
_MicroSD_Detect = 7 # détection de la présence d'une carte MicroSD (GP7)
_MicroSD_Select = 13 # définition de la pin Select du SDCARD (GP13)
_SPI1_SCK = 14 # SPI1_shared Clock
_SPI1_MOSI = 15 # SPI1_shared MOSI
_SPI1_MISO = 12 # SPI1_shared MISO
_ST7789_SCK = 2 # définition de la pin Clock du ST7789 (GP2) SPI0
_ST7789_MOSI = 3 # définition de la pin MOSI du ST7789 (GP3) SPI0
_ST7789_RESET = 4 # définition de la pin Reset du ST7789 (GP4)
_ST7789_DC = 5 # définition de la pinSelect du ST7789 (GP5)
_ST7789_BL = 6 # définition de la pinBacklit du ST7789 (GP6)
_Led_System = 25 # définition du port  del systeme (GP25)
_I2C_SDA = 20 # définition de Data du I2C(0) (GP20)
_I2C_SCL = 21 # définition de SCL du I2C(0) (GP21)
_Buzzer = 11 # définition du  buzzer (GP11)
_NeoPixel = 23 # définition du port NeoPixel (GP23)
_NeoPixel_nbr = 1 # nombre de neopixel sur le port
_Boutons = 26 # définition du port analogue des boutons (GP26)
# Configuration du port serie sur le connecteur
_UART = 0 # UART par defaut
_TX_PIN = 0 # TX Pin (GP0)
_RX_PIN = 1 # TX Pin (GP1)
_BaudRate = 9600 # Baud rate du UART


# Configuration Remote Module
_analog_X = machine.ADC(27)
_analog_Y = machine.ADC(28)
_Led_Obstacle = 17
_Led_Warning = 16 
_Led_Lost_comm = 24 
_SW_A = 19
_SW_B = 18
_SW_C = 22

# uCompute NRF24l01+ Radio Module
#_SPI1_SCK = 14 # SPI1_shared Clock with SD Card
#_SPI1_MOSI = 15 # SPI1_shared MOSI with SD Card
#_SPI1_MISO = 12 # SPI1_shared MISO with SD Card
_NRF24l01_CSN = Pin(8, mode=Pin.OUT, value=1)  # Chip Select (LOW during SPI)
_NRF24l01_CE  = Pin(10, mode=Pin.OUT, value=0)  # Enable TX/RX (HIGH); standby (LOW)
_NRF24l01_IRQ  = Pin(9, mode=Pin.IN)  # IRQ (Interrupt): Optional. Goes LOW when data is received or transmission completes.
payload_size = 20
_NRF24l01_Channel=2
# RF_SETUP register
_NRF24l01_POWER_0 = const(0x00)  # -18 dBm
_NRF24l01_POWER_1 = const(0x02)  # -12 dBm
_NRF24l01_POWER_2 = const(0x04)  # -6 dBm
_NRF24l01_POWER_3 = const(0x06)  # 0 dBm
_NRF24l01_SPEED_1M = const(0x00)
_NRF24l01_SPEED_2M = const(0x08)
_NRF24l01_SPEED_250K = const(0x20)

role = "Transmitter"
#role = "Receiver"
if role == "Transmitter":
    send_pipe = b"\xe1\xf0\xf0\xf0\xf0"
    receive_pipe = b"\xd2\xf0\xf0\xf0\xf0"
else:
    send_pipe = b"\xd2\xf0\xf0\xf0\xf0"
    receive_pipe = b"\xe1\xf0\xf0\xf0\xf0"
#
#
# set landscape screen
screen_width = 240
screen_height = 240
screen_rotation = 1
#gestion de la sortie STDOUT sur l'ecran LCD
TTY_Pointer=0
WrapScreen= int(screen_height/20)-1  # nombre de ligne avant de wrapper sur l'écran /10 si charactere 8x8
TTY = ['']*WrapScreen# creation d'une matrice pour emuler un TTY

#-------------------------------------
#
# Début de l'initialisation 
#

#Initialisation des IOs
System_LED = Pin(_Led_System,Pin.OUT)
COMM_LOST = Pin(_Led_Lost_comm,Pin.OUT)
MicroSD_Detect = Pin(_MicroSD_Detect,Pin.IN)
BTN_Analogue = machine.ADC(_Boutons) #Diviseur de tension des boutons


#initialisation du bus I2C
i2c=I2C(0,sda=Pin(_I2C_SDA), scl=Pin(_I2C_SCL), freq=200000)
# -----------------------------------
# Choisir la résolution du OLED
#
oled = SSD1306_I2C(128, 64, i2c)
#oled = SSD1306_I2C(128, 32, i2c)
#------------------------------------


def WaitInputKey():
    while BTN_Analogue.read_u16()>64000: # attend any key
        utime.sleep(.05)

def PrintTTY(texte):
#------------------------------------------------------------------------------------
# Fonctions permettant d'utiliser le display comme un TTY pour afficher les logs
# et de scroller automatiquement
#------------------------------------------------------------------------------------
    global TTY_Pointer # en utilisant une variable global, cela permet d'initialiser une seule fois la variable. Il y a surement une facon plus elegante, pour garder l'etat d'une variable locale dans une fonction. 
    
    if TTY_Pointer < WrapScreen:
        TTY[TTY_Pointer]=texte[:15] # je limite le texte a la largeur de l'ecran
        TTY_Pointer+=1
    else: #  dans le cas ou je suis a la derniere ligne de l'ecran, je decale vers le haut
        for i in range(WrapScreen-1):
            TTY[i] = TTY[i+1] # je decale vers le haut
        TTY[TTY_Pointer-1]=texte[:15] # je limite le texte a la largeur de l'ecran
# j'affiche le texte sur l'ecran 
    fbuf.fill(st7789.BLACK)
    for i in range(TTY_Pointer):
        line_ptr=i*20
        fbuf.large_text(TTY[i],0,line_ptr,2,st7789.LIME)
     
    display.blit_buffer(buffer, 0, 0, buffer_width, buffer_height) # render display

def setup_NRF24l01():
    print("Initialising the nRF24L0+ Module")
    spi = SPI(1, sck=Pin(_SPI1_SCK), mosi=Pin(_SPI1_MOSI), miso=Pin(_SPI1_MISO))
    nrf = NRF24L01(spi, _NRF24l01_CSN, _NRF24l01_CE, channel=_NRF24l01_Channel,  payload_size=payload_size)
    nrf.open_tx_pipe(send_pipe)
    nrf.open_rx_pipe(1, receive_pipe)
    nrf.start_listening()
    nrf.set_power_speed(_NRF24l01_POWER_3, _NRF24l01_SPEED_250K)  # Best for point to point links

    return nrf

def SplashScreen():
    oled.fill(0)
    oled.text('----------------', 0, 0)
    oled.text('RC REMOTE TEST', 10, 10)
    oled.text('----------------', 0, 20)
    oled.text('[Press AnyKey]', 5, 50)
    oled.show()
    
def MainDisplay(p_gauche, p_droite):    
    oled.fill(0)
    oled.text('Main Display', 10, 0)
    oled.text('Motors', 10, 30)
    oled.text(str(p_gauche) +"  " + str(p_droite), 10, 45)
    oled.show()

def init_puissance():
    # 'h' signifie "signed short" (entier 16 bits signé), idéal pour -100 à 100
    # On envoie deux valeurs : moteur gauche et moteur droit
    COMM_LOST(0)
    payload = struct.pack("hh", 0, 0)
    try:
        nrf.send(payload)
        LastPayload=payload
        #print(f"Envoyé: G={p_gauche}, D={p_droite}")
    except OSError:
        #print("Erreur d'envoi (pas de réponse du robot)")
        COMM_LOST(1)
        
def envoyer_puissance(p_gauche, p_droite):
    # 'h' signifie "signed short" (entier 16 bits signé), idéal pour -100 à 100
    # On envoie deux valeurs : moteur gauche et moteur droit
    COMM_LOST(0)
    payload = struct.pack("hh", p_gauche, p_droite)
    try:
        nrf.send_start(payload)
        LastPayload=payload
        #print(f"Envoyé: G={p_gauche}, D={p_droite}")
    except OSError:
        #print("Erreur d'envoi (pas de réponse du robot)")
        COMM_LOST(1)
        
def get_motor_powers(x_val, y_val, resolution=65535):
    # 1. Normalisation : conversion de 0-65535 vers -100 à 100
    # On définit le neutre au centre (env. 32767)
    center = resolution / 2
    x = ((x_val - center) / center) * 100
    y = ((y_val - center) / center) * 100
    
    # Zone neutre (deadzone) pour éviter que les moteurs buzz au repos
    if abs(x) < 4: x = 0
    if abs(y) < 4: y = 0

    # 2. Algorithme de mixage (Vecteur Y = Avancer/Reculer, Vecteur X = Pivoter)
    left_power = y + x
    right_power = y - x

    # 3. Contrainte (Clamping) entre -100% et 100%
    left_power = max(min(left_power, 100), -100)
    right_power = max(min(right_power, 100), -100)

    return int(left_power*-1), int(right_power*-1)

def flash_led(times:int=None):
    ''' Flashed the built in LED the number of times defined in the times parameter '''
    for _ in range(times):
        System_LED(1)
        sleep(0.01)
        System_LED(0)
        sleep(0.01)
        
#--------------------------------------------------------------------------------------------------------------------------------------------------
#
#
#--------------------------------------------------------------------------------------------------------------------------------------------------
flash_led(1)
SplashScreen()
WaitInputKey()
try:
    nrf = setup_NRF24l01()
except OSError:
    print("NRF24l01 not found")
    COMM_LOST(1)
    oled.fill(0)
    oled.text('err Comm. Module', 0, 0)
    oled.text('-----------------', 0, 10)
    oled.text("nRF24L0+", 25, 30)
    oled.text("not found", 20, 40)
    oled.show()
    while True: # puisqu'il y a une erreure, je boucle en infini car cela ne sert a rien de continuer
        utime.sleep(0.1)
init_puissance() #initialisation puissance 0,0 pour ouvrir le canal de communication        
p_gauche=0
p_droite=0

while True:
    # Read 16-bit value (0 - 65535)
    Last_G = p_gauche
    Last_D = p_droite
    value_X = _analog_X.read_u16()
    value_Y = _analog_Y.read_u16()
    # --- Exemple d'utilisation ---
    # Si x=65535 (droite toute) et y=65535 (avant toute)
    p_gauche, p_droite = get_motor_powers(value_X, value_Y)
    envoyer_puissance(p_gauche, p_droite)
    MainDisplay(p_gauche, p_droite)
    