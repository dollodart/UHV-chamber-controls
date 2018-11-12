import matplotlib.pyplot as plt
from drawnow import drawnow, figure
import datetime
import csv
import numpy as np
from time import sleep

now=datetime.datetime.now()
time_stamp=str(now.year) +'-'+ str(now.month) +'-'+ str(now.day) +'-'+ str(now.hour)
time_plot_update=4 #seconds
num_items=20

plt.xlabel('Electron Beam Energy (eV)')
plt.ylabel('Counts')

plotQ=True
while plotQ:
    try:
        do_plot=open('setpoints/do_plot.control','r')
        for line in do_plot:
            plotQ=bool(line.rstrip('\n'))
        do_plot.close()
    except:
        plotQ=False

    time_lst=[]
    AESx_lst=[]
    AESy_lst=[]
    AES_hist=open('out/AES_hist-' + time_stamp,'r')
    with AES_hist as AES_csv:
        AES_reader=csv.reader(AES_csv)
        for line in AES_reader:
            time,AESx,AESy=line
            AESx_lst.append(float(AESx))
            AESy_lst.append(float(AESy))
    AES_hist.close()
    try:
        AESx_lst=AESx_lst[-num_items:]
        AESy_lst=AESy_lst[-num_items:]
    except:
        pass
    if len(time_lst) < num_items:
        plt.plot(AESx_lst,AESy_lst,color='k')
    else:
        t_AESx_lst=AESx_lst[-num_items:]
        t_AESy_lst=AESy_lst[-num_items:]
        plt.plot(AESx_lst,AESy_lst,'k-')
    plt.pause(time_plot_update)
    sleep(time_plot_update)
