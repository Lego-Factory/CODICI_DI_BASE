from buildhat import *
import time
#librerie da importare sempre

#seleziono i motori

motor = Motor ("D") #CONTROLLARE SE PORTA D
#metto il motore nella posizione 0
def Motorun():
    motor.start(-50) #il motore parte a velocità 50 in direzione negativa
    time.sleep(120) #il motore va per 120 sec
    
    
if __name__ == "__main__": #richiama ed avvia la funzione
    Motorun()
 
