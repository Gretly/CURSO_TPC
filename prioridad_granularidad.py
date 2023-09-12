import threading
import time

# Función para imprimir mensajes con prioridad baja
def prioridad_baja():
    for i in range(5):
        print("Tarea de BAJA prioridad")
        time.sleep(0.1)

# Función para imprimir mensajes con prioridad media
def prioridad_media():
    for i in range(5):
        print("Tarea de MEDIA prioridad")
        time.sleep(0.2)

# Función para imprimir mensajes con alta prioridad
def prioridad_alta():
    for i in range(5):
        print("Tarea de ALTA prioridad")
        time.sleep(0.3)

# Crear hilos con diferentes prioridades
prioridad_baja_thread = threading.Thread(target=prioridad_baja)
prioridad_media_thread = threading.Thread(target=prioridad_media)
prioridad_alta_thread = threading.Thread(target=prioridad_alta)

# Asignar prioridades a los hilos
prioridad_baja_thread.daemon = True
prioridad_media_thread.daemon = True
prioridad_alta_thread.daemon = True

# Iniciar los hilos
prioridad_baja_thread.start()
prioridad_media_thread.start()
prioridad_alta_thread.start()

# Esperar a que todos los hilos terminen
prioridad_baja_thread.join()
prioridad_media_thread.join()
prioridad_alta_thread.join()

print("Todos los hilos han terminado.")
