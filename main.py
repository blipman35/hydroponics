import datetime
import time

while True:

    current_time = datetime.datetime.now()

    if current_time.hour % 2 == 0:
        print('even hour!')
