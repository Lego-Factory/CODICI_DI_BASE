from buildhat import *
import time
#librerie da importare sempre

#seleziono i motori

motor = Motor ("C") #CONTROLLARE SE PORTA D
#metto il motore nella posizione 0
def push():
    motor.run_for_degrees(-270,50) #-270° va avanti a velocità 50
    motor.run_for_degrees(270,50) #+270° va indietro a velocità 50
    motor.run_to_position(0,50) #resetto la posizione a velocità 50
    time.sleep(1)  #CONTROLLARE COSA FA
    
if __name__ == "__main__": #richiama ed avvia la funzione
    push()