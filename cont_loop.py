import u12
from time import sleep
from time import time
from scipy.integrate import simps
import datetime
import csv
import numpy as np
import sys
sys.path.insert(0, '/home/egs/UHV-chamber-controls/funcs')
from funcs import PID

d1=u12.U12(serialNumber=100054654)
d2=u12.U12(serialNumber=100035035)

time_iter=0.3
time_tot=10000
time_cont=2

status_time=20
num_iters=int(round(time_tot/time_iter))
num_status_iters=int(round(status_time/time_iter))
num_hist=int(round(time_cont/time_iter))

now=datetime.datetime.now()
time_stamp=str(now.year) +'-'+ str(now.month) +'-'+ str(now.day) +'-'+ str(now.hour)

time_lst=[]
err_lst=[0]*3
o=0
init_time=time()

for i in range(num_iters):
    #read data from device
    AESx=d2.eAnalogIn(channel=8,gain=1)['voltage'] 
    AESx*=100.
    AESx*=1.7 #gain
    AESy=d2.eAnalogIn(channel=9,gain=1)['voltage']
    PS=d1.eAnalogIn(channel=10,gain=1)['voltage']
    if PS > 10:
        d.eAnalogOut(0,0)
        print('out of safe operating range, PS voltage set to 0')
        break
    TC=d2.eAnalogIn(channel=4)['voltage'] #this signal comes from an Op-amp, that is, not differential
    PD=d1.eAnalogIn(channel=8,gain=1)['voltage']
    PDrough=d1.eAnalogIn(channel=9,gain=20)['voltage']
   
    #voltage to physical conversion
    temp=(TC-1.25)/0.005 # deg C
    pres=-2.73*PD+0.07 # microtorr
    pres_rough=1.*PDrough  # torr

    #controls
    time_lst.append(time()-init_time) #nominal time and real time may differ due to processing time
    try:
        temperature_setpoint=open('setpoints/temp.control','r')
        for line in temperature_setpoint:
            tempSP=float(line.rstrip('\n'))
        temperature_setpoint.close()
    except:
        tempSP=25 #deg C, room temperature
    try:
        manual_override=open('setpoints/PSV.control','r')
        for line in manual_override:
            PS0=float(line.rstrip('\n'))
        manual_override.close()
        if o > num_status_iters:
            print('status:manual override\n time (s), PS voltage, temperature (K), pressure (utorr)')
            print(i*time_iter,PS,temp,pres)
            o=0
        d1.eAnalogOut(PS0)
    except:
        err=tempSP-temp
        err_lst.append(err)
        response=PID(err_lst,time_iter,num_hist)
        PSto=PS0+response # adjust the current voltage by NFB
        if o > num_status_iters:
            print('status:automatic control\n time (s), PS voltage, temperature (K), pressure (utorr)')
            print(i*time_iter,PS,temp,pres)
            o=0
        d1.eAnalogOut(PSto/6.5,0) # voltage signal to voltage power supply, full scale adjustment, see calibration files

    #write out
    AES_hist=open('out/AES_hist-' + time_stamp,'a')
    cont_hist=open('out/cont_hist-' + time_stamp,'a')
    with AES_hist as AES_csv:
        AES_writer=csv.writer(AES_csv)
        AES_writer.writerow([str(i*time_iter),str(AESx),str(AESy)])
    with cont_hist as cont_csv:
        cont_writer=csv.writer(cont_csv)
        cont_writer.writerow([str(i*time_iter),str(PS),str(temp),str(pres),str(PDrough)])
    AES_hist.close()
    cont_hist.close()

    sleep(time_iter)
    o+=1

d2.close()
d1.close()
