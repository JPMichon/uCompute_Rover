# Contribuer au projet uCompute Ecosystem 🚀

Un grand merci de l'intérêt que vous portez à l'écosystème **uCompute** ! Que vous travailliez sur la version originale (RP2040), la version simplifiée (**uCompute Junior**) ou la version Linux avancée (**uCompute Rover Pi "Frankenstein"**), votre aide est la bienvenue.

Ce projet est propulsé par les valeurs de l'Open Hardware et partagé sous licence **CC BY-NC-SA 4.0**. L'architecture matérielle (PCBs, routage, isolation de puissance) et la mécanique 3D ont été conçues pour être robustes, standardisées et modulaires. 

**Le socle matériel et la communication bas niveau sont aujourd'hui stables et validés. Si vous avez envie de contribuer, un petit coup de pouce serait apprécié dans l'évolution de la couche applicative.**

---

## 🎯 État actuel

La communication bidirectionnelle par paquets binaires (`struct.pack` / `unpack` au format `"hh"`) est parfaitement fonctionnelle entre la télécommande MicroPython et le Rover Pi. Sur le Raspberry Pi 3B+, la couche d'affichage et de communication s'appuie sur des outils natifs et optimisés sous Python 3 :
* **`pyrf24`** (wrapper C++ ultra-rapide pour le NRF24L01+).
* **`luma.oled`** (gestion de l'affichage SSD1306 via le contexte de dessin `with canvas(oled)`).

Si le cœur vous en dit, voici les axes sur lesquels nous pouvons faire progresser la plateforme :

### 🐍 1. Applications de Vision & Autonomie (Python 3 / Pi 3B+)
* Implémentation de scripts de vision par ordinateur (**OpenCV** / **TensorFlow Lite**) exploitant la PiCam montée sur le mécanisme Pan/Tilt (suivi d'objets, reconnaissance de formes, maintien de trajectoire).
* Algorithmes d'évitement d'obstacles combinant le bouclier de sécurité avant (ultrasons HC-SR04) et le scanner laser mobile (ToF VL53L0X) géré par les servos SG90.

### 📊 2. Télémétrie, Énergie & Capteurs
* Écriture du script de surveillance de la batterie et de gestion de l'énergie en extrayant les données du moniteur de puissance **INA3321** en I2C.
* Exploitation et fusion des données géographiques du **GPS NEO-6M** (via liaison UART) et du cap de la boussole **QMC5883 / GY-271** (I2C) pour créer des scripts de navigation par points de passage (*Waypoints*).

### 🌐 3. Un horizon intéressant : Portage ROS 2 (Robot Operating System)
Puisque le Rover Pi utilise exclusivement des composants standards de l'industrie (moteurs via DRV8833, boussole, laser, GPS), la plateforme matérielle est parfaitement blindée pour accueillir ROS 2 !
* Création de nœuds ROS 2 pour encapsuler le contrôle moteur en PWM logicielle ou matérielle.
* Création de nœuds de conversion des lectures de distance (ToF + ultrasons) en un signal `LaserScan` virtuel pour permettre la cartographie 2D et le SLAM.

---

## 🛠️ Comment contribuer ?

### 1. Signaler un bug ou proposer une idée (Issues)
* Vérifiez que l'idée ou le bug n'a pas déjà été signalé dans la section **Issues**.
* Ouvrez une nouvelle Issue en décrivant le problème, le comportement avant/après attendu et le modèle de carte concerné (Original, Junior, Rover Pi).

### 2. Soumettre des modifications de code (Pull Requests)
1. **Forkez** le dépôt correspondant.
2. Créez une branche descriptive pour votre fonctionnalité (`git checkout -b feature/nom-de-la-fonction`).
3. Écrivez un code propre, documenté et testé sur machine réelle.
4. Poussez votre branche (`git push origin feature/nom-de-la-fonction`).
5. Ouvrez une **Pull Request** vers la branche `main` du projet d'origine en explicitant vos changements.

---

## 📜 Code de conduite & Esprit du projet

Ce projet est né dans un esprit d'entraînement, d'apprentissage et de partage accessible (STEM/Fablabs). Nous demandons à tous les contributeurs de faire preuve de bienveillance, de respect et de pédagogie lors des échanges.

*La quincaillerie et l'électronique de puissance sont prêtes et isolées, à vos claviers pour donner une âme à ce Rover !* 🛠️💻

