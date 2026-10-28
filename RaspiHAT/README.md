# En Constuction

A vos risques (pour l'instant, en phase de test)

# Block diagram

<img width="1092" height="694" alt="image" src="https://github.com/user-attachments/assets/2a73a6bf-f385-48a7-b643-c1e354bbf833" />




# Rendu 3D du RASPI ROVER HAT

<img width="698" height="815" alt="image" src="https://github.com/user-attachments/assets/49894fa0-a319-47ab-95f4-9f3d2e5b3dcc" />



## Tableau de correspondance de votre câblage sous Python3


| Signal nRF24 | Broche Physique (Raspberry Pi) | Identifiant dans le code Python | Rôle |
| :--- | :--- | :--- | :--- |
| **CSN** | GPIO 8 | `board.D8` | Sélection de la puce SPI |
| **CE** | GPIO 22 | `board.D22` | Activation Radio (Émission/Réception) |
| **MOSI** | GPIO 10 | Géré automatiquement par `busio.SPI` | Données Sortantes SPI |
| **MISO** | GPIO 9 | Géré automatiquement par `busio.SPI` | Données Entrantes SPI |
| **SCLK** | GPIO 11 | Géré automatiquement par `busio.SPI` | Horloge SPI |
| **IRQ** | GPIO 13 | `board.D13` | Signal d'interruption matérielle |

### Cartographie Matérielle (Moteurs, Capteurs et Sécurité)

| Composant / Module | Signal du Schéma | Broche GPIO (BCM) | Broche Physique Pi | Rôle Logique dans le Robot |
| :--- | :--- | :---: | :---: | :--- |
| **Moteurs Gauche** | `AIN1`/`BIN1` | **GPIO 5** |  | Vitesse / Direction (PWM) |
| | `AIN2`/`BIN2` | **GPIO 6** |  | Direction (PWM)|
| | `FAULT1` (ULT) | **GPIO 12** | Broche 32 | Détection de surchauffe / court-circuit U2 |
| **Moteurs Droit** | `AIN1`/`BIN1` | **GPIO 17** |  | Vitesse / Direction (PWM) |
| | `AIN2`/`BIN2`  | **GPIO 27** | | Direction (PWM) |
| | `FAULT2` (ULT) | **GPIO 25** | Broche 22 | Détection de surchauffe / court-circuit U3 |
| **Mise en veille <br> (U2 + U3)**| `nSleep` | **GPIO 26** | Broche 37 | Actif à l'état HAUT. Réveille les deux drivers DRV8833 |
| **Moniteur Énergie** | `VCC Detect` | **GPIO 7** | Broche 26 | Surveillance de la présence de la tension de puissance |
| **Télémètre (HC-SR04)** | `TRIG` | **GPIO 23** | Broche 16 | Émission de l'impulsion ultrason |
| | `ECHO` | **GPIO 24** | Broche 18 | Mesure du temps de retour de l'onde |
| **Alerte Sonore** | `BUZ` | **GPIO 16** |  | Signal sonore d'état ou d'erreur (Buzzer) |
| **Fan** | `FAN` | **GPIO 18** |  | Activation/desactivation du FAN |
| **Servomoteur** | Servo 1 (`M1`) | **GPIO 20** |  | Commande de position angulaire (PWM) |
| **Servomoteur** | Servo 2 (`M1`) | **GPIO 21** |  | Commande de position angulaire (PWM) |
| **NeoPixel** |`DI`|**GPIO 19**| Broche 35 | Signal Données NeoPixel WS2812B |

## Module de gestion d'allimentation (Power Management)

Ce module permet de réglé la spaghetti du cablage tout en permettant d'avoir du monitoring des alimentations.

<img width="1051" height="724" alt="image" src="https://github.com/user-attachments/assets/eed6e33b-775d-4ea7-8a05-cf65b467892f" />

### 📋 Nomenclature des coûts (BOM) — Rover version Pi 3B+

| Qté | Description | Prix (CAD) |
| :---: | :--- | :---: |
| 1 | Raspberry Pi 3B+ | 60.00 $ |
| 1 | Power module (2x bucks + INA3321) | 15.00 $ |
| 1 | GPS Module NEO6M + Antenne | 10.00 $ |
| 1 | I2C GUI module (SSD1306 + PCF8574 + AT24C) | 15.00 $ |
| 1 | Pi hat PCB + composants passifs | 10.00 $ |
| 1 | CSI longue pour la caméra (30cm) | 5.00 $ |
| 2 | Servo SG90 | 5.00 $ |
| 1 | Ventilateur 5V | 2.50 $ |
| 1 | Capteur ultrasons HC-SR04 | 1.00 $ |
| 1 | Adaptateur + NRF24L01+ | 5.00 $ |
| 4 | Moteur TT + Roue tout-terrain | 15.00 $ |
| 1 | Capteur de distance ToF — VL53L0X | 5.00 $ |
| 1 | Boussole GY-271 QMC5883 | 5.00 $ |
| 2 | Driver de moteur DRV8833 | 5.00 $ |
| 1 | PiCam générique | 15.00 $ |
| 1 | Barrette Neopixel | 1.00 $ |
| 1 | PLA + Quincailleries + carte MicroSD 16Go | 25.00 $ |
| **Total** | **Coût de revient estimé** | **199.50 $** |

---

### 💡 Notes importantes sur la fabrication et le sourcing

* **Optimisation des circuits imprimés (PCBs) :** Les usines de fabrication (comme JLCPCB ou PCBWay) produisent généralement les circuits imprimés par lots minimaux de 5 ou 10 unités. À l'unité, le coût de revient réel de la plaque de circuit nu tombe à **environ 2,00 $ la pièce**. Pour réduire drastiquement l'impact des frais de port industriels, il est fortement recommandé de **combiner la commande de vos différents PCBs** (la carte mère Pi Hat et les modules d'extension) au sein d'un même panier d'expédition.
* **Stratégie d'approvisionnement (Sourcing) :** Pour l'achat de la quincaillerie et des modules électroniques, l'utilisation de plateformes comme **AliExpress** (en regroupant vos articles via les offres *Choice* pour débloquer la livraison gratuite) ou **Amazon** (pour les pièces requérant une réception rapide) constitue l'option de loin la plus économique pour respecter ce budget de moins de 200 $ CAD.
### 💡 Notes importantes sur la fabrication et le sourcing

* **Optimisation des circuits imprimés (PCBs) :** Les usines de fabrication (comme JLCPCB ou PCBWay) produisent généralement les circuits imprimés par lots minimaux de 5 ou 10 unités. À l'unité, le coût de revient réel de la plaque de circuit nu tombe à **environ 2,00 $ la pièce**. Pour réduire drastiquement l'impact des frais de port industriels, il est fortement recommandé de **combiner la commande de vos différents PCBs** (la carte mère Pi Hat et les modules d'extension) au sein d'un même panier d'expédition.
* **Stratégie d'approvisionnement (Sourcing) :** Pour l'achat de la quincaillerie et des modules électroniques, l'utilisation de plateformes comme **AliExpress** (en regroupant vos articles via les offres *Choice* pour débloquer la livraison gratuite) ou **Amazon** (pour les pièces requérant une réception rapide) constitue l'option de loin la plus économique pour respecter ce budget de moins de 200 $ CAD.
* **📦 Le syndrome du tiroir à composants (La règle du Maker) :** Soyons honnêtes : comme tout bon maker qui se respecte, vous accumulez probablement une quantité déraisonnable de modules et de quincaillerie qui dorment dans vos tiroirs depuis des mois (voire des années). Bon nombre de ces composants n'attendent qu'à être dépoussiérés pour enfin servir à quelque chose ! Honnêtement, combien de Raspberry Pi avez-vous dans vos tiroirs ? Au final, le coût réel de ce Rover devrait être largement inférieur aux 199,50 $ affichés, le tout indexé sur votre degré d'accumulation personnel. **C'est l'excuse parfaite pour justifier ce projet auprès de vos proches !**


  
## Version provisoire  <br>

Le Raspi sur son support du Rover.

A noter le trou pour le micro interrupteur. Une nouvelle version avec deux trous sera disponible sous peu. <br>


<img width="833" height="622" alt="image" src="https://github.com/user-attachments/assets/d6b8107f-96bd-4c11-b19a-7536e8db5db1" />

## (Beauty Shoots) du rover avec une version _prototype_ du raspberry PI HAT

<img width="481" height="697" alt="image" src="https://github.com/user-attachments/assets/bda82363-5f9d-4d3a-b798-940965958e41" />

<img width="512" height="671" alt="image" src="https://github.com/user-attachments/assets/b8b6e79b-4d0a-4950-9bf9-986f170248af" />

<img width="444" height="608" alt="image" src="https://github.com/user-attachments/assets/aa1b6f92-8ef1-40e4-a946-5e4110ff0dbc" />




