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

## 📍 Installation des moteurs

Chaque moteur est raccordé par un fil electrique a deux conducteur d'environ **30 cm**.

| Inserer le fils dans le trous | Insérer chaque fils de chaque coté | Souder les fils au borne du moteur | Sécurisé le moteur a l'aide de vis |  Sortir l'autre extremité dans le bas de la plaque |
| :---: | :---: | :---: | :---: | :---: |
| <img width="93" height="123" alt="image" src="https://github.com/user-attachments/assets/3da047b3-cd6d-452a-b9b7-f2d928ebe226" /> | <img width="95" height="122" alt="image" src="https://github.com/user-attachments/assets/35381b1d-b1d5-4d95-a2ac-663825c24f85" /> | <img width="93" height="122" alt="image" src="https://github.com/user-attachments/assets/e0115f6c-00bd-4f50-b995-d03e1cee78ea" /> | <img width="92" height="120" alt="image" src="https://github.com/user-attachments/assets/bedd2ab9-a23f-4b60-a01e-06ba27a4e731" /> |  <img width="94" height="124" alt="image" src="https://github.com/user-attachments/assets/2bf7494d-16c2-489a-8ea8-a37977a90ced" /> | <img width="94" height="122" alt="image" src="https://github.com/user-attachments/assets/f078b472-b96a-4687-ac73-6bcecad818a1" />



## 🔋 Alimentation et Puissance
Le Rover est propulsé par un boîtier de 6 piles AA (ou équivalent). La tension est abaissée à **5V (2A min)** via le module LM2596 pour alimenter la carte principale, les moteurs et le servomoteur.
