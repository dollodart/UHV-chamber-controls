import matplotlib.pyplot as plt
import datetime
import csv
import numpy as np
from time import sleep
#in order for the updates to happen, a different backend such as 'wx' has to be used, but there are version incompatibilities
plt.switch_backend('Qt4Agg')

plt.ion()
now=datetime.datetime.now()
time_stamp=str(now.year) +'-'+ str(now.month) +'-'+ str(now.day) +'-'+ str(now.hour)
time_plot_update=4 #seconds
num_items=20

f, axarr = plt.subplots(2, sharex=True)
ax1,ax2=axarr

plt.xlabel('Time (s)')
ax1.set_title('Electron Beam Energy (eV)')
ax2.set_title('Counts')
f.subplots_adjust(hspace=0.3)

plotQ=True
lineAESx,=ax1.plot([],[],lw=2)
lineAESy,=ax2.plot([],[],lw=2)

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
            time_lst.append(float(time))
            AESx_lst.append(float(AESx))
            AESy_lst.append(float(AESy))
    AES_hist.close()
    try:
        time_lst=time_lst[-num_items:]
        AESx_lst=AESx_lst[-num_items:]
        AESy_lst=AESy_lst[-num_items:]
    except:
        pass
    if len(time_lst) < num_items:
        lineAESx.set_data(time_lst,AESx_lst)
        lineAESy.set_data(time_lst,AESy_lst)
    else:
        t_time_lst=time_lst[-num_items:]
        time_adj=np.array(t_time_lst)+(time_lst[-1] -time_lst[-num_items]) #broadcast initial time
        t_AESx_lst=AESx_lst[-num_items:]
        t_AESy_lst=AESy_lst[-num_items:]
        ax1.set_xlim(t_time_lst[0],t_time_lst[-1])
        ax2.set_xlim(t_time_lst[0],t_time_lst[-1])
        lineAESx.set_data(t_time_lst,t_AESx_lst)
        lineAESy.set_data(t_time_lst,t_AESy_lst)
    f.canvas.draw()
    f.canvas.flush_events()
    sleep(time_plot_update)
