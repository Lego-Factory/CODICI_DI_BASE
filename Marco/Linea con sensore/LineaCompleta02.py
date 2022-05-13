from buildhat import *
import time
#librerie da importare sempre

#assegno una variabile

pusher = Motor ("C")
conveyor = Motor ("D")
sensor = ColorSensor ("B")

#controllo posizione PUSHER

def homing ():
    
    position = pusher.get_aposition()

    if position >=85 and position <=95: '''il pusher controlla la sua posizione
    cioè controlla se è dentro o fuori'''
        pusher.run_for_degrees(270,50) #-270° va avanti a velocità 50
        pusher.run_to_position(0,50) #resetto la posizione a velocità 50
    else:
            pusher.run_to_position(0,50) #resetto la posizione a velocità 50
    pusher.run_for_degrees(-270,50)

#muovo il pusher per spostare i pezzi
def pushing ():
     pusher.run_for_degrees(270,30) #-270° va avanti a velocità 50
     pusher.run_to_position(0,30) #resetto la posizione a velocità 50
     pusher.run_for_degrees(-270,30)
    
#facccio andare avanti il conveyor    
def startconveyor():
    conveyor.start(-50) #il motore parte a velocità 50 in direzione negativa
#stop il conveyor    
def stopconveyor():
    conveyor.stop()
  
        
if __name__ == "__main__": #richiama ed avvia la funzione
    homing()
    startconveyor()
    i=0
    while True:
        pallet=sensor.get_reflected_light()
        if pallet >= 30: #definizione riflessione luce colore pallet
            pushing ()
            '''i+=1 se metto qui conto il numero dei push e non il tempo 
            se parto da 1 come inzio ho 10 push
            '''
        if i >= 600: #numero di cicli = cercherà un pallet per 60 sec
            break
        i+=1
        time.sleep(0.1) #durata singolo ciclo
  
    stopconveyor()    
        