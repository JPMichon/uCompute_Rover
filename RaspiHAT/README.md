# En Constuction

A vos risques

<img width="628" height="745" alt="image" src="https://github.com/user-attachments/assets/449dcb6e-3a0f-4fcc-bb92-41bd3b2287ab" />


## Tableau de correspondance de votre câblage sous Python3


| Signal nRF24 | Broche Physique (Raspberry Pi) | Identifiant dans le code Python | Rôle |
| :--- | :--- | :--- | :--- |
| **CSN** | GPIO 8 | `board.D8` | Sélection de la puce SPI |
| **CE** | GPIO 22 | `board.D22` | Activation Radio (Émission/Réception) |
| **MOSI** | GPIO 10 | Géré automatiquement par `busio.SPI` | Données Sortantes SPI |
| **MISO** | GPIO 9 | Géré automatiquement par `busio.SPI` | Données Entrantes SPI |
| **SCLK** | GPIO 11 | Géré automatiquement par `busio.SPI` | Horloge SPI |
| **IRQ** | GPIO 13 | `board.D13` | Signal d'interruption matérielle |
