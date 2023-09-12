import time
import threading

#CONCURRENCIA: este programa realiza tres tareas a la vez, codificar, responder correos, responder llamada

def codificar():
    time.sleep(4)

    print(f'ESTOY PROGRAMANDO')

def responder_correos():
    time.sleep(4)

    print(f'REVISO MI WHATSAPP')

def responder_llamada():
    time.sleep(4)

    print(f'CONTESTO UNA LLAMADA')


threading.Thread(target=codificar).start()
threading.Thread(target=responder_correos).start()
threading.Thread(target=responder_llamada).start()