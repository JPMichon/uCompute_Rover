## 🤖 Module Rover

# 4WD Rover
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
* 2 x Modules radio NRF24L01+
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
![Diagramme du rover](https://github.com/JPMichon/uCompute_Rover/blob/main/Rover_Diagram_V1.png)

---

## 🤖 Module Rover

Le module Rover se connecte directement à l'interface de la carte principale. Cette dernière intègre le port VIN, qui doit impérativement être alimenté en courant continu (CC) sous une tension de 5 V, avec une source capable de délivrer environ 2 A. 

À partir de cette ligne 5 V, les éléments suivants sont alimentés en direct :
* Le servomoteur
* Le capteur HC-SR04
* Les deux contrôleurs de moteur DRV8833

Enfin, cette tension alimente également la broche 5 V du module principal, qui fait office de tension continue (CC) pour le circuit de régulation. Le module GPS, quant à lui, est alimenté en 3,3 V depuis le régulateur de la carte principale.

## 📻 Module Radio NRF24L01+

La communication sans fil est gérée par un module radio NRF24L01+. Celui-ci est relié à l'uCompute via un adaptateur dédié qui se connecte à l'arrière de la carte (sur le connecteur initialement réservé au module W5500). 

Ce module radio offre une grande flexibilité d'intégration. Selon vos besoins, vous pouvez opter pour :
* La version équipée d'un connecteur mâle double rangée (*header* DIN 2x4).
* La version miniature de type CMS (*SMD*).

Il existe également des variantes dotées d'un amplificateur de signal et d'un préamplificateur à faible bruit (**PA+LNA**). Ces dernières permettent de raccorder une antenne externe via un connecteur IPEX, augmentant ainsi considérablement la portée du signal. Selon les sources consultées et le débit de données configuré, il est possible d'établir une liaison stable sur plusieurs kilomètres. De plus, ce matériel prend nativement en charge les architectures de réseau maillé (*mesh*).

[Consulter la fiche technique du NRF24L01P (PDF)](https://docs.nordicsemi.com/bundle/nRF24L01P_PS_v1.0/resource/nRF24L01P_PS_v1.0.pdf)


---

## 📜 Licence

Le matériel (fichiers de conception, schémas, typons) et les logiciels de ce projet sont mis à disposition selon les termes de la Licence **Creative Commons Attribution - Pas d'Utilisation Commerciale - Partage dans les Mêmes Conditions 4.0 International (CC BY-NC-SA 4.0)**.

❌ **L'utilisation commerciale de ce projet (revente de PCBs nus, kits ou cartes retroPico assemblées) est strictement interdite sans autorisation préalable de l'auteur.**

Consultez le fichier [LICENSE](LICENSE) pour lire l'intégralité des termes.

---

## ☕ Soutenir le projet

Si vous appréciez mon travail et souhaitez m'offrir un café pour me soutenir bénévolement dans mes futurs projets de soudure et de code, vous pouvez me laisser un [**pourboire sur Ko-fi** ](https://ko-fi.com/jpmichon) . C'est entièrement volontaire et grandement apprécié !

