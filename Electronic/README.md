# ⚡ Électronique et Câblage du uCompute Rover

Ce répertoire regroupe toutes les informations nécessaires pour assembler, câbler et alimenter les composants électroniques du robot.

## 🗺️ Vue schématisée de l'électronique embarquée

*(Insérez ici l'image de votre schéma global)*

## 📍 Tableau de connexion des composants

| Composant | Broche Roverboard / uCompute | Rôle / Fonction |
| :--- | :---: | :--- |
| **Moteurs Gauches** | OUT1 / OUT2 (DRV8833 A) | Propulsion côté gauche |
| **Moteurs Droits** | OUT3 / OUT4 (DRV8833 B) | Propulsion côté droit |
| **Servomoteur** | GP23 (PWM) | Orientation du capteur avant |
| **HC-SR04 (Trig)** | GP... | Déclenchement de l'ultrason |
| **HC-SR04 (Echo)** | GP... | Réception de l'écho |

## 🔋 Alimentation et Puissance
Le Rover est propulsé par un boîtier de 6 piles AA (ou équivalent). La tension est abaissée à **5V (2A min)** via le module LM2596 pour alimenter la carte principale, les moteurs et le servomoteur.
