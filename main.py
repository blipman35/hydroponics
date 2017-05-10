#This project is creating a python script that uses raspberry pi to control lights
#and irrigation for hydroponic buckets.

import datetime
import time

###Define some constants that determine timing
WATER_LIGHTS_FOR = 1800 #number of seconds to irrigate and keep the lights on
WAIT_TIME = 5400 #number of seconds to wait until lights and water are turned on again

def turnon():
    print('Lights and water are on')
    #replace with giop pins

def turnoff():
    print('Lights and water are off')
    #replace with giop pins

while True:

    current_time = datetime.datetime.now() #sets the current time to a variable

    turnon() #turns on the water and light
    time.sleep(WATER_LIGHTS_FOR) #Waits specified amount of time

    turnoff() #turns off the water and light
    time.sleep(WATER_LIGHTS_FOR) #Waits specified amount of time
