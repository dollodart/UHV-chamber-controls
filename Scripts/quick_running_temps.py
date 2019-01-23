import u12
import sys
import time
sys.path.insert(0, '/home/albert/Documents/Albert Work/Scripts')
from funcs import PID
from thermocouple import temperature_read
import matplotlib.pyplot as plt
import pylab as pylab

d=u12.U12()
i=0
max=100
frequency=1

temps=[]
sum=0
while i<max:
    t=temperature_read(d)
    temps.append(t)
    sum+=t
    # time.sleep(frequency)
    i+=1

avg=sum/max
print avg
x_vals=range(max)
plt.plot(x_vals, temps)
plt.xlabel("Measurments")
plt.ylabel("Temperatures")
plt.tight_layout()
plt.show()