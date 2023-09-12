import threading

# Dos recursos compartidos
recurso_a = threading.Lock()
recurso_b = threading.Lock()

# Función que representa un proceso que intenta adquirir los recursos
def proceso1():
    with recurso_a:
        print("Proceso 1 adquiere recurso A")
        # Simular una espera o procesamiento
        threading.sleep(1)
        print("Proceso 1 espera por recurso B")
        with recurso_b:
            print("Proceso 1 adquiere recurso B")

# Función que representa otro proceso que intenta adquirir los recursos en un orden inverso
def proceso2():
    with recurso_b:
        print("Proceso 2 adquiere recurso B")
        # Simular una espera o procesamiento
        threading.sleep(1)
        print("Proceso 2 espera por recurso A")
        with recurso_a:
            print("Proceso 2 adquiere recurso A")

# Crear dos hilos que ejecutan los procesos
hilo1 = threading.Thread(target=proceso1)
hilo2 = threading.Thread(target=proceso2)

# Iniciar los hilos
hilo1.start()
hilo2.start()

# Esperar a que ambos hilos terminen
hilo1.join()
hilo2.join()

print("Ambos procesos han terminado")
