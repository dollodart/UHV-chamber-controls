import matplotlib.pyplot as plt
from drawnow import drawnow, figure
import datetime
import numpy as np
from time import sleep
import csv

now=datetime.datetime.now()
time_stamp=str(now.year) +'-'+ str(now.month) +'-'+ str(now.day) +'-'+ str(now.hour)
time_plot_update=1 # seconds
plot_window=20 # seconds
time_iter=0.3
num_items=int(round(plot_window/time_iter))

def draw_fig():
    f, axarr = plt.subplots(4, sharex=True)
    plt.xlabel('Time (s)')
    axarr[0].set_title('Power Supply Potential (V)')
    axarr[1].set_title('Temperature (deg C)')
    axarr[2].set_title('Pressure (1e-7 torr)')
    axarr[3].set_title('Foreline pressure (torr)')
    axarr[0].plot(time_lst,PS_lst)
    axarr[1].plot(time_lst,temp_lst)
    axarr[2].plot(time_lst,pres_lst)
    axarr[3].plot(time_lst,pres_rough_lst)
    f.subplots_adjust(hspace=0.3)
    plt.show()

plotQ=True
while plotQ:
    try:
        do_plot=open('setpoints/do_plot.control','r')
        for line in do_plot:
            plotQ=bool(line.rstrip('\n'))
    except:
        plotQ=False
    time_lst=[]
    PS_lst=[]
    temp_lst=[]
    pres_lst=[]
    pres_rough_lst=[]
    with open('out/cont_hist-'+time_stamp,'r') as csv_file:
        csv_reader=csv.reader(csv_file)
        for line in csv_reader:
            time,PS,temp,pres,pres_rough=line
            time_lst.append(float(time))
            PS_lst.append(float(PS))
            temp_lst.append(float(temp))
            pres_lst.append(float(pres))
            pres_rough_lst.append(float(pres_rough))
    if len(time_lst) > num_items:
        time_lst=time_lst[-num_items:]
        PS_lst=PS_lst[-num_items:]
        temp_lst=temp_lst[-num_items:]
        pres_lst=pres_lst[-num_items:]
        pres_rough_lst=pres_rough_lst[-num_items:]
    sleep(time_plot_update)
    drawnow(draw_fig)
