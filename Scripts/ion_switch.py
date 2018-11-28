
import u12
from time import sleep
from time import time
import sys
sys.path.insert(0, '/home/albert/Documents/Albert Work/Scripts')
from pressure import pressure_read

d=u12.U12()

d.eDigitalOut(0,1)
d.eDigitalOut(1,1)
p=pressure_read(d,5)

d.eDigitalOut(0,0)
d.eDigitalOut(1,0)

print("Pressure: " + str(p))
d.close()
