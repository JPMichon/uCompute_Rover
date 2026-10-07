# 🤖 uCompute Rover

## [Version française disponible ici](./README.md)

![3D View](https://github.com/JPMichon/uCompute_Rover/blob/main/Rover_3D.png)

## 🛠️ Required Hardware
* 4 x DC Gear Motors — "TT Motor" — 200 RPM (3 to 6 VDC)
* 2 x DRV8833 — Dual H-Bridge Motor Drivers (1.5 A, 3 to 10 V)
* 1 x uCompute RP2040 Module v1.3 (Rover)
* 1 x uCompute-Rover Board v1.0
* 1 x LM2596 DC-DC Buck Converter (3 A or equivalent)
* 1 x 6-AA Battery Holder (or equivalent)

## ⚙️ Options and Extensions
* 1 x SG90 Micro Servo Motor
* 1 x HC-SR04 / HCSR04 Ultrasonic Sensor
* 1 x Rover Wiring Diagram
* 1 x Snap-in Rocker Switch 10x15 mm (ON-OFF)
* 2 x nRF24L01+ Radio Modules
* 1 x uCompute RP2040 Module v1.3 (Remote)
* 1 x uCompute Remote Controller
* 1 x INA219 I2C Power Sensor and Voltage/Current Monitor
* 1 x GY-NEO-6M GPS Module with Active Ceramic Antenna
* 1 x GY-530 VL53L0X Laser ToF (Time-of-Flight) Distance Sensor
* 1 x GY-271 QMC5883L 3-Axis Magnetic Compass (3V-5V)
* 1 x AMG8833 Infrared Thermal Camera (8x8 Sensor Grid)
* 1 x AHT20+BMP280 I2C High-Precision Temperature, Humidity, and Air Pressure Module
* 1 x ENS160+AHT21 Air Quality Analysis Module (CO2, eCO2, TVOC)
* *Any other optional module according to your preferences.*

---

# 🔌 Electronic Architecture & Modularity

The **uCompute Rover** project is built on a fully modular hardware architecture. This repository focuses specifically on the chassis, mechanical assembly, and the rover interface board (*Rover board*). 

The "brain" and the various required communication modules come from the global **RP2040 uCompute** ecosystem.

---

## 🔗 Parent Repository & Electronics Documentation

To manufacture, program, or understand the detailed operation of the main board and its modules, please refer to the primary repository:

👉 **[GitHub - RP2040 uCompute](https://github.com/JPMichon/RP2040_uCompute)**

You will find:
* 📂 Hardware design files (**Gerber**, circuit diagrams, and Bills of Materials BOM).
* 📂 The modules.
* 📍 Full pinout mapping and technical specifications of the platform.

## Assembly Guides
The guide is split into 3 sections (hardware, electronics, and code):
* Rover assembly can be found in the 📂 **3D_Parts** directory
* Sensor and electronics installation in the 📂 **Electronic** directory
* Component operation validation in the 📂 **testcode** directory
  
---

## ⚡ Schematic View of the Onboard Electronics
<p align="center">
<img width="500" height="550" alt="image" src="https://github.com/user-attachments/assets/00ff8261-1ec5-4b57-87cb-6808611c9471" />
</p>

---

### 🧠 The Heart of the System: uCompute
The robot's onboard intelligence utilizes the **uCompute** autonomous development platform (based on the Raspberry Pi RP2040 microcontroller). It handles the execution of driving scripts (MicroPython), the graphical diagnostic interface, and the centralization of sensor data.<br>
<img width="775" height="350" alt="image" src="https://github.com/user-attachments/assets/4a8f9f4d-8950-45fe-b8cd-cc78aa2371bc" />

---

### 💡 An Open and Universal Architecture

Although the project is designed around the **uCompute** (RP2040) ecosystem, the motor control module was developed in a pure spirit of software and hardware freedom. The entire structure is completely agnostic: the power module uses **3.3V** logic signals. This means a **maker** can easily adapt this chassis and extension module to control them with an **ESP32**, an **Arduino**, or any other development platform of their choice, by crafting their own control module or by using the project's modules and simply adapting the wiring and the driving script.<br>

 ### 🏎️💨 For More Demanding Makers
 It is entirely feasible to integrate a more robust solution, such as a **Raspberry Pi**. Using a microcomputer of this caliber allows for handling heavy computing tasks or more complex scripts. However, care must be taken to adjust the circuit's power supply module: unlike traditional microcontrollers, a Raspberry Pi requires a stable power source and a **higher current (3A for a Pi 4 Model B) + (1A for the 4 motors) = 4A 5V DC** to ensure stability. Once this electrical, software, and hardware adaptation is done, the possibilities for your build will be endless.<br>
 
**Feel free to create a Frankenstein! 🧟‍♂️**

---

### 📻 Extension Modules (Add-ons)
To ensure wireless connectivity and bidirectional telemetry with the remote controller, the rover utilizes interchangeable extension modules from the main project (specifically the **NRF24L01+** radio module).

👉 **[RP2040_uCompute Modules](https://github.com/JPMichon/RP2040_uCompute/tree/main/Modules)**

| Location | Module | Description & Features | Visual Render |
| :--- | :--- | :--- | :--- |
| **Rear Socket** (Communication) | **Wi-Fi Module** (ESP-12F) | Adapter board with ESP8266 for Wi-Fi connectivity. | <img width="100" height="133" alt="image" src="https://github.com/user-attachments/assets/f0c80621-1b07-46e6-844b-4594e3d338f9" />  |
| **Rear Socket** (Communication) | **Radio Module** (NRF24L01) | Adapter board for 2.4 GHz radio links. | <img width="112" height="140" alt="image" src="https://github.com/user-attachments/assets/a6a0a83b-80ed-4dbc-bc28-06579f64b54c" /> |
| **Pin Headers** <br> (IO Connector) | **µCompute Remote** <br> (REV 1.0) | Analog control module with buttons. | <img width="175" height="131" alt="image" src="https://github.com/user-attachments/assets/25dda003-8ab8-48c4-a7d1-1a45fdbca7a4" /> |
| **Pin Headers** <br> (IO Connector) | **µCompute Rover** <br> (REV 1.0) | DC motor controller (2+2) + Servo + HC-SR04 + GPS Module (Neo-6M). | <img width="220" height="145" alt="image" src="https://github.com/user-attachments/assets/90114819-d70b-4cbb-8cfd-5e95b66cca84" /> |

---

## 🎮 Remote Control (RC Mode)

The **uCompute Rover** features a standalone radio-controlled (RC) driving mode. The remote controller is built around a second uCompute module equipped with an analog joystick, push-buttons, an OLED **SSD1306** display, and an **NRF24L01+** radio module.

<p align="center">
  <img width="495" height="676" alt="image" src="https://github.com/user-attachments/assets/c12b0136-ba45-4c3e-a211-9a4611322f68" />
</p>

### 📐 Mechanical Design and 3D Case
The controller's ergonomics have been specially designed to provide a comfortable grip thanks to integrated side handles.
* 📁 The STL file for the case is available here: **[RC_remote_v1.stl](https://github.com/JPMichon/uCompute_Rover/blob/main/3D_Parts/RC_remote_v1.stl)**

### 💾 Test Scripts (MicroPython)
The system relies on two separate scripts that manage real-time bidirectional communication (sending steering commands and receiving telemetry on the OLED screen):

1. **Remote Control Side:** **[Remote_Rover_v1_SSD1306.py](https://github.com/JPMichon/uCompute_Rover/blob/main/testcode/Remote_Rover_v1_SSD1306.py)**
   * Initializes the SPI bus for the NRF24L01+ radio module.
   * Reads the status of the analog joystick (X/Y axes) and control buttons.
   * Manages the display of system information on the local OLED screen.
   * Periodically transmits command packets to the rover.

2. **Rover Side:** **[RC_Rover_v1_SSD1306.py](https://github.com/JPMichon/uCompute_Rover/blob/main/testcode/RC_Rover_v1_SSD1306.py)**
   * Listens for radio packets transmitted by the remote control.
   * Decodes trajectory and speed instructions to drive the DC motors via the DRV8833 H-bridges.
   * Manages safety features (automatic emergency stop of the motors in case of radio link loss).

---
  
## 🚀 Evolution Towards an Autonomous Rover and Telemetry

Although the project is initially presented with a radio-controlled (RC) driving mode, the hardware architecture of the **uCompute Rover** was designed from the ground up for modularity. Thanks to its numerous onboard sensors, the robot can easily be transformed into a **100% autonomous vehicle**.

### 🤖 Scalable Autonomous Logic
The interface board (*Roverboard*) natively interconnects all essential components to allow the RP2040 microcontroller to make real-time decisions:
* **Obstacle avoidance:** The **HC-SR04** ultrasonic sensor (or the **VL53L0X** ToF laser sensor) allows mapping the immediate environment and adapting the trajectory.
* **Navigation and orientation:** Adding the **GY-271** magnetic compass and the **NEO-6M** GPS module paves the way for waypoint navigation algorithms.

Switching to autonomous mode requires no major hardware modifications: it is primarily a **software deployment** (automatic trajectory control scripts in MicroPython).

### 🌐 Control via Web Interface (Wi-Fi)
Since a **Wi-Fi module (ESP-12F)** is available within the uCompute ecosystem (designed to plug into the rear communication socket), remote control possibilities extend to IP networks. 

By deploying a MicroPython HTTP micro-server on the uCompute, it becomes possible to:
* **Drive the rover from any device** (smartphone, tablet, or PC) connected to the same Wi-Fi network, without needing a physical controller.
* Create a **modern and interactive web interface** (touch buttons, speed sliders, virtual JavaScript joystick) to easily control the robot's movements.

### 📡 Long-Range Connectivity (LoRa)
Thanks to the SPI bus exposed on the rear socket, integrating a **LoRa** radio module (such as the RFM95W or equivalent) is also feasible with very little effort. This technology radically extends the rover's operating range, allowing the transmission of commands and telemetry over very long distances outdoors (rural or dense urban environments), where Wi-Fi or traditional 2.4 GHz links fall short.

*Note: A standardized LoRa add-on is currently under consideration and could be officially available in future evolutions of the uCompute platform.*

### 📊 Real-Time Bidirectional Telemetry
In autonomous mode, the **NRF24L01+** radio modules switch roles. Instead of just receiving driving commands, the wireless link is used to send a constant stream of data (telemetry) back to a ground station (PC, console, or the *uCompute Remote* module):
* Real-time monitoring of voltage and current consumption (via the **INA219** power sensor).
* Transmission of geographic coordinates (GPS), heading (compass), and environmental conditions (temperature, pressure via the **BME280**).
* Remote visualization of thermal data if the **AMG8833** infrared sensor is installed.

*A set of example scripts dedicated to autonomous navigation and the telemetry communication protocol will be progressively added to the `testcode` folder.*

---
# 🎯 The Ideal Project to Get Started

Do you dream of building your own advanced robotics platform, but don't know where to begin? Are you worried about running out of time, lacking programming skills, or lacking electronics expertise? Are you afraid of getting lost in a mess of loose wires that constantly unplug, or leaving your students stuck with overly complex code?

The **uCompute Rover** was designed specifically to put an end to these frustrations.

## 🧠 No Need to Be an Expert to Start
* **Zero complex programming:** Forget austere C++. The robot is powered by the RP2040 microcontroller and programmed in **MicroPython**. It is the simplest, most readable, and fastest programming language to learn today. With just a few lines of code, your robot moves.
* **Zero frustrating blockages:** Thanks to the integrated visual system (*uComputeOS*), if you or one of your students makes a mistake in the code, the screen displays a clear alert instead of completely crashing the board. You understand the error instantly without wasting time.

## 🛠️ Zero Soldering if You Prefer!
* Think you don't have the skills to solder tiny electronic components (SMD)? No problem. While the final board layout is ultra-clean, the project is designed to be **100% reproducible on a simple breadboard** using a standard, low-cost Raspberry Pi Pico or Pico 2. This is the ideal solution to get started quickly at home or to equip an entire classroom on a controlled budget.

## 🚀 Unlimited Evolution, at Your Own Pace
Don't get stuck with a rigid, toy-like robot. Start with a basic remote-controlled chassis driving in a straight line, then upgrade it when you have the time: add Wi-Fi to drive it from your smartphone, connect a long-range radio module, or install a GPS and a distance sensor to make it completely autonomous.

## 🛠️ For Makers: The Ultimate Sandbox
* **Total modularity:** No more rigid robots or unstable bundles of *Dupont* wires. Thanks to its system of interchangeable daughterboards, upgrade your rover however you like: add Wi-Fi (ESP-12F), radio (NRF24L01+), LoRa, GPS, or thermal imaging without ever reworking the main circuit.
* **Open architecture:** Explore standard industrial and communication protocols (I2C, SPI, UART, PWM) on a robust and rewarding platform.

## 🎓 For Schools & Educational Projects: Frictionless Learning
* **Minimal barrier to entry:** Powered by the RP2040 microcontroller and uCompute technologies, the rover allows students to understand concepts and achieve tangible results in just a few lines of code, much faster than in C++.
* **Safety and error tolerance:** Thanks to the built-in diagnostic interface (*uComputeOS*), if a student's code contains an error, the board captures the exception and displays a visual alert screen instead of freezing the robot. Learning happens through smooth experimentation, without frustration.
* **Accessible to all budgets:** While the original SMD assembly requires some expertise, the platform is **100% backward compatible on a breadboard** using a standard Raspberry Pi Pico or Pico 2. You can equip an entire classroom at a lower cost!

*The uCompute Rover provides you with a solid mechanical and electronic foundation. All you have to do is assemble the blocks, at your own pace and according to your current skills.*

---

## 📜 License

The hardware (design files, schematics, layouts) and software of this project are made available under the terms of the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)**.

❌ **Commercial use of this project (reselling bare PCBs, kits, or assembled retroPico boards) is strictly prohibited without prior authorization from the author.**

Check the [LICENSE](LICENSE) file to read the full terms.

---

## ☕ Support the Project

If you appreciate my work and would like to buy me a coffee to support my future soldering and coding projects on a voluntary basis, you can leave me a [**tip on Ko-fi** ](https://ko-fi.com/jpmichon). It is entirely optional and greatly appreciated!
