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

def write_to_csv(row, name, read):
    ''' data order=[times,resistance,amps,volts,power,temps, sstemps, pressures]'''
    file_temp = open(name,read)
    with file_temp as temp_csv:
        temp_writer=csv.writer(temp_csv)
        temp_writer.writerow(row)
        # temp_writer.writerow([str(times),str(amps),str(volts),str(power),str(temps), str(pressures)])
    file_temp.close()
    return
        

d=u12.U12()

now=datetime.datetime.now()
time_stamp=str(now.year) +'-'+ str(now.month) +'-'+ str(now.day) +'-'+ str(now.hour)

iter= 2
time_length= 5000
sstemp=0
temps=["Temps"]
sstemps=["SSTemps"]
times=["Times"]
resistances=["Resistances"]
amps=["Amps"]
volts=["Volts"]
power=["Power"]
pressures=["Pressures"]
data=[times,amps,volts,power,temps, pressures]

file_new=input("Append File or Create New: 2=New/Rewrite 1=New w/ Descriptor, 0=Append -> ")

if file_new==1:
        descriptor=input("File Descriptor: (text must have quotes) ")
        file_name='power_temp-' + time_stamp + "_" + str(descriptor)
        read_write='a'
        power_temp = open(file_name,read_write)
elif file_new==0:
    file_name='power_temp-' + time_stamp
    read_write='a'
    
else:
    file_name='power_temp-' + time_stamp
    read_write='w'
    power_temp = open(file_name,read_write)    
write_to_csv(data, file_name, read_write)

voltage=input("Initial volts: ")
amperage=input("Initial amps: ")
resistance=input("Initial Resistance: ")
initial=time()
k=0
for i in range(time_length/iter):
    resistances.append(resistance)
    meas_temp=temperature_read(d)
    temps.append(meas_temp)
    meas_pressure=pressure_read(d, time=0)
    pressures.append(meas_pressure)
    current_t=time()
    actual=current_t-initial
    times.append(actual)
    sstemps.append(sstemp)
    amps.append(amperage)
    volts.append(voltage)
    calc_power=amperage*voltage
    power.append(calc_power)
    data_row=[actual,resistance,amperage, voltage, calc_power, meas_temp,sstemp, meas_pressure]
    write_to_csv(data_row,file_name, read_write)
    if(k%10==0):
        print("Running Temp: " + str(meas_temp) + " deg C")
    k+=1
    try:
        sleep(iter)
    except KeyboardInterrupt:
        sstemp=input("Steady State Temperature: ")
        continue_check = input("\n Continue? 1=YES, 0=NO -> ")
        if continue_check:
            voltage=input("New Voltage: ")
            amperage=input("New Amps: ")
        else:
            break

plot_choice=input("Plot Desired: 0= Temp-Power, 1=Temp-Time 2=Pressures-Time, 3=Skip Plot Generation-> ")
if plot_choice==1:
    plt.plot(times,temps)
    plt.xlabel('Times in Seconds')
    plt.ylabel('Temperature in deg. C')
    plt.tight_layout()
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