import u12
from time import sleep
from time import time
import sys
sys.path.insert(0, '/home/albert/Documents/Albert Work/Scripts')
from pressure import pressure_read

d=u12.U12()

#d.eAnalogOut(1, 0)
#out=d.eAnalogIn(0)

d.eDigitalOut(0,1)
pressure_read(d,10)

#out1=d.eAnalogIn(0)

d.eDigitalOut(0,0)

#out2=d.eAnalogIn(0)

print("done")

#print(out1)
#print(out2)