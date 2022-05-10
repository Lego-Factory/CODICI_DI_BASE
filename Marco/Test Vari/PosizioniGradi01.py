from buildhat import *
import time
#librerie da importare sempre

#controllo posizione PUSHER
motor = Motor ("C")
def position ():
    
    position = motor.get_aposition()

    if position >=85 and position <=95:
        motor.run_for_degrees(270,50) #-270° va avanti a velocità 50
        motor.run_to_position(0,50) #resetto la posizione a velocità 50
    else:
            motor.run_to_position(0,50) #resetto la posizione a velocità 50
    motor.run_for_degrees(-270,50)
        
if __name__ == "__main__": #richiama ed avvia la funzione
    position()
        