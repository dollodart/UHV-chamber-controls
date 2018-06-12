import matplotlib.pyplot as plt
import datetime
import csv
from time import sleep

now=datetime.datetime.now()
time_stamp=str(now.year) +'-'+ str(now.month) +'-'+ str(now.day) +'-'+ str(now.hour)
time_plot_update=4#seconds
num_items=200

fig=plt.figure()
plt.xlabel('Beam Energy in eV')
plt.ylabel('Auger Signal')

ax=fig.add_subplot(1,1,1)

plotQ=True
while plotQ:
    try:
        do_plot=open('do_plot.control','r')
        for line in manual_override:
            plotQ=bool(line.rstrip('\n'))

    except:
        plotQ=False

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

    if len(AESx_lst) < num_items:
        ax.plot(AESx_lst,AESy_lst)
    else:
        ax.plot(AESx_lst[-num_items:],AESy_lst[-num_items:])
    plt.pause(time_plot_update)
    sleep(time_plot_update)
