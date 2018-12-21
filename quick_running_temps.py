import u12
import sys
import time
sys.path.insert(0, '/home/albert/Documents/Albert Work/Scripts')
from funcs import PID
from thermocouple import temperature_read

d=u12.U12()
i=0
max=100
frequency=1

while i<max:
    t=temperature_read(d)
    print("Temperature: " + str(t))
    time.sleep(frequency)
    i+=1