import threading
import time

# Función que simula un trabajo que tarda un tiempo aleatorio
def trabajo(id):
    print(f"Hilo {id} inició.")
    time.sleep(4)  # Simula un trabajo que toma 1 segundo
    print(f"Hilo {id} terminó.")

# Creación de hilos con diferentes prioridades
hilo1 = threading.Thread(target=trabajo, args=(1,), name="Hilo 1", daemon=True)
hilo2 = threading.Thread(target=trabajo, args=(2,), name="Hilo 2", daemon=True)
hilo3 = threading.Thread(target=trabajo, args=(3,), name="Hilo 3", daemon=True)

# Establecer prioridades (por defecto, todos los hilos tienen la misma prioridad)
hilo1.priority = 1
hilo2.priority = 2
hilo3.priority = 3

# Inicio de los hilos
hilo1.start()
hilo2.start()
hilo3.start()

# Espera a que todos los hilos terminen
hilo1.join()
hilo2.join()
hilo3.join()

print("Programa terminado.")
