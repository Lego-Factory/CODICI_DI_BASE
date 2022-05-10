from buildhat import *
import time
#librerie da importare sempre

#seleziono i motori
#la posizione 0 è tutto fuori quindi -270°
#torno indietro, resetto la posizione e torno a -270°
motor = Motor ("C") #CONTROLLARE SE PORTA D
#metto il motore nella posizione 0
def pushome():
    motor.run_for_degrees(-270,60) #-270° va avanti a velocità 60
    time.sleep(1)
    motor.run_for_degrees(270,60) #+270° va indietro a velocità 60
    motor.run_to_position(0,50) #resetto la posizione a velocità 50
    time.sleep(2)
    motor.run_for_degrees(-270,60) #-270° va avanti a velocità 60
    time.sleep(1)
     
if __name__ == "__main__": #richiama ed avvia la funzione
    pushome()