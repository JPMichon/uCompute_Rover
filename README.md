# uCompute_Rover
4WD Rover  conçu pour utiliser les modules uCompute 1 ou 2 comme fondation.

### Materiel requis
* 4 X DC Gearbox Motor - "TT Motor" - 200RPM - 3 to 6VDC
* 2 X DRV8833 Dual H-Bridge Motor Control Module 1.5A 3-10V
* 1 X uCompute RP2040 ver1.3 module (Rover)
* 1 X uCompute-Rover ver1.0
* 1 X LM2596 DC-DC Step Down converter de 3 A (ou éqivalent)
* 6 x AA Battery Case Shell Storage Holder (ou éqivalent)
  
### Optionels
* 1 X SG90 Micro Servo Motor
* 1 X Ultrasonic sensor HC-SR04 HCSR04 
* 1 X Diagramme du rover
* 1 X 10*15mm Snap-in Rocker Switch ON-OFF 
* 2 X NRF24l01+
* 2 X NRF24L01+ Radio Module
* 1 X uCompute RP2040 ver1.3 module (Remote)
* 1 X uCompute-Remote controller
* 1 X INA219 I2C Current Voltage Power Sensor 
* 1 X GY-NEO-6M GPS module, active ceramic antenna,
* 1 X GY-530 VL53L0X Time-o F-Flight (ToF) Laser Ranging Sensor
* 1 X GY-271 QMC5883L 3V-5V Three 3 Triple Axis Magnetic Field Compass Magnetometer Sensor
* 1 X AMG8833 IR 8x8 Thermal Imager Array Temperature Sensor Module
* 1 X AHT20+BMP280 Temperature Humidity and Air Pressure Module High-precision Digital Sensor IIC I2C
* 1 X ENS160+AHT21 Carbon Dioxide CO2 eCO2 TVOC Air Quality & Temperature & Humidity Sensor Module
* Ou autres modules selon vos préférences

## Vue d'ensemble du Rover
![Diagramme du rover](https://github.com/JPMichon/uCompute_Rover/blob/main/Rover_Diagram_V1.png)

# Rover Module
Le Rover module est un module ce connectant a l'interface du board principale. Celui est intègre le port VIN devant absolument etre alimenter en CC 5volts avec une source pouvant délivrer environ 2 amp. 
De ce 5 volts est alimenté directement, le servo, le HC-SR04, les deux modules DRV8833 et finalement, il alimente la broche 5 volts du module principale servant de CC pour le circuit de régulation. 
Le module GPS est alimenté en 3.3volts a partir du régulateur du module principale. 
![PCB du module](https://github.com/JPMichon/uCompute_Rover/blob/main/electronique/Rover_pcb.png)
![vue 3D du module](https://github.com/JPMichon/uCompute_Rover/blob/main/electronique/Rover_module.png)
