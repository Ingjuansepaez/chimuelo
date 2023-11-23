#!/usr/bin/env python3

import serial
import time

def parse_serial_data(serial_line):
    # Aquí debes implementar la lógica para analizar los datos según el formato de tu sensor
    # Esto es un ejemplo básico y puede necesitar ajustes según el protocolo del sensor
    data = serial_line.decode('utf-8').strip()
    return data

# Configura el puerto serial (ajusta el nombre del puerto según tu configuración)
ser = serial.Serial('/dev/ttyACM0', 115200)

# Espera a que el puerto serial esté listo
time.sleep(2)

while True:
    try:
        # Lee una línea de datos desde el sensor
        line = ser.readline()

        # Analiza los datos
        sensor_data = parse_serial_data(line)

        # Divide los datos en las componentes
        components = sensor_data.split(',')

        # Imprime los datos del sensor de forma ordenada con etiquetas
        print("Datos del sensor 9DoF IMU:")
        print("Aceleración lineal en el eje X:", components[0])
        print("Aceleración lineal en el eje Y:", components[1])
        print("Aceleración lineal en el eje Z:", components[2])
        print("Velocidad angular alrededor del eje X (roll):", components[3])
        print("Velocidad angular alrededor del eje Y (pitch):", components[4])
        print("Velocidad angular alrededor del eje Z (yaw):", components[5])
        print("Campo magnético en el eje X:", components[6])
        print("Campo magnético en el eje Y:", components[7])
        print("Campo magnético en el eje Z:", components[8])

        # Pausa para evitar lecturas demasiado rápidas
        time.sleep(0.1)

    except KeyboardInterrupt:
        # Manejo de interrupción por teclado (Ctrl+C)
        print("Interrupción por teclado. Saliendo...")
        break

    except Exception as e:
        # Manejo de otras excepciones
        print("Error:", e)

# Cierra el puerto serial al salir
ser.close()
