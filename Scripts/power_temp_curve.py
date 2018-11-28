import u12
from time import sleep
from time import time
import datetime
import csv
import numpy as np
import sys
#path has to be adjusted unique to each machine
#change to make look in current directory?
sys.path.insert(0, '/home/albert/Documents/Albert Work/Scripts')
from thermocouple import temperature_read
import matplotlib.pyplot as plt
import pylab as pylab

d=u12.U12()
iter= 2
time_length= 1500
initial=time()
print("check")
print(initial)
temps=[]
times=[]
for i in range(2*time_length):
    #try except catch KeyboardInterrupt
    temps.append(temperature_read(d))
    current=time()
    actual=current-initial
    times.append(actual)
    try:
        sleep(iter)
    except: KeyboardInterrupt
        

plt.plot(times,temps)
plt.xlabel('Times in Seconds')
plt.ylabel('Temperature in deg. C')
pylab.show()

# now=datetime.datetime.now()
# time_stamp=str(now.year) +'-'+ str(now.month) +'-'+ str(now.day) +'-'+ str(now.hour)

# # temp_hist = open('out/temp_hist-' + time_stamp,'a')
# # with temp_hist as temp_csv:
# #         temp_writer=csv.writer(temp_csv)
# #         temp_writer.writerow([str(i*time_iter),str(PS),str(temp),str(pres),str(PDrough)])
# # temp_hist.close()