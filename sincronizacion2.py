import threading

# Variable compartida
contador = 0

# Definición de un mutex para sincronizar el acceso a la variable contador
mutex = threading.Lock()

# Función que incrementa el contador y muestra un mensaje
def incrementa_contador():
    global contador
    for _ in range(4):
        # Adquiere el mutex antes de modificar la variable compartida
        mutex.acquire()
        contador += 2
        print(f"Hilo {threading.current_thread().name}: Contador = {contador}")
        # Libera el mutex después de modificar la variable compartida
        mutex.release()

# Creación de dos hilos
hilo1 = threading.Thread(target=incrementa_contador)
hilo2 = threading.Thread(target=incrementa_contador)
hilo3 = threading.Thread(target=incrementa_contador)
hilo4 = threading.Thread(target=incrementa_contador)

# Inicio de los hilos
hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()

# Espera a que ambos hilos terminen
hilo1.join()
hilo2.join()
hilo3.join()
hilo4.join()

print("Fin del programa.")
