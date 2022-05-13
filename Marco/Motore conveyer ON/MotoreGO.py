'''QUESTO CODICE FA ANDARE IL MOTORE DEL CONVEYOR PER 120 SEC'''
from buildhat import *
import time
#librerie da importare sempre

#seleziono i motori

motor = Motor ("D") #CONTROLLARE SE PORTA D

def Motorun():
    motor.start(-50) #il motore parte a velocità 50 in direzione negativa
    time.sleep(120) #il motore va per 120 sec
    
    
if __name__ == "__main__": #richiama ed avvia la funzione
    Motorun()