# ⚡ Électronique et Câblage du uCompute Rover

Ce répertoire regroupe toutes les informations nécessaires pour assembler, câbler et alimenter les composants électroniques du robot.

## 🗺️ Vue schématisée de l'électronique embarquée
<p align="center">
<img width="860" height="860" alt="image" src="https://github.com/user-attachments/assets/88a6deb9-74b1-4e49-9caa-6c8eda09083e" />
</p>


## 📍 Tableau de connexion des composants

| Composant | Broche Roverboard / uCompute | Rôle / Fonction |
| :--- | :---: | :--- |
| **Moteurs Gauches** | OUT1 / OUT2 (DRV8833 A) | Propulsion côté gauche |
| **Moteurs Droits** | OUT3 / OUT4 (DRV8833 B) | Propulsion côté droit |
| **Servomoteur** | GP23 (PWM) | Orientation du capteur avant |
| **HC-SR04 (Trig)** | GP... | Déclenchement de l'ultrason |
| **HC-SR04 (Echo)** | GP... | Réception de l'écho |

## ⚙️ Installation des moteurs

 **Vous aurez besoins de:**
• 8 vis de (25 mm x 3 mm),<br>
• 4 vis perçante de (5 mm  x 3mm),<br>
• 4 roues tout terrain, <br>       <img width="90" height="90" alt="image" src="https://github.com/user-attachments/assets/b3bb7392-6669-4420-9f55-6e464e4ed142" /><br>
• 4 moteurs TT double CC 3-6 V Rapport 200 tr/min Moteur d'arbre 1:48, <br>      <img width="161" height="86" alt="image" src="https://github.com/user-attachments/assets/4b796235-ff34-42b0-b956-b00d7a48ca09" /><br> 

**Alonger les fils des moteurs aux besoins** :  Ma version prototype utilise des connecteurs JST-XH 2.54 2-pin, libre à vous d'utiliser votre propre recette.

Chaque moteur est raccordé par un fil à deux conducteurs de calibre 26 AWG d'environ **30 cm**.

| Insérer le fil dans le petit trou | Insérer chaque fil de chaque côté | Souder les fils aux bornes du moteur | Sécuriser le moteur à l'aide de vis | Sortir l'autre extrémité dans le bas de la plaque électronique |
| :---: | :---: | :---: | :---: | :---: |
| <img width="150" height="195"  alt="image" src="https://github.com/user-attachments/assets/3da047b3-cd6d-452a-b9b7-f2d928ebe226" /> | <img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/35381b1d-b1d5-4d95-a2ac-663825c24f85" /> | <img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/e0115f6c-00bd-4f50-b995-d03e1cee78ea" /> | <img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/bedd2ab9-a23f-4b60-a01e-06ba27a4e731" /> |   <img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/f078b472-b96a-4687-ac73-6bcecad818a1" />



## 🔋 Alimentation et Puissance
Le Rover est propulsé par un boîtier de 6 piles AA (ou équivalent). La tension est abaissée à **5V (2A min)** via le module LM2596 pour alimenter la carte principale, les moteurs et le servomoteur.
