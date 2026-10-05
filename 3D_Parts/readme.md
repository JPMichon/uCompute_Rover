# Impression du Rover


<img width="751" height="715" alt="image" src="https://github.com/user-attachments/assets/4a28565e-bafb-4b29-a7ef-f42afe067af9" />


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

A noter sur la photo, les **jambes** (En rouge) sont déjà assemblées aux pièces latérales (**côtés**) en blanc. Elles sont simplement insérées en presse-fit. Vous pouvez appliquer une goutte de colle cyanoacrylate afin de sécuriser les pièces.

---

# 🛠️ Guide d'Assemblage – uCompute Rover
Ce guide détaille les étapes nécessaires pour assembler la structure mécanique et les supports électroniques du Rover.

## 📋 Étape 1 : Inventaire et Impression des Pièces
Avant de commencer, assurez-vous d'avoir imprimé l'ensemble des composants nécessaires en quantité suffisante :

### Pièces structurales et de liaison<br>
• **Les côtés (2x)** : 1x `Rover_Side_L_fixed.stl` (Gauche) et 1x `Rover_Side_R_fixed.stl` (Droit).<br>
• **Les Jambes (2x)** : Imprimer deux fois le fichier <br>
• **Tablette (2x)** : Imprimer deux fois le fichier `Tablette.stl`. Servent de support structurel et de bac pour les batteries.

### Pièces structurales transversales<br>
• **Tablette du haut (1x)** : `Servo_plate_v2.stl` (Support pour servo 9g et antennes).<br>
• **Détection de collision (1x)** : `frontal_sensor_v3.stl`.<br>
• **Le tableau électronique (1x)** : `Electronic_plate_v2_uCRP2040.stl` (Pour la carte RP2040 Ucompute V1.3).

>[!NOTE]
> Une version pour la carte RP2350 Ucompute2 V1.1 est en conception <br>

## 🔧 Étape 2 : Pré-assemblage des Train de Roulement (Jambes et Côtés)<br>
1. **Insertion à blanc** : Insérez les Jambes (en rouge sur les photos de référence) dans les Pièces latérales (côtés droit et gauche).<br>
2. **Fixation** : Les pièces sont conçues pour s'ajuster en "presse-fit" (serrage mécanique).<br>

## 📐 Étape 3 : Assemblage du Châssis Central (Les Tablettes)

1. **Positionnement des tablettes basses :** Prenez les deux pièces *Tablette* imprimées. Elles viennent relier les blocs latéraux gauche et droit afin de fermer le châssis en largeur.
2. **Sécurisation :** Fixez-les solidement ; ces tablettes vont rigidifier l'ensemble du Rover et serviront plus tard de logement pour vos batteries et composants lourds.
3. **Ajout de la Tablette du haut :** Installez la plaque `Servo_plate_v2`. Intégrez-y le servomoteur 9g et fixez le support pour les antennes avant de refermer complètement la partie supérieure.

| Tablettes | Tablettes | Tablette haut | Tablette haut |  Vue haut | Support avant | Plaque electronique |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| <img width="94" height="124" alt="image" src="https://github.com/user-attachments/assets/14978c74-fd83-4283-9904-132776d71155" /> | <img width="92" height="122" alt="image" src="https://github.com/user-attachments/assets/c6409e4a-77cb-4d2b-a6ee-3aed988a7bbd" /> | <img width="94" height="124" alt="image" src="https://github.com/user-attachments/assets/f8480e1c-d032-4de0-8248-6e1a538836c6" /> |<img width="94" height="124" alt="image" src="https://github.com/user-attachments/assets/e655bf08-c3b3-4ac3-9c0f-88ce32c5b03c" /> |  <img width="94" height="124" alt="image" src="https://github.com/user-attachments/assets/2bf7494d-16c2-489a-8ea8-a37977a90ced" /> | <img width="95" height="124" alt="image" src="https://github.com/user-attachments/assets/e0b9fc12-6d61-4bd9-85e4-0d05c2873b69" /> | <img width="124" height="94" alt="image" src="https://github.com/user-attachments/assets/fc621546-d3f9-459b-aa7c-d6d34f745af3" />
<br>

### Le uCompute Rover assemblé :
<br>
<p align="center">
<img width="371" height="417" alt="image" src="https://github.com/user-attachments/assets/add39a4e-4057-4132-92d3-497a460eee17" /><img width="371" height="417" alt="image" src="https://github.com/user-attachments/assets/042d32d9-e3fa-45ca-bb6a-84f7ea5539e0" />
</p>


## 📡 Étape 4 : Intégration des Capteurs et de l'Électronique<br>
1. **Module de détection frontal** : Assemblez le module de détection de collision à l'avant du robot.<br>
2. **Plaque électronique** : Installez le tableau électronique (Electronic_plate) conçu pour votre carte RP2040 Ucompute V1.3.<br>
3. **Fixation**:Fixez la carte sur son support avant de connecter les câbles des moteurs, du servo et des capteurs frontaux. Utiliser 4 vis perçantes (_ou faire des petits trous_) de (8 mm x 3mm) 2 par côté.<br>
4. **Sécurisation du Ucompute et du Rover module** : Utiliser des vis de (8 mm x 3mm).

## 🧐 Étape 5 : Vérification Finale<br>
• **Vérification de l'équerrage** : Posez le Rover sur une surface plane pour vérifier l'alignement des jambes et de l'empattement (comme illustré sur la vue 3D de l'assemblage final).<br>

## 🔒 Étape 6 : Sécurisation de la structure (_Optionnelle mais recommandée_) <br>
•  Pour garantir une robustesse structurelle et éviter que les vibrations ne séparent les pièces, appliquez une goutte de colle cyanoacrylate (_Crazy Glue_) au niveau des mortaises de liaison entre les pièces.

## 🔧 Étape 7 : fixation des moteurs et des roues<br>
• **visser les Moteurs TT CC 3-6 V** : aux 4 Jambes avec 2 vis de (25 mm x 3 mm) et 1 vis percante de (5 mm  x 3mm) par jambes.
   <img width="161" height="86" alt="image" src="https://github.com/user-attachments/assets/4b796235-ff34-42b0-b956-b00d7a48ca09" />
   <img width="90" height="90" alt="image" src="https://github.com/user-attachments/assets/b3bb7392-6669-4420-9f55-6e464e4ed142" /><br>
• **Alonger les fils des moteurs aux besoins** :  Ma version prototype utilise des connecteurs JST-XH 2.54 2-pin, libre à vous d'utiliser votre propre recette.




