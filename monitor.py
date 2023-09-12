import threading

class MonitorContador:
    def __init__(self):
        self.contador = 0
        self.mutex = threading.Condition()  # Creamos un objeto Condition para sincronización

    def incrementar(self):
        with self.mutex:
            self.contador += 2
            print(f"Contador incrementado a {self.contador}")
            self.mutex.notify()  # Despierta a cualquier hilo que esté esperando

    def obtener_valor(self):
        with self.mutex:
            return self.contador

    def esperar_valor(self, valor_esperado):
        with self.mutex:
            while self.contador != valor_esperado:
                self.mutex.wait()  # Espera hasta que el valor sea el esperado

# Crear una instancia del monitor
monitor_contador = MonitorContador()

# Función para incrementar el contador
def incrementar_contador():
    for _ in range(8):
        monitor_contador.incrementar()

# Función para esperar hasta que el contador llegue a un valor específico
def esperar_hasta(valor_esperado):
    monitor_contador.esperar_valor(valor_esperado)
    print(f"El contador ha alcanzado el valor esperado: {valor_esperado}")

# Crear hilos
hilo1 = threading.Thread(target=incrementar_contador)
hilo2 = threading.Thread(target=esperar_hasta, args=(16,))

# Iniciar hilos
hilo1.start()
hilo2.start()

# Esperar a que ambos hilos terminen
hilo1.join()
hilo2.join()

print("Programa terminado.")
