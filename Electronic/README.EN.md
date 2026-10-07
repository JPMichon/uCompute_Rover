# ⚡ uCompute Rover Wiring

This directory contains all the necessary information to assemble, wire, and power the robot's electronic components.

## 🗺️ Schematic View of the Onboard Electronics
<p align="center">
<img width="700" height="720" alt="image" src="https://github.com/user-attachments/assets/95619a81-7fdf-4ab7-bc80-40e4ef133049" />
</p>

---

# Assembly Guide

<br>

## ⚙️ Motor Installation

### **You will need:** <br>
• 8 screws (25 mm x 3 mm), <br>
• 4 self-tapping screws (3 mm x 5 mm), <br>
• 4 all-terrain wheels, <br> 
• 4 TT dual-shaft DC motors 3-6 V, 200 RPM ratio, 1:48 reduction, <br>      
<img width="161" height="86" alt="image" src="https://github.com/user-attachments/assets/4b796235-ff34-42b0-b956-b00d7a48ca09" /> <img width="90" height="90" alt="image" src="https://github.com/user-attachments/assets/b3bb7392-6669-4420-9f55-6e464e4ed142" /><br>

**Extend the motor wires as needed**: My prototype version uses **JST-XH 2.54 2-pin** connectors.<br> 
Feel free to use your own setup.

Each motor is connected using a 26 AWG two-conductor wire measuring approximately **30 cm**.

### Steps:

| Insert the wire into the top hole | Insert each wire on each side | Solder the wires to the motor terminals | Secure the motor using screws | Route the other end out the bottom of the electronics plate | Add a sticker on the axles of the 4 motors |
| :---: | :---: | :---: | :---: | :---: | :---: |
| <img width="150" height="195"  alt="image" src="https://github.com/user-attachments/assets/3da047b3-cd6d-452a-b9b7-f2d928ebe226" /> | <img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/35381b1d-b1d5-4d95-a2ac-663825c24f85" /> | <img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/e0115f6c-00bd-4f50-b995-d03e1cee78ea" /> | <img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/bedd2ab9-a23f-4b60-a01e-06ba27a4e731" /> |   <img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/f078b472-b96a-4687-ac73-6bcecad818a1" /> | <img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/9e90e19c-61b7-4f4f-9f23-453a9aff9fd4" /> 


>[!NOTE]
> To **save yourself some time**, make sure to always solder the positive and negative terminals in the same order, as the power module reverses the polarity of the second motor on the same **side**. **This means that if the motors run backward** instead of forward, **you must** swap the connectors between the two motors. <br>
><img width="493" height="365" alt="image" src="https://github.com/user-attachments/assets/a11a52eb-1617-4ab3-91f5-c9088e2ee0c3" /> <br>
> Another element: the **right and left motors operate in pairs**. **That is to say**, the **two** motors on the same side are wired to be synchronous. This reduces **the number of I/Os (IOs)** required to control the motors. The other advantage is that it makes it easier to use **tracks** without having to implement software safeguards, while allowing for more features on the Rover Board. However, **every advantage has its drawbacks**, and this configuration **does not allow** for the use of **Mecanum wheels**. Since the **uCompute Rover is modular** and the schematics are available, **it is relatively simple to DIY your own** motor control module. It is not impossible that in the near future, I might add a specific module to control **Mecanum wheels**.

## ⚙️ Installing the Control Modules

### **You will need:** <br>
• 1 x RP2040 uCompute module,<br>
• 1 x uCompute Rover module,<br>
• 2 x DRV8833 modules,<br>
• 8 self-tapping screws (3 mm x 5 mm),<br>

### Installation:

| Prepare 4 mounting screws | Secure the <br> RP2040 uCompute module | Prepare 4 mounting screws | Secure the <br> uCompute Rover module | Connect the right <br> and left motors | Insert the DRV8833 modules <BR> (Output pins facing down) |
| :---: | :---: | :---: | :---: | :---: | :---: |
|<img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/3ec77fa0-d365-4186-8708-d8237c24c6ca" /> | <img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/79f8e3ea-e109-46d2-86dd-459fcce02352" /> | <img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/3ec77fa0-d365-4186-8708-d8237c24c6ca" /> | <img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/be683505-5f27-4249-aa85-a1ee1a0a3862" /> | <img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/fc1628c4-654d-496d-a528-4a6979441c69" /> | <img width="195" height="130" alt="image" src="https://github.com/user-attachments/assets/51e70eb6-8db5-4d5a-8402-acc7078e0970" />

## ⚙️ Installing the Power Switch
### **You will need:** <br>
• 1 x 24 AWG two-conductor wire, approximately 20 cm,<br>
• 1 x SPST rocker switch, model: **KCD11 (10X15mm)**,<br>

### Installation:

| Solder the wires to the switch terminals | Insert the switch into the square hole on the control panel |
| :---: | :---: |
|<img width="500" height="150" alt="image" src="https://github.com/user-attachments/assets/733b0b0f-aa1c-450f-910f-20608ac14508" />|<img width="350" height="340" alt="image" src="https://github.com/user-attachments/assets/3aaee718-4ee8-49d7-90cf-3798e28d6079" />

## :scissors: Mounting the Power Supply
This section is simple, yet effective…<BR>
The easiest way to hold the various components in place is by using Velcro strips.<br>
_If it's good enough for NASA, it's good enough for the Rover!_

### Steps:

| Stick a Velcro strip <br> on the top shelf | Stick Velcro strips <br> under the battery holder | Stick a Velcro strip <br> under the regulator | Test the installation |
| :---: | :---: | :---: | :---: |
|<img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/c107f1a8-6312-4248-9366-c316a7f7d4ba" /> | <img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/57736bb1-8eb8-4f72-b4a3-aec0f6b3897c" />|<img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/de930fa3-1bfb-46a3-a759-b9004eb18326" />|<img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/f7e2de8b-040c-4291-987d-cc17d87b8475" />|

## ⚙️ Preparing and Installing the NeoPixel Strip

> [!NOTE]
> Only available for the `frontal_sensor_v3.stl` which natively integrates the **NeoPixel** strip.

### **You will need:** <br>
• 3 x wires with a female **DuPont** connector on one end, approximately **25 cm** long,<br>
• 1 x **NeoPixel** strip with 8 addressable **WS2812B** (5050) LEDs,<br>
• 2 self-tapping screws (3 mm x 5 mm),<br>

### Steps:

| View of the NeoPixel strip | Solder the wires <br> to the side labeled DI | Result | Prepare 2 mounting screws | Secure the NeoPixel module <br> underneath the sonar |
| :---: | :---: | :---: | :---: | :---: |
|<img width="174" height="140" alt="image" src="https://github.com/user-attachments/assets/cdb4634b-3352-4bdd-9df5-cf7747b15e1e" /> | <img width="140" height="140" alt="image" src="https://github.com/user-attachments/assets/32493c68-3fc3-417f-8772-2d89dd0ca7c9" /> | <img width="174" height="140" alt="image" src="https://github.com/user-attachments/assets/1256647f-7e10-459c-887c-93a61bae876d" /> | <img width="140" height="140" alt="image" src="https://github.com/user-attachments/assets/5aad3843-ac5f-4070-b4c9-71dc1bb1a9b1" /> | <img width="174" height="140" alt="image" src="https://github.com/user-attachments/assets/56701e16-c661-4b51-9658-7692be9a8ef8" />|

## :scissors: Installing the HC-SR04 Sonar
For this part, you will need **hot glue…** <br>
Hooray for crafting! <br>

### **You will need:** <br>
• 4 x wires with female-to-female **DuPont** connectors, approximately **25 cm** long,<br>
• 1 x HC-SR04 Sonar Module<br>

### Steps:

| Installing the **DuPont connectors** <br> on the sonar | Installing the sensor in its housing <br> use a little hot glue to secure it |
| :---: | :---: |
|<img width="140" height="140" alt="image" src="https://github.com/user-attachments/assets/ae667222-eca8-4012-8073-a54363463a40" />|<img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/83c1719c-cbda-49d0-8bfa-db9b828553cb" />|

> [!NOTE]
> Hot glue has a melting point around 190°C (374°F), which is very close to 3D printing temperatures. <br>
> **Use hot glue sparingly** to avoid warping your printed parts.

## ⚙️ Installing the Servo Motor
### **You will need:** <br>
• 1 x **SG90 Mini Gear Micro 9g** Servo or equivalent,<br>
• 2 self-tapping screws (2 mm x 5 mm) (usually included with the Servo).<br>

### Steps:

| Servo Image | Prepare 2 Screws | Secure the Servo <br> to the Mount |
| :---: | :---: | :---: |
|<img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/668c6d31-3bc1-4559-942a-de1110a8d83f" /> | <img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/c54f9c5b-419e-45fa-821b-f27f2311db96" /> | <img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/6fb1a63c-3361-4c0a-aba4-560b6990f80c" />|

## ⚙️ Preparing the LM2596
### **You will need:** <br>
• 1 x 24 AWG two-conductor wire, approximately 10 cm,<br>
• 1 x 24 AWG two-conductor wire, approximately 15 cm, with a **JST XH2.54 2P** connector on one end,<br>
• 1 x **LM2596 DC-DC buck converter** module,<br>

### Steps:

| Solder the wires<br> + Red, - Black | Close-up of the <br> JST XH2.54 2P connector | 
| :---: | :---: |
|<img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/db85b3f0-d31a-4ef3-8d37-3c7a2af4c18b" />|<img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/1485ad30-8d50-4e6b-a011-543ba3d12896" />|

> [!WARNING]
> ### ⚡ WARNING: Mandatory Tuning of the LM2596 Regulator
> The Rover module strictly requires a **5V** power supply voltage. Since the LM2596 DC-DC converter is an **adjustable** regulator, it is **crucial to adjust its output voltage to 5V using a multimeter BEFORE connecting it** to the Rover's electronic boards.
> 
> Connecting the regulator without prior adjustment or with a voltage that is too high will lead to the **immediate destruction** of the RP2040 microcontroller, the LCD screen, and all of your sensors.

### Adjusting the Regulator

**Using a multimeter and a small flathead screwdriver, adjust the voltage by turning the potentiometer screw (indicated in the photo below).**
> 🔄 **Potentiometer Adjustment Direction:**
> * **To DECREASE the voltage:** Turn the screw **counterclockwise**.
> * **To INCREASE the voltage:** Turn the screw **clockwise**.
> 
> *Note: These multi-turn potentiometers often have a wide initial adjustment range. It is completely normal to have to complete several full turns (sometimes more than 10 to 15 turns) before seeing the voltage begin to change on your multimeter. Proceed gently with small adjustments once you are close to 5V.*

<p align="center">
<img width="569" height="371" alt="image" src="https://github.com/user-attachments/assets/10494b81-9cd7-41e0-a7ae-1cd8d28e3c3e" />
</p>

## 🔋 Power Supply Diagram

The Rover is powered by a 6-AA battery pack (or equivalent). The voltage is stepped down to **5V (2A min)** via the LM2596 module to power the main board, the motors, and the servo motor.

<p align="center">
<img width="500" height="350" alt="image" src="https://github.com/user-attachments/assets/0465d19e-39bf-4fe8-96a4-ff1c747c2283" />
</p>

---

## Final Connections
The power supply, the HC-SR04 Sonar, and the Servo all connect to this specific location on the control board.<br>
The **NeoPixels** connect directly to the uCompute board.<br>

The motors were already connected in the previous steps. If they aren't, you can connect them now.<br> 

### Steps:

| Close-up of the connectors | Once connected | Connect the NeoPixel <br> directly to the uCompute | Connect the INA219 <br> to the back of the uCompute |
| :---: | :---: | :---: | :---: |
|<img width="260" height="260" alt="image" src="https://github.com/user-attachments/assets/d5e51127-a20c-459e-b88b-437bd7cad6f1" /> | <img width="210" height="265" alt="image" src="https://github.com/user-attachments/assets/8a936ef8-850f-44cf-b5c1-ff70a51956a8" /> |<img width="220" height="270" alt="image" src="https://github.com/user-attachments/assets/c901930c-2662-46a1-947c-ffec8f33ab00" /> |<img width="220" height="270" alt="image" src="https://github.com/user-attachments/assets/addd0c1f-4bb3-4e6b-9fe0-355f3d8e9717" />|


## Cable Management (Optional):

### **You will need:** <br>
• A **sufficient quantity** of **10 cm cable ties (zip ties / tie-wraps)**.<br>
• A pair of **wire cutters** to trim off the excess.

Although optional, this part is nevertheless important if you **want** a reliable project over time. The horizontal pieces were designed with notches to make cable management easier, allowing the use of **10 cm cable ties (zip ties)** to secure the **cables** firmly. Feel free to use them as you see fit.

### Location of the notches<br>
<img width="170" height="215" alt="image" src="https://github.com/user-attachments/assets/6c4ad347-de4c-4709-ba90-b360f6cfbd97" />


## GPS Connection
**Coming soon**

## Telecommunication Module Connection
**Coming soon**

---

# EXTRA

## More than one I2C sensor? No problem!
There is a good chance you will want to include more than one I2C sensor in your project. The solution is quite simple and can be achieved by connecting them in parallel using a quick DIY trick.

### DIY Details

| Top View | Soldering Details | 
| :---: | :---: |
|<img width="490" height="482" alt="image" src="https://github.com/user-attachments/assets/60e30bce-4825-49b2-8960-8a73b0164005" /> | <img width="476" height="485" alt="image" src="https://github.com/user-attachments/assets/09589e99-1ec8-4e45-9f84-ce6641fc09cc" /> |

> [!NOTE]
> 💡 **Important note regarding the I2C bus**
> * The I2C bus requires two pull-up resistors—one on SDA and one on SCL—connected to VCC to function properly.
> * Most ready-to-use sensor modules (breakout boards) already include these built-in resistors.
> * Connecting too many modules in parallel drops the total pull-up resistance (Ohm's law / resistors in parallel). If you connect more than 3 or 4 sensors, the signal quality may degrade.
> 
> ⚠️ **In case of issues:** If you experience communication errors, you will need to remove (unsolder) the pull-up resistors from some of the modules to keep only a single pair on the entire bus.
