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

### **Vous aurez besoins de:** <br>
• 8 vis de (25 mm x 3 mm), <br>
• 4 vis perçante de (3 mm  x 5 mm), <br>
• 4 roues tout terrain, <br> 
• 4 moteurs TT double CC 3-6 V Rapport 200 tr/min Moteur d'arbre 1:48, <br>      
<img width="161" height="86" alt="image" src="https://github.com/user-attachments/assets/4b796235-ff34-42b0-b956-b00d7a48ca09" /> <img width="90" height="90" alt="image" src="https://github.com/user-attachments/assets/b3bb7392-6669-4420-9f55-6e464e4ed142" /><br>

**Alonger les fils des moteurs aux besoins** :  Ma version prototype utilise des connecteurs JST-XH 2.54 2-pin, libre à vous d'utiliser votre propre recette.

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

### **Vous aurez besoins de:** <br>
• 1 x module RP2040 uCompute,<br>
• 1 x uCompute Rover module,<br>
• 2 x Module DRV8833
• 8 vis perçante de (3 mm  x 5 mm), <br>

### Installation:
| A l'aide de 4 vis | Sécuriser le <br> RP2040 uCompute | A l'aide de 4 vis | Sécuriser le <br> uCompute Rover module | Raccorder les moteurs <br> droite - gauche | Inserer les modules DRV8833 <BR> output vers le bas |
| :---: | :---: | :---: | :---: | :---: | :---: |
|<img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/3ec77fa0-d365-4186-8708-d8237c24c6ca" /> | <img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/79f8e3ea-e109-46d2-86dd-459fcce02352" /> | <img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/3ec77fa0-d365-4186-8708-d8237c24c6ca" /> | <img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/be683505-5f27-4249-aa85-a1ee1a0a3862" /> | <img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/fc1628c4-654d-496d-a528-4a6979441c69" /> | <img width="195" height="130" alt="image" src="https://github.com/user-attachments/assets/51e70eb6-8db5-4d5a-8402-acc7078e0970" />

## ⚙️ Installation de l'interrupteur d'alimentation
### **Vous aurez besoins de:** <br>
• 1 x fil à deux conducteurs de calibre **24 AWG** d'environ **20 cm**.,<br>
• 1 x un interrupteur à bascule SPST modele: **KCD11 (10X15mm)**,<br>

### Installation:
| Souder le fils sur les bornes de l'interrupteur | Insérer l'interrupteur dans le trou carré du panneau de controle |
| :---: | :---: |
|<img width="500" height="150" alt="image" src="https://github.com/user-attachments/assets/733b0b0f-aa1c-450f-910f-20608ac14508" />|<img width="350" height="340" alt="image" src="https://github.com/user-attachments/assets/3aaee718-4ee8-49d7-90cf-3798e28d6079" />

## ⚙️ Fixation de de l'alimentation

Cette section est low-tech... La façon la plus simple de maintenir en place les différentes composantes, je propose l'utilisation du velcro.

|Coller une bande de velcro <br> sur la tablette du haut| Coller des bandes de velcro <br> sous le porte piles   | Coller une bande de velcro <br> sous le régulateur | Tester l'installation |
| :---: | :---: | :---: | :---: |
|<img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/c107f1a8-6312-4248-9366-c316a7f7d4ba" /> | <img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/57736bb1-8eb8-4f72-b4a3-aec0f6b3897c" />|<img width="140" height="175" alt="image" src="https://github.com/user-attachments/assets/de930fa3-1bfb-46a3-a759-b9004eb18326" />|<img width="175" height="140" alt="image" src="https://github.com/user-attachments/assets/f7e2de8b-040c-4291-987d-cc17d87b8475" />|




### Installation:
---

## 🔋 Schéma de connection de l'alimentation et Puissance
Le Rover est propulsé par un boîtier de 6 piles AA (ou équivalent). La tension est abaissée à **5 V (2 A min)** via le module LM2596 pour alimenter la carte principale, les moteurs et le servomoteur.

<p align="center">
<img width="500" height="350" alt="image" src="https://github.com/user-attachments/assets/0465d19e-39bf-4fe8-96a4-ff1c747c2283" />
</p>

> [!WARNING]
> ### ⚡ ATTENTION : Réglage impératif du régulateur LM2596
> Le module du Rover requiert une tension d'alimentation stricte de **5 V**. Le convertisseur DC-DC LM2596 étant un régulateur **ajustable**, il est **crucial d'ajuster sa tension de sortie à 5 V à l'aide d'un multimètre AVANT de le connecter** aux cartes électroniques du Rover. 
> 
> Brancher le régulateur sans réglage préalable ou avec une tension trop élevée entraînera la **destruction immédiate** du microcontrôleur RP2040, de l'écran LCD et de l'ensemble de vos capteurs.

### Ajustement du regulateur

**À l’aide d’un multimètre et d’un petit tournevis plat, ajustez la tension en tournant la vis du potentiomètre (indiquée sur la photo ci-dessous).**
> 🔄 **Sens de réglage du potentiomètre :**
> * **Pour DIMINUER la tension :** Tournez la vis dans le **sens inverse des aiguilles d'une montre** (antihoraire).
> * **Pour AUGMENTER la tension :** Tournez la vis dans le **sens des aiguilles d'une montre** (horaire).
> 
> *Note : Ces potentiomètres multitours possèdent souvent une large plage de réglage initiale. Il est tout à fait normal de devoir effectuer plusieurs tours complets (parfois plus de 10 à 15 tours) avant de voir la tension commencer à varier sur votre multimètre. Procédez par petits gestes une fois proche des 5 V.*

<p align="center">
<img width="569" height="371" alt="image" src="https://github.com/user-attachments/assets/10494b81-9cd7-41e0-a7ae-1cd8d28e3c3e" />
</p>


