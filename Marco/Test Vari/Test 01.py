from buildhat import *
import time
#librerie da importare sempre

#seleziono i motori

motor = Motor ("A") #CONTROLLARE SE PORTA A
#metto il motore nella posizione 0
def push ():
    motor.run_for_degrees(-270,50) #-270° va avanti a velocità 50
    motor.run_for_degrees(270,50) #+270° va indietro a velocità 50
    motor.run_to_position(0,50) #resetto la posizione a velocità 50
    time.sleep(1)  #CONTROLLARE COSA FA
    
sensor = Sensor('B') #CONTROLLARE SE PORTA b
def sensor
while True:


# uncomment to test lines of color sensor

# while True:
#     #print("Reflected" , csensor.get_reflected_light() )
#     #print("Color", csensor.get_color() )
#     #print("RGBI", csensor.get_color_rgbi() )

