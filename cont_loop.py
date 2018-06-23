import u12
from time import sleep
import datetime
from scipy.integrate import simps
import csv
import numpy as np

def PID(err_lst):
    kp=0.01
    ki=0.1
    kd=0.01
    P=kP*np.average(err_lst[-num_hist:])
    I=kI*np.trapz(err_lst,x=None,dx=time_iter)
    D=kD*np.average(np.gradient(err_lst,time_iter)[-num_hist:])
    return P+I+D

dCont=u12.U12(serialNumber=100054654)
dAES=u12.U12(serialNumber=100035035)

time_iter=0.3
time_tot=10000
time_cont=2

tempSP=400 # deg C
status_time=20
num_iters=int(round(time_tot/time_iter))
num_status_iters=int(round(status_time/time_iter))
num_hist=int(round(time_cont/time_iter))

now=datetime.datetime.now()
time_stamp=str(now.year) +'-'+ str(now.month) +'-'+ str(now.day) +'-'+ str(now.hour)
time_lst=[]
err_lst=[]
tempSP=25 # initialize this to desired temperature in deg C
o=0

for i in range(num_iters): #need way for user input during control loop
    #read data from device
    AESxp=dAES.eAnalogIn(0)
    AESxn=dAES.eAnalogIn(1)
    AESx=AESxp['voltage']-AESxn['voltage']
    AESyp=dAES.eAnalogIn(2)
    AESyn=dAES.eAnalogIn(3)
    AESy=AESxp['voltage']-AESxn['voltage']
    PSp=dCont.eAnalogIn(4)
    PSn=dCont.eAnalogIn(5)
    PS=PSp['voltage']-PSn['voltage']
    if PS > 10:
        d.eAnalogOut(0,0)
        print('out of safe operating range, PS voltage set to 0')
        break
    PDn=dCont.eAnalogIn(0)['voltage']
    PDp=dCont.eAnalogIn(1)['voltage']
    PD=PDp-PDn
    PDroughn=dCont.eAnalogIn(2)['voltage']
    PDroughp=dCont.eAnalogIn(3)['voltage']
    PDrough=PDroughp-PDroughn
    TC=dCont.eAnalogIn(7)['voltage']
   
    temp=(TC-1.25)/0.005 # deg C
    pres=-2.73*PD+0.07 # microtorr
    pres_rough=PDrough

    #controls
    time_lst.append(i*time_iter)
    try:
        manual_override=open('setpoints/PSV.control','r')
        for line in manual_override:
            PSto=float(line.rstrip('\n'))
        manual_override.close()
        if o > num_status_iters:
            print('status:manual override')
            print('time','PS voltage', 'temperature', 'pressure')
            print(i*time_iter,PS,temp,pres)
            o=0
    except:
        err=temp-tempSP
        err_lst.append(err)
        response=PID(err_lst)
        PSto=PS-response # adjust the current voltage by NFB
        if o > num_status_iters:
            print('status:automatic control')
            print('time','PS voltage', 'temperature', 'pressure')
            print(i*time_iter,PS,temp,pres)
            o=0
    dCont.eAnalogOut(PSto/6.5,0) # see calibration files

    #write out for plotting
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

dAES.close()
dCont.close()
