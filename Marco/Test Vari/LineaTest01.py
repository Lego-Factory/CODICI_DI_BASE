from buildhat import *
import time
#librerie da importare sempre

#RESET PUSHER
motor = Motor ("C") #CONTROLLARE SE PORTA C
#metto il motore nella posizione 0

#Creare funzione che controlla posizione del motore e lo porta a 0 e poi lo pusha a +270
def home():
    motor.run_to_position(0,50) #resetto la posizione a velocità 50
    motor.run_for_degrees(-270,50) #-270° va avanti a velocità 50



##def push():
    ##motor.run_for_degrees(270,50) #+270° va indietro a velocità 50
    ##motor.run_for_degrees(-270,50) #-270° va avanti a velocità 50
    ##motor.run_to_position(0,50) #resetto la posizione a velocità 50
    ##motor.run_for_degrees(270,50) #+270° va indietro a velocità 50
    ##time.sleep(1)  #CONTROLLARE COSA FA
    

#AVVIO MOTORE
conveior = Motor ("D") #CONTROLLARE SE PORTA D
#metto il motore nella posizione 0
def Motorun():
    conveior.start(-50) #il motore parte a velocità 50 in direzione negativa
    #time.sleep(200) #il motore va per 120 sec
    
#AVVIO PUSHER
#motor = Motor ("C") #CONTROLLARE SE PORTA D
#metto il motore nella posizione 0
def pushome():
    motor.run_for_degrees(270,60) #+270° va indietro a velocità 60
    time.sleep(1)
    motor.run_for_degrees(-270,60) #-270° va avanti a velocità 60
    time.sleep(1)
    
#SPEGNIMENTO MOTORE    
def Motorstop():
    conveior.stop (-50) #il motore parte a velocità 50 in direzione negativa
    #time.sleep(200) #il motore va per 120 sec
     
if __name__ == "__main__": #richiama ed avvia la funzione
    home()
    Motorun()
    pushome()
    Motorstop()
