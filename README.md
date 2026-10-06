# 🤖 uCompute Rover

*4WD Rover conçu pour utiliser les modules uCompute 1 ou 2 comme fondation.*

![vue 3D](https://github.com/JPMichon/uCompute_Rover/blob/main/Rover_3D.png)

## 🛠️ Matériel requis
* 4 x Motoréducteurs CC — "TT Motor" — 200 RPM (3 à 6 VCC)
* 2 x DRV8833 — Contrôleurs de moteur double pont en H (1,5 A, 3 à 10 V)
* 1 x Module uCompute RP2040 ver 1.3 (Rover)
* 1 x uCompute-Rover ver 1.0
* 1 x Convertisseur abaisseur de tension DC-DC LM2596 (3 A ou équivalent)
* 1 x Boîtier pour 6 piles AA (ou équivalent)

## ⚙️ Options et extensions
* 1 x Micro-servomoteur SG90
* 1 x Capteur à ultrasons HC-SR04 / HCSR04
* 1 x Schéma de câblage du rover
* 1 x Interrupteur à bascule encastrable (*Snap-in*) 10x15 mm (ON-OFF)
* 2 x Modules radio nRF24L01+
* 1 x Module uCompute RP2040 ver 1.3 (Télécommande)
* 1 x Contrôleur à distance uCompute (*Remote controller*)
* 1 x Capteur de puissance et moniteur de tension/courant I2C INA219
* 1 x Module GPS GY-NEO-6M avec antenne active en céramique
* 1 x Capteur de distance laser ToF (*Time-of-Flight*) GY-530 VL53L0X
* 1 x Boussole magnétique à trois axes GY-271 QMC5883L (3V-5V)
* 1 x Caméra thermique infrarouge AMG8833 (Matrice de capteurs 8x8)
* 1 x Module haute précision de température, humidité et pression d'air I2C AHT20+BMP280
* 1 x Module d'analyse de la qualité de l'air (CO2, eCO2, TVOC) ENS160+AHT21
* *Tout autre module optionnel selon vos préférences.*

---

## ⚡Vue schématisé de l'électronique embarqué
<img width="353" height="380" alt="image" src="https://github.com/user-attachments/assets/00ff8261-1ec5-4b57-87cb-6808611c9471" />


---

# 🔌 Architecture Électronique & Modularité

Le projet **uCompute Rover** repose sur une architecture matérielle entièrement modulaire. Ce dépôt se concentre spécifiquement sur le châssis, l'assemblage mécanique et la carte d'interface du rover (*Roverboard*). 

Le "cerveau" et les différents modules de communication requis proviennent de l'écosystème global **RP2040 uCompute**.

---

## 🔗 Dépôt Parent & Documentation Électronique

Pour fabriquer, programmer ou comprendre le fonctionnement détaillé de la carte maîtresse et de ses modules, veuillez vous référer au dépôt principal :

👉 **[GitHub - RP2040 uCompute](https://github.com/JPMichon/RP2040_uCompute)**

Vous y trouverez :
* 📂 Les fichiers de conception matérielle (**Gerber**, schémas de circuits et listes de composants BOM).
* 📂 Les modules.
* 📍 La cartographie complète des ports et les spécifications techniques de la plateforme.

---

### 🧠 Le Cœur du Système : uCompute
L'intelligence embarquée du robot utilise la plateforme de développement autonome **uCompute** (basée sur le microcontrôleur Raspberry Pi RP2040). C'est elle qui gère l'exécution des scripts de pilotage (MicroPython), l'interface graphique de diagnostic et la centralisation des données des capteurs.<br>
<img width="775" height="350" alt="image" src="https://github.com/user-attachments/assets/4a8f9f4d-8950-45fe-b8cd-cc78aa2371bc" />

---

### 📻 Modules d'Extension (Add-ons)
Pour assurer la liaison sans fil et la télémétrie bidirectionnelle avec la télécommande, le rover exploite les modules d'extension interchangeables du projet principal (notamment le module radio **NRF24L01+**).

👉 **[RP2040_uCompute Modules](https://github.com/JPMichon/RP2040_uCompute/tree/main/Modules)**

| Emplacement | Module | Description & Fonctionnalités | Rendu Visuel |
| :--- | :--- | :--- | :--- |
| **Socket Arrière** (Communication) | **Module Wi-Fi** (ESP-12F) | Carte d'adaptation avec ESP8266 pour une connectivité Wi-Fi. | <img width="100" height="133" alt="image" src="https://github.com/user-attachments/assets/f0c80621-1b07-46e6-844b-4594e3d338f9" />  |
| **Socket Arrière** (Communication) | **Module Radio** (NRF24L01) | Carte d'adaptateur pour liaisons radio 2,4 GHz. | <img width="112" height="140" alt="image" src="https://github.com/user-attachments/assets/a6a0a83b-80ed-4dbc-bc28-06579f64b54c" /> |
| **Pins Header** <br> (Connecteur IOs) | **µCompute Remote** <br> (REV 1.0) | Module de commande analogue avec boutons. | <img width="175" height="131" alt="image" src="https://github.com/user-attachments/assets/25dda003-8ab8-48c4-a7d1-1a45fdbca7a4" /> |
| **Pins Header** <br> (Connecteur IOs) | **µCompute Rover** <br> (REV 1.0) | Contrôleur de moteur DC (2+2) + Servo + HC-SR04 + Module GPS (Neo-6M). | <img width="220" height="145" alt="image" src="https://github.com/user-attachments/assets/90114819-d70b-4cbb-8cfd-5e95b66cca84" /> |

---

## 🎮 Contrôle à distance (Mode RC)

Le **uCompute Rover** intègre un mode de pilotage radiocommandé (RC) autonome. La télécommande est construite autour d'un second module uCompute équipé d'un joystick analogique, de boutons poussoirs, d'un écran OLED SSD1306 et d'un module radio NRF24L01+.

<p align="center">
  <img width="495" height="676" alt="image" src="https://github.com/user-attachments/assets/c12b0136-ba45-4c3e-a211-9a4611322f68" />
</p>

### 📐 Conception mécanique et boîtier 3D
L'ergonomie de la manette a été spécialement étudiée pour offrir une prise en main confortable grâce à des poignées latérales intégrées. 

* 📁 Le fichier STL du boîtier est disponible ici : **[RC_remote_v1.stl](https://github.com/JPMichon/uCompute_Rover/blob/main/3D_Parts/RC_remote_v1.stl)**

### 💾 Scripts de test (MicroPython)
Le système s'appuie sur deux scripts distincts qui gèrent la communication bidirectionnelle en temps réel (envoi des commandes de pilotage et réception de la télémétrie sur l'écran OLED) :

1. **Côté Télécommande :** **[Remote_Rover_v1_SSD1306.py](https://github.com/JPMichon/uCompute_Rover/blob/main/testcode/Remote_Rover_v1_SSD1306.py)**
   * Initialise le bus SPI pour le module radio NRF24L01+.
   * Lit l'état du joystick analogique (axes X/Y) et des boutons de commande.
   * Gère l'affichage des informations système sur l'écran OLED local.
   * Transmet les paquets de commande vers le robot de manière périodique.

2. **Côté Rover :** **[RC_Rover_v1_SSD1306.py](https://github.com/JPMichon/uCompute_Rover/blob/main/testcode/RC_Rover_v1_SSD1306.py)**
   * Reste à l'écoute des paquets radio émis par la télécommande.
   * Décode les consignes de trajectoire et de vitesse pour piloter les moteurs CC via les ponts en H DRV8833.
   * Gère la sécurité (arrêt d'urgence automatique des moteurs en cas de perte de liaison radio).

---

## 🚀 Évolution vers un Rover Autonome et Télémétrie

Bien que le projet soit initialement présenté avec un mode de pilotage radiocommandé (RC), l'architecture matérielle du **uCompute Rover** a été pensée dès le départ pour la modularité. Grâce à ses nombreux capteurs embarqués, le robot peut très facilement être transformé en **véhicule 100 % autonome**.

### 🤖 Logique d'Autonomie Évolutive
La carte d'interface (*Roverboard*) interconnecte nativement tous les éléments essentiels pour permettre au microcontrôleur RP2040 de prendre des décisions en temps réel :
* **Évitement d'obstacles :** Le capteur à ultrasons **HC-SR04** (ou le capteur laser ToF **VL53L0X**) permet de cartographier l'environnement direct et d'adapter la trajectoire.
* **Navigation et orientation :** L'ajout de la boussole magnétique **GY-271** et du module GPS **NEO-6M** ouvre la voie à des algorithmes de navigation par points de passage (*waypoints*).

Le passage au mode autonome ne nécessite aucune modification matérielle majeure : il s'agit principalement d'un **déploiement logiciel** (scripts de contrôle de trajectoire automatique en MicroPython).

### 🌐 Pilotage par Interface Web (Wi-Fi)
Puisqu'un module **Wi-Fi (ESP-12F)** est disponible dans l'écosystème uCompute (conçu pour s'insérer sur le socket arrière de communication), les possibilités de contrôle à distance s'étendent au réseau IP. 

En déployant un micro-serveur HTTP en MicroPython sur l'uCompute, il devient possible de :
* **Piloter le rover depuis n'importe quel appareil** (smartphone, tablette ou PC) connecté au même réseau Wi-Fi, sans avoir besoin d'une manette physique.
* Créer une **interface web moderne et interactive** (boutons tactiles, sliders de vitesse, joystick virtuel en JavaScript) pour contrôler les mouvements du robot en toute simplicité.

  ### 📡 Liaison Longue Portée (LoRa)
Grâce au bus SPI exposé sur le socket arrière, l'intégration d'un module radio **LoRa** (comme le RFM95W ou équivalent) est également envisageable avec très peu d'efforts. Cette technologie permet d'étendre radicalement le rayon d'action du rover, autorisant la transmission de commandes et de télémétrie sur de très longues distances en extérieur (milieu rural ou urbain dense), là où le Wi-Fi ou les liaisons 2,4 GHz classiques s'essoufflent. 

*Note : Un add-on LoRa standardisé fait partie des pistes de réflexion et pourrait être officiellement disponible dans les prochaines évolutions de la plateforme uCompute.*

### 📊 Télémétrie Bidirectionnelle en Temps Réel
En mode autonome, les modules radio **NRF24L01+** changent de rôle. Au lieu de simplement recevoir des commandes de pilotage, le lien sans fil sert à renvoyer un flux constant de données (télémétrie) vers une station au sol (PC, console ou le module *uCompute Remote*) :
* Surveillance en temps réel de la tension et du courant consommé (via le capteur de puissance **INA219**).
* Transmission des coordonnées géographiques (GPS), du cap (boussole) et des conditions environnementales (température, pression via le **BME280**).
* Visualisation des données thermiques à distance si le capteur infrarouge **AMG8833** est installé.

*Un ensemble de scripts exemples dédiés à la navigation autonome et au protocole de communication de télémétrie sera progressivement ajouté au dossier `testcode`.*

---

# 🎯 Le projet idéal pour vous lancer

Vous rêvez de construire votre propre plateforme de robotique avancée, mais vous ne savez pas par où commencer ? Vous avez peur de manquer de temps, de connaissances en programmation ou d'expertise en électronique ? Vous craignez de vous perdre dans un fouillis de câbles qui se débranchent tout le temps, ou de bloquer vos élèves avec du code trop complexe ?

Le **uCompute Rover** a été créé précisément pour en finir avec ces frustrations.

## 🧠 Pas besoin d'être un expert pour débuter
* **Zéro programmation complexe :** Oubliez le C++ austère. Le robot est propulsé par le microcontrôleur RP2040 et se programme en **MicroPython**. C'est le langage le plus simple, le plus lisible et le plus rapide à apprendre aujourd'hui. En quelques lignes de code, votre robot avance.
* **Zéro blocage frustrant :** Grâce au système visuel intégré (*uComputeOS*), si vous ou l'un de vos élèves faites une erreur dans le code, l'écran affiche une alerte claire au lieu de faire planter complètement la carte. Vous comprenez l'erreur instantanément sans perdre de temps.

## 🛠️ Zéro soudure si vous le souhaitez !
* Vous pensez ne pas avoir le niveau pour souder de minuscules composants électroniques (CMS) ? Aucun problème. Bien que la carte finale soit ultra-propre, le projet est conçu pour être **100 % reproductible sur une simple plaque de prototypage (*Breadboard*)** avec un Raspberry Pi Pico ou Pico 2 classique à bas coût. C'est la solution idéale pour débuter rapidement à la maison ou équiper toute une classe avec un budget maîtrisé.

## 🚀 Une évolution sans limites, à votre rythme
Ne restez pas bloqué avec un robot jouet figé. Commencez par un châssis basique télécommandé en ligne droite, puis faites-le évoluer quand vous aurez le temps : ajoutez le Wi-Fi pour le piloter depuis votre smartphone, connectez un module radio longue portée, ou installez un GPS et un capteur de distance pour le rendre totalement autonome.

## 🛠️ Pour les Makers : Le bac à sable ultime
* **Modularité totale :** Finis les robots figés ou les amas de câbles *Dupont* instables. Grâce à son système de cartes filles interchangeables, faites évoluer votre rover au gré de vos envies : ajoutez le Wi-Fi (ESP-12F), la radio (NRF24L01+), le LoRa, un GPS ou de l'imagerie thermique sans jamais refaire le circuit principal.
* **Architecture ouverte :** Explorez des protocoles industriels et de communication standardisés (I2C, SPI, UART, PWM) sur une plateforme robuste et gratifiante.

## 🎓 Pour les Écoles & Projets Éducatifs : Une pédagogie sans friction
* **Barrière à l'entrée minimale :** Propulsé par le microcontrôleur RP2040 et les technologies d'uCompute, le rover permet aux étudiants de comprendre et d'obtenir des résultats concrets en seulement quelques lignes de code, bien plus rapidement qu'en C++.
* **Sécurité et tolérance aux erreurs :** Grâce à l'interface de diagnostic intégrée (*uComputeOS*), si le code d'un élève contient une erreur, la carte capture l'exception et affiche un écran d'alerte visuel au lieu de figer le robot. L'apprentissage se fait par expérimentation fluide, sans frustration.
* **Accessible à tous les budgets :** Si l'assemblage CMS d'origine demande de l'expertise, la plateforme est **100 % rétrocompatible sur plaque de prototypage (*Breadboard*)** avec un Raspberry Pi Pico ou Pico 2 standard. Vous pouvez équiper une classe entière à moindre coût !

*Le uCompute Rover vous fournit une base mécanique et électronique solide. Vous n'avez plus qu'à assembler les blocs, à votre rythme et selon vos compétences actuelles.*

---


## 📜 Licence

Le matériel (fichiers de conception, schémas, typons) et les logiciels de ce projet sont mis à disposition selon les termes de la Licence **Creative Commons Attribution - Pas d'Utilisation Commerciale - Partage dans les Mêmes Conditions 4.0 International (CC BY-NC-SA 4.0)**.

❌ **L'utilisation commerciale de ce projet (revente de PCBs nus, kits ou cartes retroPico assemblées) est strictement interdite sans autorisation préalable de l'auteur.**

Consultez le fichier [LICENSE](LICENSE) pour lire l'intégralité des termes.

---

## ☕ Soutenir le projet

Si vous appréciez mon travail et souhaitez m'offrir un café pour me soutenir bénévolement dans mes futurs projets de soudure et de code, vous pouvez me laisser un [**pourboire sur Ko-fi** ](https://ko-fi.com/jpmichon) . C'est entièrement volontaire et grandement apprécié !

