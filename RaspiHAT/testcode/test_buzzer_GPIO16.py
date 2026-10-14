import time
from gpiozero import PWMOutputDevice

# Définition de la broche GPIO 16 (Broche physique 36)
# Un buzzer passif a besoin d'un signal PWM (fréquence) pour produire un son.
BUZZER_PIN = 16
buzzer = PWMOutputDevice(BUZZER_PIN, active_high=True, frequency=440)

def play_tone(frequency, duration):
    """Fait sonner le buzzer à une fréquence précise pendant une durée donnée."""
    if frequency == 0:
        buzzer.value = 0  # Silence
    else:
        buzzer.frequency = frequency
        buzzer.value = 0.5  # Cycle de travail (Duty Cycle) à 50%
    time.sleep(duration)
    buzzer.value = 0  # Arrêt du son après la durée

print("Début du test du buzzer passif sur GPIO 16...")

try:
    # 1. Test de tonalités successives (Bip Bip)
    print("Test de bips...")
    for _ in range(3):
        play_tone(1000, 0.2)  # Son aigu (1000 Hz) pendant 0,2 seconde
        time.sleep(0.2)       # Pause de 0,2 seconde

    time.sleep(1)

    # 2. Test de variation de fréquence (Sirène)
    print("Test de sirène (variation de fréquence)...")
    for freq in range(400, 2000, 100):
        play_tone(freq, 0.05)
    for freq in range(2000, 400, -100):
        play_tone(freq, 0.05)

    print("Test terminé avec succès !")

except KeyboardInterrupt:
    print("\nTest interrompu par l'utilisateur.")

finally:
    buzzer.close()  # Libère proprement la broche GPIO
