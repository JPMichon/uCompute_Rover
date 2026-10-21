# En Constuction

A vos risques

<img width="659" height="761" alt="image" src="https://github.com/user-attachments/assets/9d93764b-a566-4956-8e0b-d68c2b9f4383" />



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
| **Alerte Sonore** | `BUZ1` | **GPIO 16** |  | Signal sonore d'état ou d'erreur (Buzzer) |
| **Servomoteur** | Servo 1 (`M1`) | **GPIO 20** |  | Commande de position angulaire (PWM) |
| **Servomoteur** | Servo 2 (`M1`) | **GPIO 21** |  | Commande de position angulaire (PWM) |
| **NeoPixel** |`DI`|**GPIO 19**| Broche 35 | Signal Données NeoPixel WS2812B |
