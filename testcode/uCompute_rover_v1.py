from machine import I2C, UART, SPI, PWM, Pin
import st7789 as st7789
import framebuf2
import time
import ahtx0
import ina219
from myENS160 import myENS160

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
_ATH20_ADDR = 0x38 # adresse du ATH20
_INA219_ADDR = 0x40 # adresse du INA219
_INA219_SHUNT_OHMS = 0.1  # Check value of shunt used with your INA219
_Boutons = 26 # définition du port analogue des boutons (GP26)
_UART = 0 # UART par defaut
_TX_PIN = 0 # TX Pin (GP0)
_RX_PIN = 1 # TX Pin (GP1)
_BaudRate = 9600 # Baud rate du UART
# set landscape screen
screen_width = 240
screen_height = 240
screen_rotation = 1
#gestion de la sortie STDOUT sur l'ecran LCD
TTY_Pointer=0
WrapScreen= int(screen_height/20)-1  # nombre de ligne avant de wrapper sur l'écran /10 si charactere 8x8
TTY = ['']*WrapScreen# creation d'une matrice pour emuler un TTY

#Parametre pour le diagnostique lors du demarrage
SCAN_I2C=False # Affiche le scan du I2C
FastBoot=False # skip la lecture des capteurs au demarrage


#-------------------------------------
#
# Début de l'initialisation 
#

#Initialisation des IOs
System_LED = Pin(_Led_System,Pin.OUT)
MicroSD_Detect = Pin(_MicroSD_Detect,Pin.IN)
BTN_Analogue = machine.ADC(_Boutons) #Diviseur de tension des boutons

spi = SPI(0,baudrate=20000000,polarity=1,phase=1,bits=8,firstbit=SPI.MSB,sck=Pin(_ST7789_SCK),mosi=Pin(_ST7789_MOSI))
display = st7789.ST7789(spi,screen_width,screen_height,reset=Pin(_ST7789_RESET, Pin.OUT),dc=Pin(_ST7789_DC, Pin.OUT),backlight=Pin(_ST7789_BL, Pin.OUT),rotation=screen_rotation)

#initialisation du bus I2C
i2c=I2C(0,sda=Pin(_I2C_SDA), scl=Pin(_I2C_SCL), freq=200000)



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
    
def PrintSplash():    
#------------------------------------------------------------------------------------
# Splash Screen
#------------------------------------------------------------------------------------
    PrintTTY("--------------")
    PrintTTY("uCompute-Rover")
    PrintTTY("          V1.0")
    PrintTTY("--------------")
    PrintTTY("")

def ScanI2C():    
#------------------------------------------------------------------------------------
# Scan Sensor I2C BUS
# Registre des adresses i2c
# 0x2c  =  GY273 (HMC5883L)3-Axis Digital Compass
# 0x38  = AHT10/AHT20 temperature+humidity sensor
# 0x3c  = OLED SSD1306
# 0x40  = INA219 Current/Power Monitor
# 0x50  = EEPROM
# 0x53  = ENS160
#------------------------------------------------------------------------------------
    PrintTTY("I2C Scan")
    devices = i2c.scan()
    if len(devices) == 0:
      PrintTTY("No i2c device!")
    else:
      PrintTTY('found:'+str(len(devices)))

      for device in devices:  
        PrintTTY("addr: "+hex(device))
    PrintTTY("")
    
def TestSensors():    
#------------------------------------------------------------------------------------
# Test Sensor I2C BUS    
    PrintTTY("---------------")
    PrintTTY("-Test sensors-")
    PrintTTY("---------------")
    PrintTTY("")
    PrintTTY("Test ATH20")
    if sensor_ATH20_Present:
        PrintTTY("Temp: "+str(round(sensor_ATH20.temperature,1))+"c")
        PrintTTY("Humi: "+str(round(sensor_ATH20.relative_humidity,1))+"%")
    else:
        PrintTTY("Not found")    
    PrintTTY("")
    PrintTTY("")
    PrintTTY("Test INA219")
    if sensor_INA219_Present:
        PrintTTY("Curr.:" +str(f"{sensor_INA219.current:.3f}"+" mA"))
        PrintTTY("Volts:" +str(f"{sensor_INA219.bus_voltage:.3f}"+" V"))
        PrintTTY("Power:" +str(f"{((sensor_INA219.current/100)*sensor_INA219.bus_voltage):.3f}"+" Watt"))
    else:
        PrintTTY("Not found") 
    PrintTTY("")
    PrintTTY("")
    PrintTTY("Test ENS160")
    if sensor_ENS160_Present:
        PrintTTY("TVOC:" +str(ENS160.getTVOC()))
        PrintTTY("AQI:" +str(ENS160.getAQI()))
        PrintTTY("ECO2:" +str(ENS160.getECO2()))
    else:
        PrintTTY("Not found") 

# Initialisation du FrameBuffer
# FrameBuffer needs 2 bytes for every RGB565 pixel
buffer_width = 240
buffer_height = 240
buffer = bytearray(buffer_width * buffer_height * 2)
fbuf = framebuf2.FrameBuffer(buffer, buffer_width, buffer_height, framebuf2.RGB565)
fbuf.fill(st7789.BLACK) #flush le display
display.blit_buffer(buffer, 0, 0, buffer_width, buffer_height) # render display

#---------------------------------------------------------------------
#-------------------------------------------------------------------
# Scan les differents sensors pour determiner la presence de ceux-ci
#
#
sensor_ATH20_Present=True
sensor_INA219_Present=True
sensor_ENS160_Present=True
EEPROM_Present=True

PrintSplash()
if SCAN_I2C:
    ScanI2C()
PrintTTY("-- Sensors --") 
try:
    sensor_ATH20 = ahtx0.AHT10(i2c, address=_ATH20_ADDR)
    PrintTTY("ATH20  - Found")
except:
    sensor_ATH20_Present=False
    PrintTTY("ATH20  - Failed")
try:    
    sensor_INA219 = ina219.INA219(i2c, addr=_INA219_ADDR)
    PrintTTY("INA219 - Found")
except:
    sensor_INA219_Present=False
    PrintTTY("INA219 - Failed")
try:
    EEP = eeprom_i2c.EEPROM(i2c, T24C64, addr=_EEPROM_ADDR)  
    PrintTTY("EEPROM - Found")
except:
    EEPROM_Present=False
    PrintTTY("EEPROM - Failed")
try:
    ENS160 = myENS160(i2c)
    PrintTTY("ENS160 - Found")
except:
    sensor_ENS160_Present=False
    PrintTTY("ENS160 - Failed")
    
if FastBoot==False:
    TestSensors()
PrintTTY("") 
PrintTTY("-Completed-")    
    