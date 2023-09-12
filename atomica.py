import multiprocessing

# Función para agregar datos a la cola (productor)
def productor(queue):
    for i in range(5):
        fruta = f"Nro. {i}"
        queue.put(fruta)
        print(f"Produciendo la fruta: {fruta}")

# Función para leer datos de la cola (consumidor)
def consumidor(queue):
    while True:
        fruta = queue.get()
        if fruta is None:
            break
        print(f"Consumiendo la fruta: {fruta}")

if __name__ == "__main__":
    # Crear una cola para la comunicación entre procesos
    queue = multiprocessing.Queue()

    # Crear procesos para el productor y el consumidor
    productor_process = multiprocessing.Process(target=productor, args=(queue,))
    consumidor_process = multiprocessing.Process(target=consumidor, args=(queue,))

    # Iniciar los procesos
    productor_process.start()
    consumidor_process.start()

    # Esperar a que el productor termine su trabajo
    productor_process.join()

    # Indicar al consumidor que ha terminado
    queue.put(None)

    # Esperar a que el consumidor termine su trabajo
    consumidor_process.join()
