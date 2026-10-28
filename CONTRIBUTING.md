# Contributing to uCompute Ecosystem / Contribuer au projet 🚀

---

### 🌍 Note from the author / Note de l'auteur
> **FR:** Bonjour ! Je suis francophone et mon anglais n'est pas parfait. Merci d'avance pour votre indulgence. Vous pouvez ouvrir des discussions, des tickets ou des Pull Requests en français ou en anglais !
>
> **EN:** Hello! I am a native French speaker and my English is not perfect. Feel free to open discussions, issues, or pull requests in either French or English!

---
## ENGLISH

Thank you for your interest in the **uCompute Ecosystem** under the **CC BY-NC-SA 4.0** license. With a stable hardware foundation, contributions are welcome for the application layer (computer vision, telemetry, and ROS 2 porting).

For full details regarding the current status, contribution areas, submission guidelines, and code of conduct, please refer to the complete markdown text in the source documentation.

*The hardware and power electronics are ready and isolated; grab your keyboards to give this Rover a soul!* 🛠️💻

## 🎯 Current Status

Bidirectional communication using binary packets (`struct.pack` / `unpack` with `"hh"` format) is fully functional between the MicroPython remote control and the Rover Pi. On the Raspberry Pi 3B+, the display and communication layers rely on native, highly optimized Python 3 tools:
* **`pyrf24`** (an ultra-fast C++ wrapper for the NRF24L01+).
* **`luma.oled`** (SSD1306 display management using the `with canvas(oled)` drawing context).

If you feel like contributing, here are the main areas where we can advance the platform:

### 🐍 1. Vision Applications & Autonomy (Python 3 / Pi 3B+)
* Implementing computer vision scripts (**OpenCV** / **TensorFlow Lite**) leveraging the PiCam mounted on the Pan/Tilt mechanism (object tracking, shape recognition, lane keeping/trajectory hold).
* Obstacle avoidance algorithms combining the front safety shield (HC-SR04 ultrasonic sensor) and the mobile laser scanner (ToF VL53L0X) driven by the SG90 servos.

### 📊 2. Telemetry, Power Management & Sensors
* Writing the battery monitoring and power management script by extracting data from the **INA3321** power monitor via I2C.
* Exploiting and fusing geographical data from the **NEO-6M GPS** (via UART link) and heading from the **QMC5883 / GY-271** compass (I2C) to create waypoint navigation scripts.

### 🌐 3. An Exciting Horizon: ROS 2 Porting (Robot Operating System)
Since the Rover Pi exclusively uses industry-standard components (motors via DRV8833, compass, laser, GPS), the hardware platform is perfectly ruggedized to welcome ROS 2!
* Creating ROS 2 nodes to encapsulate motor control using software or hardware PWM.
* Creating conversion nodes to transform distance readings (ToF + ultrasonic) into a virtual `LaserScan` signal to enable 2D mapping and SLAM.

---

## 🛠️ How to Contribute?

### 1. Report a bug or suggest an idea (Issues)
* Check that the idea or bug hasn't already been reported in the **Issues** section.
* Open a new Issue describing the problem, the expected before/after behavior, and the specific board model involved (Original, Junior, Rover Pi).

### 2. Submit code changes (Pull Requests)
1. **Fork** the corresponding repository.
2. Create a descriptive branch for your feature (`git checkout -b feature/feature-name`).
3. Write clean, documented code tested on real hardware.
4. Push your branch (`git push origin feature/feature-name`).
5. Open a **Pull Request** to the `main` branch of the original project, clearly explaining your changes.

---

## FRANCAIS

Un grand merci de l'intérêt que vous portez à l'écosystème **uCompute** ! Que vous travailliez sur la version originale (RP2040), la version simplifiée (**uCompute Junior**) ou la version Linux avancée (**uCompute Rover Pi "Frankenstein"**), votre aide est la bienvenue.

Ce projet est propulsé par les valeurs de l'Open Hardware et partagé sous licence **CC BY-NC-SA 4.0**. L'architecture matérielle (PCBs, routage, isolation de puissance) et la mécanique 3D ont été conçues pour être robustes, standardisées et modulaires. 

**Le socle matériel et la communication bas niveau sont aujourd'hui stables et validés. Si vous avez envie de contribuer, un petit coup de pouce serait apprécié dans l'évolution de la couche applicative.* 🛠️💻

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

