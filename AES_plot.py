import matplotlib.pyplot as plt
from drawnow import drawnow, figure
import datetime
import csv
import numpy as np
from time import sleep

now=datetime.datetime.now()
time_stamp=str(now.year) +'-'+ str(now.month) +'-'+ str(now.day) +'-'+ str(now.hour)
time_plot_update=1.
num_items=1000

plotQ=True
AESx_lst=[]
AESy_lst=[]

def draw():
    plt.subplot(2,2,1)
    plt.plot(t,-1.*np.array(x),'bo-')
    plt.ylabel('Electron Beam Energy (eV)')
    plt.subplot(2,2,3)
    plt.ylabel('Counts (a.u.)')
    plt.xlabel('Time (s)')
    plt.plot(t,y,'bo-')
    plt.subplot(2,2,2)
    plt.plot(x,y)
    plt.xticks(np.linspace(min(x),max(x),10),
            [int(val) for val in np.round(-np.linspace(min(x),max(x),10))])
    plt.xlabel('Electron Beam Energy (eV)')
    plt.ylabel('Counts (a.u.)')

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

    if len(time_lst) > num_items:
        time_lst=time_lst[-num_items:]
        AESx_lst=AESx_lst[-num_items:]
        AESy_lst=AESy_lst[-num_items:]
    t=time_lst #short-hand references
    x=AESx_lst
    y=AESy_lst
    drawnow(draw)
    sleep(time_plot_update)
