#----------------------------------------------------------------
# Programme pour tester les connections des moteurs sur le Rover
#afin que ceux-ci tourne dans la bonne direction
# # il est concu pour utiliser un SSD1306 connecté sur le uCompute
#
#----------------------------------------------------------------



from machine import Pin,  I2C, SPI, PWM
from ssd1306 import SSD1306_I2C
from nrf24l01 import NRF24L01
import _thread
import struct
import ina219
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
_INA219_ADDR = 0x40 # adresse du INA219
_INA219_SHUNT_OHMS = 0.1  # Check value of shunt used with your INA219
_Boutons = 26 # définition du port analogue des boutons (GP26)


    
_Servo_pin = 28
_HCSR04_Trigger_pin = 27
_HCSR04_Echo_pin = 24
_GPS_TX = 0
_GPS_RX = 1

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

#role = "Transmitter"
role = "Receiver"
if role == "Transmitter":
    send_pipe = b"\xe1\xf0\xf0\xf0\xf0"
    receive_pipe = b"\xd2\xf0\xf0\xf0\xf0"
else:
    send_pipe = b"\xd2\xf0\xf0\xf0\xf0"
    receive_pipe = b"\xe1\xf0\xf0\xf0\xf0"
    
#-----------------------------------------------------------------------------------
#Initialisation
i2c=I2C(0,sda=Pin(_I2C_SDA), scl=Pin(_I2C_SCL), freq=200000)
#Initialisation des IOs

System_LED = Pin(_Led_System,Pin.OUT)
MicroSD_Detect = Pin(_MicroSD_Detect,Pin.IN)
BTN_Analogue = machine.ADC(_Boutons) #Diviseur de tension des boutons

#Configuration des Ports pour le Roverboard
_nsleep_Motors = 22 # desactivation des moteurs de traction (0=disable, 1=enable)
_MoteurDroiteA = PWM(Pin(18))
_MoteurDroiteB = PWM(Pin(19))
_MoteurGaucheA = PWM(Pin(16))
_MoteurGaucheB = PWM(Pin(17))

# Fréquence PWM (entre 1000 et 40000 Hz recommandé pour DRV8833)
for p in [_MoteurGaucheA, _MoteurGaucheB, _MoteurDroiteA, _MoteurDroiteB]:
    p.freq(30000)

nsleep=Pin(_nsleep_Motors, Pin.OUT)
nsleep.value(1) #Pour enabler les modules DRB8833, la pin nsleep doit etre a 1
# -----------------------------------
#Configuration de la résolution du OLED
oled = SSD1306_I2C(128, 64, i2c)  
sensor_INA219 = ina219.INA219(i2c, addr=_INA219_ADDR)

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
    nrf.set_power_speed(_NRF24l01_POWER_3, _NRF24l01_SPEED_250K)  # Best for point to point links
    nrf.open_tx_pipe(send_pipe)
    nrf.open_rx_pipe(1, receive_pipe)
    nrf.start_listening()
    
    return nrf

def WaitInputKey():
    while BTN_Analogue.read_u16()>64000: # attend any key
        utime.sleep(.05)
        
def SplashScreen():    
    oled.fill(0)
    oled.text('----------------', 0, 0)
    oled.text('Rover tests', 25, 10)
    oled.text('----------------', 0, 20)
    oled.text('Rover RC', 25, 35)
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

def Network_thread():
    nrf.start_listening()
    global p_gauche
    global p_droit
    global data_update
    p_gauche = 0
    p_droit = 0
    
    while True:
        if nrf.any():
            buf = nrf.recv()
            # Décompression des deux entiers 'short' signés
            temp_gauche = p_gauche
            temp_droit = p_droit
            p_gauche, p_droit = struct.unpack("hh", buf)
            controler_moteur(_MoteurGaucheA, _MoteurGaucheB, p_gauche)
            controler_moteur(_MoteurDroiteA, _MoteurDroiteB, p_droit)
        System_LED.toggle() # je fais flasher la led GP25 afin de valider que la tache fonctionne

        
def controler_moteur(in1, in2, puissance):
    # Conversion -100/100 vers 0-65535 (duty cycle MicroPython)
    duty = int((abs(puissance)/4+75) * 655.35)
    if puissance > 0:   # Marche avant
        in1.duty_u16(duty)
        in2.duty_u16(0)
    elif puissance < 0: # Marche arrière
        in1.duty_u16(0)
        in2.duty_u16(duty)
    else:               # Stop
        in1.duty_u16(0)
        in2.duty_u16(0)
  


#---------------------------------------------------------------------------------
# Main loop
#---------------------------------------------------------------------------------
SplashScreen()
WaitInputKey()
# tentative d'initialisation du module du NRF24l01
try:
    nrf = setup_NRF24l01()
except OSError:
    print("NRF24l01 not found")
    oled.fill(0)
    oled.text('err Comm. Module', 0, 0)
    oled.text('-----------------', 0, 10)
    oled.text("nRF24L0+", 25, 30)
    oled.text("not found", 20, 40)
    oled.show()
    while True: # puisqu'il y a une erreure, je boucle en infini car cela ne sert a rien de continuer
        utime.sleep(0.2)
# demmarage de la seconde tache s'occupant de la gestion des communication et du controle des moteurs
_thread.start_new_thread(Network_thread, ()) # network/ motors controls

while True:
    oled.fill(0)
    oled.text("Curr.:" +str(f"{sensor_INA219.current:.2f}"+" mA"),20, 0)
    oled.text("Volts:" +str(f"{sensor_INA219.bus_voltage:.2f}"+" V"),20, 10)
    #oled.text("Power:" +str(f"{((sensor_INA219.current/100)*sensor_INA219.bus_voltage):.3f}"+" Watt"))
    oled.text('Left      Right', 0, 40)
    oled.text(str(p_gauche)+"        "+str(p_droit), 0, 50)
    # Application aux moteurs
    print(f"Moteurs -> G: {p_gauche}, D: {p_droit}")
    oled.show()