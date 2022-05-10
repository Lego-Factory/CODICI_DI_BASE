from buildhat import *
import time
#librerie da importare sempre

pusher = Motor ("C")
conveyor = Motor ("D")
sensor = ColorSensor ("B")



#controllo posizione PUSHER

def homing ():
    
    position = pusher.get_aposition()

    if position >=85 and position <=95:
        pusher.run_for_degrees(270,50) #-270° va avanti a velocità 50
        pusher.run_to_position(0,50) #resetto la posizione a velocità 50
    else:
            pusher.run_to_position(0,50) #resetto la posizione a velocità 50
    pusher.run_for_degrees(-270,50)

def pushing ():
     pusher.run_for_degrees(270,30) #-270° va avanti a velocità 50
     pusher.run_to_position(0,30) #resetto la posizione a velocità 50
     pusher.run_for_degrees(-270,30)
    
    
def startconveyor():
    conveyor.start(-50) #il motore parte a velocità 50 in direzione negativa
    
def stopconveyor():
    conveyor.stop()
  
        
if __name__ == "__main__": #richiama ed avvia la funzione
    homing()
    startconveyor()
    i=0
    while True:
        pallet=sensor.get_reflected_light()
        if pallet >= 30:
            pushing ()
        if i >= 600:
            break
        i+=1
        time.sleep(0.1)
  
    stopconveyor()    
        