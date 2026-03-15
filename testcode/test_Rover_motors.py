#----------------------------------------------------------------
# Programme pour tester les connections des moteurs sur le Rover
#afin que ceux-ci tourne dans la bonne direction
# # il est concu pour utiliser un SSD1306 connecté sur le uCompute
#
#----------------------------------------------------------------



from machine import Pin,  I2C
from ssd1306 import SSD1306_I2C
import utime


#Configuration des Ports pour le uCompute V1.x
_MicroSD_Detect = 7 # détection de la présence d'une carte MicroSD (GP7)
_MicroSD_Select = 13 # définition de la pin Select du SDCARD (GP13)
_W5500_Select = 8 # définition de la pin Select du W5500 (GP8)
_W5500_Reset = 10 # définition de la pin Reset du W5500 (GP10)
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
_NeoPixel_nbr = 8 # nombre de neopixel sur le port
_EEPROM_ADDR = 0x50 # adresse du eeprom
_Boutons = 26 # définition du port analogue des boutons (GP26)

#Configuration des Ports pour le Roverboard
_nsleep_Motors = 22 # desactivation des moteurs de traction (0=disable, 1=enable)
_MoteurDroiteA = 18
_MoteurDroiteB = 19
_MoteurGaucheA = 16
_MoteurGaucheB = 17
_Servo_pin = 28
_HCSR04_Trigger_pin = 27
_HCSR04_Echo_pin = 24
_GPS_TX = 0
_GPS_RX = 1
#-----------------------------------------------------------------------------------
#Initialisation
i2c=I2C(0,sda=Pin(_I2C_SDA), scl=Pin(_I2C_SCL), freq=200000)
#Initialisation des IOs

System_LED = Pin(_Led_System,Pin.OUT)
MicroSD_Detect = Pin(_MicroSD_Detect,Pin.IN)
BTN_Analogue = machine.ADC(_Boutons) #Diviseur de tension des boutons

#Moteurs Droit
motor1a = Pin(_MoteurDroiteA, Pin.OUT) 
motor1b = Pin(_MoteurDroiteB, Pin.OUT)
#Moteurs Gauche
motor2a = Pin(_MoteurGaucheA, Pin.OUT) 
motor2b = Pin(_MoteurGaucheB, Pin.OUT)

nsleep=Pin(_nsleep_Motors, Pin.OUT)
nsleep.value(1) #Pour enabler les modules DRB8833, la pin nsleep doit etre a 1
# -----------------------------------
#Configuration de la résolution du OLED
oled = SSD1306_I2C(128, 64, i2c)


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

def WaitInputKey():
    while BTN_Analogue.read_u16()>64000: # attend any key
        utime.sleep(.05)
        
def SplashScreen():    
    oled.fill(0)
    oled.text('----------------', 0, 0)
    oled.text('Rover tests', 25, 10)
    oled.text('----------------', 0, 20)
    oled.text('Press anykey', 20, 55)
    oled.show()

def Read_Keys():
    _read = BTN_Analogue.read_u16()
    _KeyPress='null'
    if _read < 8000: #Down
        _KeyPress='down'
    elif _read < 13000: #Select
        _KeyPress='select'
    elif _read < 18000: # Up
        _KeyPress='up'          
    #print(str(_read)) #pour le debuggage affiche la lecture de la clé dans la console    
    return _KeyPress #+str(_read)
    

def forward_left():
   motor2a.high()
   motor2b.low()

def forward_right():
   motor1a.high()
   motor1b.low()
   
def backward_left():
   motor2a.low()
   motor2b.high()
   
def backward_right():
   motor1a.low()
   motor1b.high()

def stop():
   motor1a.low()
   motor1b.low()
   motor2a.low()
   motor2b.low()   


#---------------------------------------------------------------------------------
# Main loop
#---------------------------------------------------------------------------------
SplashScreen()
WaitInputKey()
oled.fill(0)
oled.text('Press buttons to', 0, 15)
oled.text('move forward', 15, 25)
oled.text('Left      Right', 0, 55)
oled.show()
stop()
while True:

    _tempo=Read_Keys() # lecture des boutons analogiques
    if _tempo == "down":
        forward_right()
    elif _tempo == "up":
        forward_left()
    else:
        stop()
    utime.sleep(.1) # Je ralenti la loop pour debouncer les boutons pour eviter les reactions ératiques        