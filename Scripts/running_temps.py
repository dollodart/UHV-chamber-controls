import u12
import sys
import time
sys.path.insert(0, '/home/albert/Documents/Albert Work/Scripts')
from funcs import PID
from thermocouple import temperature_read
import matplotlib.pyplot as plt
import pylab as pylab
import numpy as np

d=u12.U12()
i=0
max=1000000
frequency=1
t_init=temperature_read(d)
t_min=t_init
t_max=t_init
temps=[]
sum=0
k_5000=[]
k=j=0
k_avg=j_avg=0
j_5000=[]
while i<max:
    t=temperature_read(d)
    temps.append(t)
    if i>5000:
        k_5000=temps[i-5000:]
        k_avg=np.average(k_5000)
        k+=1
    if k>5000:
        j_5000=k_5000[:]
        j_avg=k_avg
    sum+=t
    if i%100==0:
        print t
    # time.sleep(frequency)
    if t>t_max:
        t_max=t
    if t<t_min:
        t_min=t
    try:
        i+=1
    except KeyboardInterrupt:
        avg=sum/max
        print avg
        print t_max
        print t_min
        x_vals=range(max)
        plt.plot(x_vals, temps)
        plt.xlabel("Measurments")
        plt.ylabel("Temperatures")
        plt.tight_layout()
        plt.show()
        check=input("continue? press enter for yes, all else for no")
        if check=='\n':
            i=0
            temps=[]
            sum=0
            continue
        else:
            break
if i==max:
    avg=sum/max
    print avg
    print t_max
    print t_min
    x_vals=range(max)
    plt.plot(x_vals, temps)
    plt.xlabel("Measurments")
    plt.ylabel("Temperatures")
    plt.tight_layout()
    plt.show()