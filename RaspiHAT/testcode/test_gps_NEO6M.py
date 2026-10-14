import serial
import sys

# Le NEO-6M communique par défaut à 9600 bauds
SERIAL_PORT = "/dev/serial0"
BAUD_RATE = 9600

print(f"--- Connexion au GPS NEO-6M sur {SERIAL_PORT} ({BAUD_RATE} bauds) ---")
print("Appuyez sur Ctrl+C pour quitter.\n")

try:
    # Ouverture du port série
    ser = serial.Serial(SERIAL_PORT, baudrate=BAUD_RATE, timeout=1)
    
    while True:
        # Lecture d'une ligne complète se terminant par \n
        if ser.in_waiting > 0:
            ligne = ser.readline().decode('utf-8', errors='ignore').strip()
            
            # Si la ligne contient des données NMEA valides (commencent par $)
            if ligne.startswith('$'):
                print(ligne)

except KeyboardInterrupt:
    print("\nArrêt du test par l'utilisateur.")
except serial.SerialException as e:
    print(f"\nErreur de port série : {e}")
    print("Vérifiez vos branchements et l'activation de l'UART.")
except Exception as e:
    print(f"\nUne erreur est survenue : {e}")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Port série fermé.")
