import threading
import random
import time

# Tamaño del búfer
TAMANO_BUFFER = 5

# Búfer compartido
buffer = []
mutex = threading.Semaphore(1)  # Semáforo para exclusión mutua
espacios_vacios = threading.Semaphore(TAMANO_BUFFER)  # Semáforo para espacios vacíos en el búfer
elementos_ocupados = threading.Semaphore(0)  # Semáforo para elementos ocupados en el búfer

# Función del productor
def productor():
    for _ in range(10):
        item = random.randint(1, 100)
        espacios_vacios.acquire()  # Esperar a que haya espacio en el búfer
        mutex.acquire()  # Entrar en la sección crítica
        buffer.append(item)
        print(f"Productor produjo {item}. Buffer: {buffer}")
        mutex.release()  # Salir de la sección crítica
        elementos_ocupados.release()  # Avisar que hay elementos ocupados

# Función del consumidor
def consumidor():
    for _ in range(10):
        elementos_ocupados.acquire()  # Esperar a que haya elementos ocupados en el búfer
        mutex.acquire()  # Entrar en la sección crítica
        item = buffer.pop(0)
        print(f"Consumidor consumió {item}. Buffer: {buffer}")
        mutex.release()  # Salir de la sección crítica
        espacios_vacios.release()  # Avisar que hay espacio vacío

# Creación de hilos productor y consumidor
hilo_productor = threading.Thread(target=productor)
hilo_consumidor = threading.Thread(target=consumidor)

# Inicio de los hilos
hilo_productor.start()
hilo_consumidor.start()

# Esperar a que ambos hilos terminen
hilo_productor.join()
hilo_consumidor.join()

print("Programa terminado.")
