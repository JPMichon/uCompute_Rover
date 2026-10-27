# En Constuction

A vos risques

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

## Version préliminaire  <br>

Le Raspi sur son support du Rover.

A noter le trou pour le micro interrupteur. Une nouvelle version avec deux trous sera disponible sous peu. <br>


<img width="833" height="622" alt="image" src="https://github.com/user-attachments/assets/d6b8107f-96bd-4c11-b19a-7536e8db5db1" />

## (Beauty Shoots) du rover

<img width="481" height="697" alt="image" src="https://github.com/user-attachments/assets/bda82363-5f9d-4d3a-b798-940965958e41" />

<img width="512" height="671" alt="image" src="https://github.com/user-attachments/assets/b8b6e79b-4d0a-4950-9bf9-986f170248af" />

<img width="444" height="608" alt="image" src="https://github.com/user-attachments/assets/aa1b6f92-8ef1-40e4-a946-5e4110ff0dbc" />




