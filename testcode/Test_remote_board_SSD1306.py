from machine import SPI, Pin, I2C
from time import sleep
from ssd1306 import SSD1306_I2C
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
LED_WARNING = Pin(_Led_Warning, Pin.OUT)
System_LED = Pin(_Led_System, Pin.OUT)
LED_COMM_LOST = Pin(_Led_Lost_comm, Pin.OUT)
LED_OBSTACLE = Pin(_Led_Obstacle, Pin.OUT)

BTN_Analogue = machine.ADC(_Boutons) #Diviseur de tension des boutons
SWITCH_A=Pin(_SW_A,Pin.IN)
SWITCH_B=Pin(_SW_B,Pin.IN)
SWITCH_C=Pin(_SW_C,Pin.IN)

i2c=I2C(0,sda=Pin(_I2C_SDA), scl=Pin(_I2C_SCL), freq=200000)
# -----------------------------------
# Choisir la résolution du OLED
#
oled = SSD1306_I2C(128, 64, i2c)
#oled = SSD1306_I2C(128, 32, i2c)
#------------------------------------
#


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



def flash_led(times:int=None):
    ''' Flashed the built in LED the number of times defined in the times parameter '''
    for _ in range(times):
        System_LED(1)
        sleep(0.01)
        System_LED(0)
        sleep(0.01)
        
#--------------------------------------------------------------------------------------------------------------------------------------------------
#  Main loop
#
#--------------------------------------------------------------------------------------------------------------------------------------------------



resolution=65535
LED_OBSTACLE.high()
LED_WARNING.high()
LED_COMM_LOST.high()
oled.text('----------------', 0, 0)
oled.text('RC REMOTE TEST', 10, 10)
oled.text('----------------', 0, 20)
oled.show()
sleep(2)
oled.fill(0)
oled.show()
center = resolution / 2
adjust_trim_x = 0
adjust_trim_y = -500
while True:
    # Read 16-bit value (0 - 65535)

    value_X = _analog_X.read_u16()
    value_Y = _analog_Y.read_u16()
    x = (((value_X - adjust_trim_x)  - center) / center) * 100
    y = (((value_Y - adjust_trim_y)- center) / center) * 100
    # --- Exemple d'utilisation ---
    # Si x=65535 (droite toute) et y=65535 (avant toute)
    oled.fill(0)
    oled.text("x=:" + str(int(x)),0,45)
    oled.text("y=:" + str(int(y)),0,55)
    oled.show()
    if not(SWITCH_A.value()):
        LED_OBSTACLE.toggle()
        sleep(0.1)
        
    if not(SWITCH_B.value()):
        LED_WARNING.toggle()
        sleep(0.1)
        
    if not(SWITCH_C.value()):
        LED_COMM_LOST.toggle()
        sleep(0.1)
               
        