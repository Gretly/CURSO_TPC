import multiprocessing
import time

# Semáforo para sincronización
semaphore = multiprocessing.Semaphore(0)

# Función para imprimir números pares
def imprime_pares():
    for i in range(2, 10, 2):
        print(f"Pares: {i}")
        time.sleep(1)
        semaphore.release()

# Función para imprimir números impares
def imprime_impares():
    for i in range(1, 10, 2):
        semaphore.acquire()
        print(f"Impares: {i}")
        time.sleep(1)

if __name__ == "__main__":
    # Crear dos procesos
    pares_process = multiprocessing.Process(target=imprime_pares)
    impares_process = multiprocessing.Process(target=imprime_impares)

    # Iniciar los procesos
    pares_process.start()
    impares_process.start()

    # Esperar a que ambos procesos terminen
    pares_process.join()
    impares_process.join()
