import matplotlib.pyplot as plt
import datetime
import numpy as np
from time import sleep
import csv

now=datetime.datetime.now()
time_stamp=str(now.year) +'-'+ str(now.month) +'-'+ str(now.day) +'-'+ str(now.hour)
plot_window=20 #seconds
time_plot_update=4#seconds
num_items=20 #the plot command doesn't have any knowledge about time (other than the read-file to be current). If a specific time window is desired, let num_items=int(round(plot_window/time_iter))

f, axarr = plt.subplots(3, sharex=True)
plt.xlabel('Time (s)')
axarr[0].set_title('Power Supply Potential (V)')
axarr[1].set_title('Temperature (deg C)')
axarr[2].set_title('Pressure (1e-7 torr)')
f.subplots_adjust(hspace=0.3)
#plt.ylabel('Temperature (deg C)')
#plt.ylabel('Pressure (1e-7 torr)')

#ax1=fig1.add_subplot(1,1,1)
#ax2=fig2.add_subplot(1,1,1)
#ax3=fig3.add_subplot(1,1,1)
plotQ=True
while plotQ:
    try:
        do_plot=open('do_plot.control','r')
        for line in do_plot:
            plotQ=bool(line.rstrip('\n'))

    except:
        plotQ=False
    time_lst=[]
    PS_lst=[]
    temp_lst=[]
    pres_lst=[]
    cont_hist=open('out/cont_hist-' + time_stamp,'r')
    with cont_hist as csvfile:
        csvobject=csv.reader(csvfile)
        for line in csvobject:
            time,PS,temp,pres=line
            time_lst.append(float(time))
            PS_lst.append(float(PS))
            temp_lst.append(float(temp))
            pres_lst.append(float(pres))
    cont_hist.close()
    if len(time_lst) < num_items:
        ax1.plot(time_lst,PS_lst)
        ax2.plot(time_lst,temp_lst)
        ax3.plot(time_lst,pres_lst)
    else:
        t_time_lst=time_lst[-num_items:]
        time_adj=np.array(t_time_lst)+(time_lst[-1] -time_lst[-num_items]) #broadcast initial time
        t_PS_lst=PS_lst[-num_items:]
        t_temp_lst=temp_lst[-num_items:]
        t_pres_lst=pres_lst[-num_items:]
        axarr[0].plot(t_time_lst,t_PS_lst)
        axarr[1].plot(t_time_lst,t_temp_lst)
        axarr[2].plot(t_time_lst,t_pres_lst)
    sleep(time_plot_update)
    plt.pause(time_plot_update)
