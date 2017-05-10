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

    current_time = datetime.datetime.now()

    turnon()
    time.sleep(WATER_LIGHTS_FOR)

    turnoff()
    time.sleep(WATER_LIGHTS_FOR)
