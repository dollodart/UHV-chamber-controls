import u12
import sys
sys.path.insert(0, '/home/albert/Documents/Albert Work/Scripts')
from funcs import PID
from thermocouple import temperature_read

d=u12.U12()

t=temperature_read(d)

print("Temperature: " + str(t))
