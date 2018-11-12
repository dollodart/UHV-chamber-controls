import matplotlib.pyplot as plt
from drawnow import drawnow, figure
import datetime
import csv
import numpy as np
from time import sleep

now=datetime.datetime.now()
time_stamp=str(now.year) +'-'+ str(now.month) +'-'+ str(now.day) +'-'+ str(now.hour)
time_plot_update=2.
num_items=30

plotQ=True
AESx_lst=[]
AESy_lst=[]

def draw_figs():
    f, axarr = plt.subplots(2, sharex=True)
    plt.xlabel('Time (s)')
    ax1,ax2=axarr
    f.subplots_adjust(hspace=0.3)
    ax1.set_title('Electron Beam Energy (eV)')
    ax2.set_title('Counts')
    ax1.plot(time_lst,AESx_lst,'bo-')
    ax2.plot(time_lst,AESy_lst,'bo-')

    plt.figure()
    plt.xlabel('Counts')
    plt.ylabel('Electron Beam Energy (eV)')
    plt.plot(AESx_lst,AESy_lst,'bo-')

    plt.show()

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
    with open('out/AES_hist-'+time_stamp,'r') as AES_csv:
        AES_reader=csv.reader(AES_csv)
        for line in AES_reader:
            time,AESx,AESy=line
            time_lst.append(float(time))
            AESx_lst.append(float(AESx))
            AESy_lst.append(float(AESy))

    try:
        time_lst=time_lst[-num_items:]
        AESx_lst=AESx_lst[-num_items:]
        AESy_lst=AESy_lst[-num_items:]
    except IndexError:
        pass

    if len(time_lst) > num_items:
        time_lst=time_lst[-num_items:]
        AESx_lst=AESx_lst[-num_items:]
        AESy_lst=AESy_lst[-num_items:]
    drawnow(draw_figs)
    sleep(time_plot_update)
