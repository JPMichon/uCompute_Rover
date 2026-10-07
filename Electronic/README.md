# ⚡ Câblage du uCompute Rover

Ce répertoire regroupe toutes les informations nécessaires pour assembler, câbler et alimenter les composants électroniques du robot.

## 🗺️ Vue schématisée de l'électronique embarquée
<p align="center">
<img width="700" height="720" alt="image" src="https://github.com/user-attachments/assets/95619a81-7fdf-4ab7-bc80-40e4ef133049" />

</p>

---

#  Guide de montage

<br>

## ⚙️ Installation des moteurs

### **Vous aurez besoin de:** <br>
• 8 vis de (25 mm x 3 mm), <br>
• 4 vis perçante de (3 mm  x 5 mm), <br>
• 4 roues tout-terrain, <br> 
• 4 moteurs TT double CC 3-6 V Rapport 200 tr/min, réduction 1:48, <br>      
<img width="161" height="86" alt="image" src="https://github.com/user-attachments/assets/4b796235-ff34-42b0-b956-b00d7a48ca09" /> <img width="90" height="90" alt="image" src="https://github.com/user-attachments/assets/b3bb7392-6669-4420-9f55-6e464e4ed142" /><br>

**Alonger les fils des moteurs aux besoins** :  Ma version prototype utilise des connecteurs **JST-XH 2.54 2-pin**<br> 
Libre à vous d'utiliser votre propre recette.

Chaque moteur est raccordé par un fil à deux conducteurs de calibre 26 AWG d'environ **30 cm**.

### Étapes:
| Insérer le fil dans le trou du haut | Insérer chaque fil de chaque côté | Souder les fils aux bornes du moteur | Sécuriser le moteur à l'aide de vis | Sortir l'autre extrémité dans le bas de la plaque électronique | Ajouter un collant sur les axes des 4 moteurs 
| :---: | :---: | :---: | :---: | :---: | :---: |
| <img width="150" height="195"  alt="image" src="https://github.com/user-attachments/assets/3da047b3-cd6d-452a-b9b7-f2d928ebe226" /> | <img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/35381b1d-b1d5-4d95-a2ac-663825c24f85" /> | <img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/e0115f6c-00bd-4f50-b995-d03e1cee78ea" /> | <img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/bedd2ab9-a23f-4b60-a01e-06ba27a4e731" /> |   <img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/f078b472-b96a-4687-ac73-6bcecad818a1" /> | <img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/9e90e19c-61b7-4f4f-9f23-453a9aff9fd4" /> 



>[!NOTE]
> Afin de **vous faire gagner du temps**, assurez-vous de toujours souder la borne positive et la borne négative dans le même ordre, car le module de puissance inverse la polarité du second moteur d’un même **côté**. **Cela signifie que si les moteurs reculent** au lieu d’avancer, **il faut** inverser les connecteurs entre les deux moteurs. <br>
><img width="493" height="365" alt="image" src="https://github.com/user-attachments/assets/a11a52eb-1617-4ab3-91f5-c9088e2ee0c3" /> <br>
> Autre élément : les **moteurs droit et gauche fonctionnent** par **paire**. **C'est-à-dire** que les **deux** moteurs d’un même côté sont câblés pour être synchrones. Cela permet de diminuer **le nombre d'E/S (IOs)** requis pour piloter les moteurs. L’autre avantage est de faciliter l’utilisation de **chenilles** sans devoir mettre en place des garde-fous logiciels, tout en permettant plus de fonctionnalités sur le Rover Board. Cependant, **tout avantage ayant ses inconvénients**, cette configuration **ne permet pas** l’utilisation de **roues Mecanum**. Comme le **uCompute Rover est modulaire** et les schémas sont disponibles, **il est relativement simple de bricoler votre propre module** de contrôle des moteurs. Il est impossible, que dans un avenir plus ou moins rapproché, j'ajoute un module spécifique pour piloter des **roues Mecanum**.

## ⚙️ Installation des modules de controle

### **Vous aurez besoin de:** <br>
• 1 x module RP2040 uCompute,<br>
• 1 x uCompute Rover module,<br>
• 2 x Module DRV8833
• 8 vis perçante de (3 mm  x 5 mm), <br>

### Installation:
| Préparer 4 vis de montage | Fixer le module <br> RP2040 uCompute | Préparer 4 vis de montage | Fixer le module <br> uCompute Rover | Raccorder les moteurs <br> droite et gauche | Insérer les modules DRV8833 <BR> (broches Output vers le bas)|
| :---: | :---: | :---: | :---: | :---: | :---: |
|<img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/3ec77fa0-d365-4186-8708-d8237c24c6ca" /> | <img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/79f8e3ea-e109-46d2-86dd-459fcce02352" /> | <img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/3ec77fa0-d365-4186-8708-d8237c24c6ca" /> | <img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/be683505-5f27-4249-aa85-a1ee1a0a3862" /> | <img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/fc1628c4-654d-496d-a528-4a6979441c69" /> | <img width="195" height="130" alt="image" src="https://github.com/user-attachments/assets/51e70eb6-8db5-4d5a-8402-acc7078e0970" />

## ⚙️ Installation de l'interrupteur d'alimentation
### **Vous aurez besoin de:** <br>
• 1 x fil à deux conducteurs de calibre **24 AWG** d'environ **20 cm**.,<br>
• 1 x un interrupteur à bascule SPST modele: **KCD11 (10X15mm)**,<br>

### Installation:
| Souder le fils sur les bornes de l'interrupteur | Insérer l'interrupteur dans le trou carré du panneau de controle |
| :---: | :---: |
|<img width="500" height="150" alt="image" src="https://github.com/user-attachments/assets/733b0b0f-aa1c-450f-910f-20608ac14508" />|<img width="350" height="340" alt="image" src="https://github.com/user-attachments/assets/3aaee718-4ee8-49d7-90cf-3798e28d6079" />

## :scissors: Fixation de l'alimentation
Cette section est simple, mais efficace…<BR>
Pour maintenir en place les différents composants, la façon la plus simple reste l’utilisation de bandes Velcro.<br>
_Si c’est assez bon pour la NASA, c’est bon pour le Rover !_

### Étapes:
| Coller une bande de Velco <br> sur la tablette du haut | Coller des bandes de Velco <br> sous le porte-piles   | Coller une bande de Velco <br> sous le régulateur | Tester l'installation |
| :---: | :---: | :---: | :---: |
|<img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/c107f1a8-6312-4248-9366-c316a7f7d4ba" /> | <img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/57736bb1-8eb8-4f72-b4a3-aec0f6b3897c" />|<img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/de930fa3-1bfb-46a3-a759-b9004eb18326" />|<img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/f7e2de8b-040c-4291-987d-cc17d87b8475" />|

## ⚙️ Préparation et installation de la bande NeoPixel

> [!NOTE]
> Seulement disponible pour le  `frontal_sensor_v3.stl` intégrant nativement la bande **Neopixel**.
> 
### **Vous aurez besoin de:** <br>
• 3 x fils avec connecteur **DuPont** femelle a l'un des bouts. Longueur environ **25 cm**,<br>
• 1 x bande **Neopixel** de 8 x **WS2812B** (5050) adressables,<br>
• 2 vis perçante de (3 mm  x 5 mm), <br>

### Étapes:
| Vue de la bande Neopixel | Souder les fils <br> sur le coté  avec DI  | Résultat | Préparer 2 vis de montage | Fixer le module NeoPixel <br> sous le sonar |
| :---: | :---: | :---: | :---: | :---: |
|<img width="174" height="140" alt="image" src="https://github.com/user-attachments/assets/cdb4634b-3352-4bdd-9df5-cf7747b15e1e" /> | <img width="140" height="140" alt="image" src="https://github.com/user-attachments/assets/32493c68-3fc3-417f-8772-2d89dd0ca7c9" /> | <img width="174" height="140" alt="image" src="https://github.com/user-attachments/assets/1256647f-7e10-459c-887c-93a61bae876d" /> | <img width="140" height="140" alt="image" src="https://github.com/user-attachments/assets/5aad3843-ac5f-4070-b4c9-71dc1bb1a9b1" /> | <img width="174" height="140" alt="image" src="https://github.com/user-attachments/assets/56701e16-c661-4b51-9658-7692be9a8ef8" />|

## :scissors: Installation du Sonar HC-SR04
Pour cette partie, vous aurez besoins de **colle chaude…** <br>
Vivement l'artisanat! <br>

### **Vous aurez besoin de:** <br>
• 4 x fils avec connecteur **DuPont** femelle au deux bouts. Longueur environ **25 cm**,<br>
• 1 x Module de Sonar HC-SR04<br>

### Étapes:
| Installation des **fiches Dupont** <br> sur le sonar | Installation du capteur dans son socle <br> un peu de colle chaude pour le tenir en place |
| :---: | :---: |
|<img width="140" height="140" alt="image" src="https://github.com/user-attachments/assets/ae667222-eca8-4012-8073-a54363463a40" />|<img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/83c1719c-cbda-49d0-8bfa-db9b828553cb" />|

> [!NOTE]
> La colle chaude a un point de fusion au alentour de 190 °C. très près des températures d'impression des pièces en 3D. <br>
> **Allez y parcimonieusement** avec la colle chaude pour évitez de déformer vos pièces.

## ⚙️ Installation du servo moteur
### **Vous aurez besoin de:** <br>
• 1 x **SG90 Mini Gear Micro 9g** Servo ou équivallent,<br>
• 2 vis perçante de (2 mm  x 5 mm). (généralement inclus avec le Servo). <br>
### Étapes:
| Image du servo | Préparer 2 vis | Fixer le servo <br> au support |
| :---: | :---: | :---: |
|<img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/668c6d31-3bc1-4559-942a-de1110a8d83f" /> | <img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/c54f9c5b-419e-45fa-821b-f27f2311db96" /> | <img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/6fb1a63c-3361-4c0a-aba4-560b6990f80c" />|

## ⚙️ Préparation du LM2596
### **Vous aurez besoin de:** <br>
• 1 x fil à deux conducteurs de calibre **24 AWG** d'environ **10 cm**.,<br>
• 1 x fil à deux conducteurs de calibre **24 AWG** d'environ **15 cm**  avec un connecteur **JST XH2.54 2P** à l'un des bout,<br>
• 1 x un module **convertisseur DC-DC LM2596**,<br>
### Étapes:
| Souder les fils<br>  + rouge, - Noir | Gros plan sur le  <br>connecteur JST XH2.54 2P | 
| :---: | :---: |
|<img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/db85b3f0-d31a-4ef3-8d37-3c7a2af4c18b" />|<img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/1485ad30-8d50-4e6b-a011-543ba3d12896" />|

> [!WARNING]
> ### ⚡ ATTENTION : Réglage impératif du régulateur LM2596
> Le module du Rover requiert une tension d'alimentation stricte de **5 V**. Le convertisseur DC-DC LM2596 étant un régulateur **ajustable**, il est **crucial d'ajuster sa tension de sortie à 5 V à l'aide d'un multimètre AVANT de le connecter** aux cartes électroniques du Rover. 
> 
> Brancher le régulateur sans réglage préalable ou avec une tension trop élevée entraînera la **destruction immédiate** du microcontrôleur RP2040, de l'écran LCD et de l'ensemble de vos capteurs.

### Ajustement du régulateur

**À l’aide d’un multimètre et d’un petit tournevis plat, ajustez la tension en tournant la vis du potentiomètre (indiquée sur la photo ci-dessous).**
> 🔄 **Sens de réglage du potentiomètre :**
> * **Pour DIMINUER la tension :** Tournez la vis dans le **sens inverse des aiguilles d'une montre** (antihoraire).
> * **Pour AUGMENTER la tension :** Tournez la vis dans le **sens des aiguilles d'une montre** (horaire).
> 
> *Note : Ces potentiomètres multitours possèdent souvent une large plage de réglage initiale. Il est tout à fait normal de devoir effectuer plusieurs tours complets (parfois plus de 10 à 15 tours) avant de voir la tension commencer à varier sur votre multimètre. Procédez par petits gestes une fois proche des 5 V.*

<p align="center">
<img width="569" height="371" alt="image" src="https://github.com/user-attachments/assets/10494b81-9cd7-41e0-a7ae-1cd8d28e3c3e" />
</p>



## 🔋 Schéma de l'alimentation électrique

Le Rover est propulsé par un boîtier de 6 piles AA (ou équivalent). La tension est abaissée à **5 V (2 A min)** via le module LM2596 pour alimenter la carte principale, les moteurs et le servomoteur.

<p align="center">
<img width="500" height="350" alt="image" src="https://github.com/user-attachments/assets/0465d19e-39bf-4fe8-96a4-ff1c747c2283" />
</p>

---

## Le branchement finale
L'alimentation, le Sonar HC-SR04 et le Servo ce connecte tous a cet endroit sur la carte de controle.<br>
Les **Neopixels** ce connecte directement sur le uCompute.<br>

Les moteurs ont déjà été connecté précédemment. Si il ne le sont pas, vous pouvez les connecter. <br> 

### Étapes:
| Gros plan sur les connecteurs | une fois connectés| Branchez le Neopixel <br> directement sur le uCompute | Branchez le INA219 <br> à l'arrière du uCompute |
| :---: | :---: | :---: | :---: |
|<img width="260" height="260" alt="image" src="https://github.com/user-attachments/assets/d5e51127-a20c-459e-b88b-437bd7cad6f1" /> | <img width="210" height="265" alt="image" src="https://github.com/user-attachments/assets/8a936ef8-850f-44cf-b5c1-ff70a51956a8" /> |<img width="220" height="270" alt="image" src="https://github.com/user-attachments/assets/c901930c-2662-46a1-947c-ffec8f33ab00" /> |<img width="220" height="270" alt="image" src="https://github.com/user-attachments/assets/addd0c1f-4bb3-4e6b-9fe0-355f3d8e9717" />|

## Plus d'un capteur I2C, pas de problème
Il y a de forte chance pour que vous désiriez avoir plus d'un capteur I2C. La solution est assez simple et ce résout par un simple bricollage.

### Détail du bricollage
| Vu du dessus | Détail des soudures | 
| :---: | :---: |
|<img width="490" height="482" alt="image" src="https://github.com/user-attachments/assets/60e30bce-4825-49b2-8960-8a73b0164005" /> | <img width="476" height="485" alt="image" src="https://github.com/user-attachments/assets/09589e99-1ec8-4e45-9f84-ce6641fc09cc" /> |

> [!NOTE]
>Le bus I2C a besoin de deux résistances de pull-up (une sur SDA, une sur SCL) reliées au VCC pour fonctionner.<br>
>• La plupart des modules de capteurs prêts à l'emploi (shields/breakouts) intègrent déjà ces résistances.<br>
>• En mettre trop en parallèle fait chuter la résistance totale (loi des mailles). Si vous connectez plus de 3 ou 4 capteurs, le signal peut se dégrader.<br>
> Si vous rencontrez des erreurs de communication, il faudra retirer (dessouder) les résistances de tirage de certains modules pour n'en garder qu'une seule paire sur tout le bus. <br>




