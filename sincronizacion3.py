import threading

# Variable compartida para sincronización
variable_compartida = 0

# Semáforo para controlar el acceso a la variable compartida
semaforo = threading.Semaphore(1)

# Función que incrementa la variable compartida
def incrementa_variable():
    global variable_compartida
    for _ in range(6):
        semaforo.acquire()  # Adquiere el semáforo para acceso exclusivo
        variable_compartida += 4
        print(f"Hilo {threading.current_thread().name}: Variable compartida = {variable_compartida}")
        semaforo.release()  # Libera el semáforo

# Creación de dos hilos
hilo1 = threading.Thread(target=incrementa_variable, name="Hilo 1")
hilo2 = threading.Thread(target=incrementa_variable, name="Hilo 2")

# Inicio de los hilos
hilo1.start()
hilo2.start()

# Espera a que ambos hilos terminen
hilo1.join()
hilo2.join()

print("Programa terminado.")
