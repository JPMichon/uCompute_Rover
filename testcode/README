# Les exemples de code

# 🧪 Validation de la polarité et du sens de rotation des moteurs

Ce script de test MicroPython permet de **valider de manière empirique** que vos 4 moteurs CC (2 par côté) sont câblés et connectés dans la bonne direction. Il utilise l'écran OLED local et les boutons de navigation analogiques du module uCompute pour activer chaque côté de manière indépendante.

## 📋 Prérequis matériels
* Le **uCompute Rover** entièrement assemblé mécaniquement.
* Les modules **DRV8833** insérés et les moteurs connectés.
* L'écran **OLED SSD1306** et le capteur de puissance **INA219** branchés.
* L'alimentation active (batteries) pour fournir la puissance aux moteurs.

---

## 🚀 Procédure de test et validation

1. **Préparation :** Placez le Rover sur un support (comme une cale ou une boîte de rangement) afin que **les 4 roues ne touchent pas le sol**. Cela évitera que le robot ne s'échappe ou ne chute de votre table de travail.
2. **Démarrage :** Allumez le robot et lancez le script. L'écran affiche un message d'accueil `Rover tests - Press anykey`.
3. **Lancement :** Appuyez sur n'importe quel bouton pour démarrer le programme. L'écran affiche désormais la tension de la batterie (Volts) et le courant consommé (mA) en temps réel.

### 📐 Grille de validation des commandes

Appuyez sur les boutons physiques de votre carte uCompute pour exécuter les tests suivants :

| Bouton pressé | Action logicielle | Résultat attendu sur le Rover |
| :---: | :--- | :--- |
| ⬇️ **BOUTON BAS** *(Down)* | Active le côté **DROIT** | Les deux roues du côté **Droit** doivent tourner vers l'**AVANT**. |
| ⬆️ **BOUTON HAUT** *(Up)* | Active le côté **GAUCHE** | Les deux roues du côté **Gauche** doivent tourner vers l'**AVANT**. |
| **AUCUN** *(Relâché)* | Arrêt total | Les 4 moteurs s'arrêtent instantanément. |

---

## 🛠️ Que faire en cas de mauvaise polarité ?

Comme indiqué dans la section d'assemblage électronique, les deux moteurs d'un même côté fonctionnent en paire (câblés de manière synchrone). Le module de puissance inverse naturellement la polarité du second moteur de ce même côté en raison de son orientation mécanique inversée.

* ❌ **Si une roue tourne vers l'arrière** alors que l'autre tourne vers l'avant : Débranchez le connecteur **JST-XH** du moteur défaillant, inversez ses deux fils (polarité), puis rebranchez-le.
* ❌ **Si les deux roues d'un même côté reculent** : Inversez simplement le sens de connexion global des connecteurs entre les deux moteurs de ce côté pour rétablir la bonne marche avant.

*Une fois que l'activation du bouton HAUT et du bouton BAS fait tourner toutes vos roues de manière fluide vers l'avant, votre uCompute Rover est officiellement prêt pour son premier script de déplacement autonome !*


## 💻 Logique logicielle : Le Mode RC

Le pilotage à distance repose sur un duo de scripts MicroPython hautement optimisés, répartis entre la télécommande (**Émetteur**) et le rover (**Récepteur**). Ils exploitent le protocole de communication radio 2,4 GHz via les modules **nRF24L01+**.

### 🎮 1. La Télécommande (L'Émetteur)
Le script de la télécommande échantillonne en continu les coordonnées analogiques (X, Y) du joystick via le convertisseur analogique-numérique (ADC) du RP2040.
* **Mixage vectoriel :** Le code intègre un algorithme de mixage mathématique. L'axe Y gère la marche avant/arrière et l'axe X gère le pivot. Le programme fusionne ces deux vecteurs pour calculer instantanément la puissance requise pour le moteur gauche et le moteur droit.
* **Zone neutre (*Deadzone*) :** Une zone morte de 4 % est logiciellement configurée au centre du joystick. Cela évite que les moteurs ne sillonnent ou ne grincent lorsque la télécommande est au repos.
* **Paquet compact :** Pour maximiser la portée et la réactivité, les puissances (comprises entre -100 et +100) sont compactées dans un paquet binaire ultra-léger de deux entiers signés de 16 bits (`struct.pack("hh", p_gauche, p_droite)`) avant l'envoi radio.

### 🤖 2. Le Rover (Le Récepteur)
Afin de garantir une sécurité maximale et d'éviter les pertes de contrôle, le rover sépare ses tâches logiques grâce aux deux cœurs du RP2040 :
* **Thread de communication dédié (`_thread`) :** Un second processus indépendant tourne en boucle fermée pour écouter la radio. Dès qu'un paquet arrive, il le décompresse (`struct.unpack`) et applique immédiatement la modulation de largeur d'impulsion (PWM) aux contrôleurs de moteurs DRV8833.
* **Boucle principale (Télémétrie) :** Le cœur principal gère l'affichage en temps réel sur l'écran OLED. Il interroge en permanence le capteur **INA219** pour afficher la tension de la batterie et la consommation électrique globale en milliampères (mA), faisant office de tableau de bord de diagnostic.
