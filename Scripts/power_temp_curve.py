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
from pressure import pressure_read
import matplotlib.pyplot as plt
import pylab as pylab

def write_to_csv(row, name):
    ''' data order=[times,amps,volts,power,temps, pressures]'''
    with name as temp_csv:
        temp_writer=csv.writer(temp_csv)
        temp_writer.writerow(row)
        # temp_writer.writerow([str(times),str(amps),str(volts),str(power),str(temps), str(pressures)])
    power_temp.close()
        

d=u12.U12()

now=datetime.datetime.now()
time_stamp=str(now.year) +'-'+ str(now.month) +'-'+ str(now.day) +'-'+ str(now.hour)

iter= 2
time_length= 5

temps=["Temps"]
times=["Times"]
amps=["Amps"]
volts=["Volts"]
power=["Power"]
pressures=["Pressures"]
data=[times,amps,volts,power,temps, pressures]

file_new=input("Append File or Create New: 1=New, 0=Append -> ")

if file_new:
        descriptor=input("File Descriptor: (text must have quotes) ")
        power_temp = open('power_temp-' + time_stamp + "_" + str(descriptor),'a')
else:
        power_temp = open('power_temp-' + time_stamp,'w')
write_to_csv(data, power_temp)

amperage=input("Initial amps: ")
voltage=input("Initial volts: ")
initial=time()
k=0
for i in range(time_length/iter):
    data_row=[]
    temps.append(temperature_read(d))
    pressures.append(pressure_read(d, time=0))
    current_t=time()
    actual=current_t-initial
    times.append(actual)
    amps.append(amperage)
    volts.append(voltage)
    power.append(amperage*voltage)
    try:
        sleep(iter)
    except KeyboardInterrupt:
        continue_check = input("\n Continue? 1=YES, 0=NO -> ")
        if continue_check:
            amperage=input("New Amps: ")
            voltage=input("New Voltage: ")
        else:
            break

plot_choice=input("Plot Desired: 0= Temp-Power, 1=Temp-Time 2=Pressures-Time, 3=Skip Plot Generation-> ")
if plot_choice==1:
    plt.plot(times,temps)
    plt.xlabel('Times in Seconds')
    plt.ylabel('Temperature in deg. C')
    pylab.show()
elif plot_choice==0:
    plt.plot(power,temps)
    plt.xlabel('Power in Watts')
    plt.ylabel('Temperature in deg. C')
    plt.tight_layout()
    pylab.show()
elif plot_choice==2:
    plt.plot(times,pressures)
    plt.xlabel('Time in Seconds')
    plt.ylabel('Pressures in Torr')
    plt.tight_layout()
    pylab.show()
else:
    print("No Plot")

#convert csv data into column mode
# data_rows=[]
# data=[times,amps,volts,power,temps, pressures]

# for i in range(len(times)):
#     temp=[]
#     for j in data:
#         temp.append(j[i])
#     data_rows.append(temp)