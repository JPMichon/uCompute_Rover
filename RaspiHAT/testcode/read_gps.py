import serial
import pynmea2
import sys

SERIAL_PORT = "/dev/serial0"
BAUD_RATE = 9600

print(f"--- Lecture GPS NEO-6M active sur {SERIAL_PORT} ---")
print("En attente du signal satellite (Fix)... Appuyez sur Ctrl+C pour quitter.\n")

try:
    ser = serial.Serial(SERIAL_PORT, baudrate=BAUD_RATE, timeout=1)
    
    while True:
        if ser.in_waiting > 0:
            # Lecture de la trame brute
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            
            # On cherche la trame GPGGA ou GPRMC qui contient la position
            if line.startswith('$GPGGA'):
                try:
                    # Décodage automatique de la trame par pynmea2
                    msg = pynmea2.parse(line)
                    
                    # Vérification du statut (0 = pas de signal, 1 ou 2 = GPS Fix valide)
                    if msg.gps_qual > 0:
                        print("\n[ DONNÉES GPS REÇUES ]")
                        print(f"Heure (UTC) : {msg.timestamp}")
                        print(f"Latitude    : {msg.latitude:.6f} {msg.lat_dir}")
                        print(f"Longitude   : {msg.longitude:.6f} {msg.lon_dir}")
                        print(f"Altitude    : {msg.altitude} {msg.altitude_units}")
                        print(f"Satellites  : {msg.num_sats}")
                    else:
                        print("Recherche de satellites en cours...", end="\r")
                        
                except pynmea2.ParseError:
                    pass

except KeyboardInterrupt:
    print("\nFin du programme.")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
