import time
from gpiozero import PWMOutputDevice

# Configuration pour votre branchement actuel sur Raspberry Pi 3B
# Broche GPIO 16 (Correspond à la broche physique 36 du header)
BUZZER_PIN = 16

# Dictionnaire des fréquences des notes
NOTES = {
    'DO4': 262, 'RE4': 294, 'MI4': 330, 'FA4': 349, 'SOL4': 392, 'LA4': 440, 'SI4': 494,
    'DO5': 523, 'RE5': 587, 'MI5': 659, 'FA5': 698, 'SOL5': 784, 'LA5': 880, 'SI5': 988,
    'SILENCE': 0
}

# Note intermédiaire manquante ajoutée dynamiquement (comme dans votre code original)
NOTES['SIB4'] = 466

def play_mario():
    # Initialisation du buzzer avec une fréquence par défaut de 440Hz
    buzzer = PWMOutputDevice(BUZZER_PIN, active_high=True, frequency=440)
    
    # Partition du thème principal de Mario
    partition = [
        'MI5', 'MI5', 'SILENCE', 'MI5', 'SILENCE', 'DO5', 'MI5', 'SILENCE',
        'SOL5', 'SILENCE', 'SOL4', 'SILENCE',
        'DO5', 'SILENCE', 'SOL4', 'SILENCE', 'MI4', 'SILENCE',
        'LA4', 'SILENCE', 'SI4', 'SILENCE', 'SIB4', 'LA4', 'SILENCE',
        'SOL4', 'MI5', 'SOL5', 'LA5', 'SILENCE', 'FA5', 'SOL5',
        'SILENCE', 'MI5', 'SILENCE', 'DO5', 'RE5', 'SI4'
    ]
    
    # Durées correspondantes (en secondes)
    tempos = [
        0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12,
        0.12, 0.36, 0.12, 0.36,
        0.18, 0.18, 0.18, 0.18, 0.18, 0.18,
        0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12,
        0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12,
        0.12, 0.12, 0.12, 0.12, 0.12, 0.24
    ]
    
    try:
        for note, duree in zip(partition, tempos):
            frequence = NOTES[note]
            
            if frequence == 0:
                buzzer.value = 0  # Silence
                time.sleep(duree)
            else:
                buzzer.frequency = frequence
                # En MicroPython, le max de duty_u16 est 65535. Votre valeur 1500 représentait environ 2.3% de puissance.
                # En gpiozero, la valeur est un float entre 0.0 (0%) et 1.0 (100%). On applique donc ~0.02.
                buzzer.value = 0.02  
                time.sleep(duree)
                
            # Micro-pause obligatoire pour détacher les notes identiques qui se suivent
            buzzer.value = 0
            time.sleep(0.03)
            
    finally:
        # Fermeture et libération propre de la broche GPIO après la mélodie
        buzzer.close()

print("Démarrage de la boucle Mario sur le Raspberry Pi... (Appuyez sur Ctrl+C pour quitter)")

# Joue le thème en boucle toutes les 6 secondes
try:
    while True:
        play_mario()
        time.sleep(6)
except KeyboardInterrupt:
    print("\nProgramme arrêté proprement.")
