import random
import threading
import time
import logging
logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

#Genero los semáforos que limitan a uno cada tipo de compra
semaforoCaja = threading.Semaphore(1) 
semaforoTelefono = threading.Semaphore(1)
semaforoApp = threading.Semaphore(1)
#Semáforo del repartidor que inicializa en cero para que no pueda entragar hasta que no esté el pedido
semaforoRepartidor = threading.Semaphore(0)


def compradorPorTelefono(): # Agente que agrega el papel
    
    while True:
        semaforoTelefono.acquire()
        logging.info(f'Haciendo el pedido')
        time.sleep(random.randint(3,6))
        semaforoTelefono.release()
        semaforoRepartidor.release()

def compradorPorCaja(): # Agente que agrega el fósforo
    
    while True:
        semaforoCaja.acquire()   
        logging.info(f'Haciendo el pedido')
        time.sleep(random.randint(3,6))
        semaforoCaja.release()
        semaforoRepartidor.release()

def compradorPorApp(): # Agente que agrega el tabaco
    
    while True:
        semaforoApp.acquire() 
        logging.info(f'Haciendo el pedido')
        time.sleep(random.randint(3,6))
        semaforoApp.release()
        semaforoRepartidor.release()


def repartidor():
    while True:
        
        semaforoRepartidor.acquire()
        logging.info(f"Entregando pedido....")
        time.sleep(random.randint(3,6))
            
       



compraTelefonica = threading.Thread(target=compradorPorTelefono ,name= "compraTelefonica")
compraPorCaja = threading.Thread(target=compradorPorCaja ,name= "compraPorCaja")
compraPorApp = threading.Thread(target=compradorPorApp ,name="compraPorApp")

repartidor = threading.Thread(target=repartidor ,name="Repartidor")


compraTelefonica.start()
compraPorCaja.start()
compraPorApp.start()
repartidor.start()
