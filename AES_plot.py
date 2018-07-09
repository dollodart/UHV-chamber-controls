import matplotlib.pyplot as plt
import datetime
import csv
from time import sleep

now=datetime.datetime.now()
time_stamp=str(now.year) +'-'+ str(now.month) +'-'+ str(now.day) +'-'+ str(now.hour)
time_plot_update=4 #seconds
num_items=200

f, axarr = plt.subplots(2, sharex=True)
plt.xlabel('Time (s)')
axarr[0].set_title('Electron Beam Energy (eV)')
axarr[1].set_title('Counts')
f.subplots_adjust(hspace=0.3)

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
    axarr[0].plot(time_lst,AESx_lst)
    axarr[1].plot(time_lst,AESy_lst)
    plt.pause(time_plot_update)
    sleep(time_plot_update)
