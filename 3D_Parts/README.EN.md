**# Impression du Rover

![3D View](https://github.com/JPMichon/uCompute_Rover/blob/main/Rover_3D.png)

## Voici un tableau récapitulatif des pièces à imprimer.

| Catégorie | Nom de la pièce | Fichier STL recommandé | Quantité | Taux de remplissage (Infill) suggéré | Notes et spécificités |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **Structure Principale** | **Les Côtés** | `Rover_Side_L_fixed.stl`<br>`Rover_Side_R_fixed.stl` | **2** <br>*(1 gauche / 1 droit)* | **30 %** | Côtés latéraux du Rover. |
| **Structure Principale** | **Les Jambes** | `Rover_Legs_V4.stl` | **2** | **30 %** | La version **V4** permet d'utiliser des vis de **25 mm x 3 mm**. Pièce mécanique sollicitée. |
| **Structure Principale** | **Détection de Collision** | `frontal_sensor_v3.stl` | **1** | **30 %** | La version **v3** permet d'accueillir un module de **8 Neopixels** en plus du capteur **HC-SR04**. |
| **Structure Principale** | **Tablette** | `Tablette.stl` | **2** | **30 %** | Support structurel de base et logement pour les batteries. |
| **Structure Principale** | **Tablette du Haut** | `Servo_plate_v2.stl` | **1** | **30 %** | Reçoit un **servo-moteur 9g** et sert de support pour les antennes. |
| **Électronique & Capteurs**| **Tableau Électronique** | `Electronic_plate_v2_uCRP2040.stl` | **1** | **30 %** | Conçu pour la carte **RP2040 Ucompute V1.3**. |

Il n'y a pas de recommandation spécifique sur le type de plastique, mon POC a été imprimé en PLA. Profitez-en pour utiliser vos restants de rouleau, **soyez créatifs !**

## Vue des pièces imprimés

<img width="824" height="688" alt="image" src="https://github.com/user-attachments/assets/f10d11fc-7654-4ade-9636-a0aaced1e533" />

A noter sur la photo, les **jambes** (En rouge) sont déjà assemblées aux pièces latérales (**côtés**) en blanc. Elles sont simplement insérées en presse-fit. 

> [!NOTE]
> Sur l'image, la version 2 du support du **HC-SR04** `frontal_sensor_v2.stl` été imprimé.<br> Je vous suggère d'imprimer la version 3 du support `frontal_sensor_v3.stl`.

---

# 🛠️ Assembly Guide – uCompute Rover
This guide details the steps required to assemble the mechanical structure and electronics supports of the Rover.

## 📋 Step 1: Inventory and Parts Printing
Before starting, ensure you have printed all the necessary components in sufficient quantities:

### Structural and Connecting Parts<br>
• **Sides (2x)**: 1x `Rover_Side_L_fixed.stl` (Left) and 1x `Rover_Side_R_fixed.stl` (Right).<br>
• **Legs (2x)**: Print the file twice.<br>
• **Shelf (2x)**: Print the `Tablette.stl` file twice. These serve as structural supports and battery bays.

### Transverse Structural Parts<br>
• **Top Shelf (1x)**: `Servo_plate_v2.stl` (Support for 9g servo and antennas).<br>
• **Collision Detection (1x)**: `frontal_sensor_v3.stl`.<br>
• **Electronics Board (1x)**: `Electronic_plate_v2_uCRP2040.stl` (For the RP2040 Ucompute V1.3 board).

>[!NOTE]
> A version for the RP2350 Ucompute2 V1.1 board is currently under design.<br>

## 🔧 Step 2: Pre-assembling the Drivetrain (Legs and Sides)<br>
1. **Dry fit**: Insert the Legs (in red in the reference photos) into the Lateral Pieces (right and left sides).<br>
2. **Securing**: The parts are designed for a mechanical "press-fit" alignment.<br>

## 📐 Step 3: Central Chassis Assembly (The Shelves)

1. **Positioning the low shelves:** Take the two printed *Shelf* parts. They connect the left and right side blocks to enclose the chassis widthwise.
2. **Securing:** Fasten them securely; these shelves will stiffen the entire Rover assembly and will later serve as the housing for your batteries and heavy components.
3. **Adding the Top Shelf:** Install the `Servo_plate_v2` plate. Integrate the 9g servo motor and secure the antenna support before fully closing the upper section.

| Shelves | Shelves | Top Shelf | Top Shelf | Top View | Front Support | Electronics Plate |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| <img width="94" height="124" alt="image" src="https://github.com/user-attachments/assets/14978c74-fd83-4283-9904-132776d71155" /> | <img width="92" height="122" alt="image" src="https://github.com/user-attachments/assets/c6409e4a-77cb-4d2b-a6ee-3aed988a7bbd" /> | <img width="94" height="124" alt="image" src="https://github.com/user-attachments/assets/f8480e1c-d032-4de0-8248-6e1a538836c6" /> |<img width="94" height="124" alt="image" src="https://github.com/user-attachments/assets/e655bf08-c3b3-4ac3-9c0f-88ce32c5b03c" /> |  <img width="94" height="124" alt="image" src="https://github.com/user-attachments/assets/2bf7494d-16c2-489a-8ea8-a37977a90ced" /> | <img width="95" height="124" alt="image" src="https://github.com/user-attachments/assets/e0b9fc12-6d61-4bd9-85e4-0d05c2873b69" /> | <img width="124" height="94" alt="image" src="https://github.com/user-attachments/assets/fc621546-d3f9-459b-aa7c-d6d34f745af3" />
<br>

### The assembled uCompute Rover:
<br>
<p align="center">
<img width="371" height="417" alt="image" src="https://github.com/user-attachments/assets/add39a4e-4057-4132-92d3-497a460eee17" /><img width="371" height="417" alt="image" src="https://github.com/user-attachments/assets/042d32d9-e3fa-45ca-bb6a-84f7ea5539e0" />
</p>


## 📡 Step 4: Sensor and Electronics Integration<br>
1. **Front detection module**: Assemble the collision detection module to the front of the robot.<br>
2. **Electronics board**: Install the electronics plate designed for your RP2040 Ucompute V1.3 board.<br>
3. **Fastening**: Secure the board to its support before connecting the cables for the motors, servo, and front sensors. Use 4 self-tapping screws (*or drill small pilot holes*) of (8 mm x 3 mm), 2 on each side.<br>
4. **Securing the Ucompute and Rover module**: Use (8 mm x 3 mm) screws.

## 🧐 Step 5: Final Inspection<br>
• **Alignment check**: Place the Rover on a flat surface to verify the alignment of the legs and the wheelbase (as shown in the 3D view of the final assembly).<br>

## 🔒 Step 6: Securing the Structure (*Optional but recommended*)<br>
• To ensure structural robustness and prevent vibrations from separating the parts, apply a drop of cyanoacrylate glue (*Crazy Glue*) to the interlocking joints between the pieces.

## The next assembly steps are in the electronics section!
**[ Go to Electronics Section ](https://github.com/JPMichon/uCompute_Rover/blob/main/Electronic/README.EN.md)**
