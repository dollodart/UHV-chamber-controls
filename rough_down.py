import u12
from time import sleep
from time import time
from scipy.integrate import simps
import datetime
import csv
import numpy as np
import sys
sys.path.insert(0, '/home/egs/UHV-chamber-controls/funcs')
from funcs import PGA_auto

d1=u12.U12(serialNumber=100054654)

time_iter=0.3
time_tot=400.

status_time=20
num_iters=int(round(time_tot/time_iter))
num_status_iters=int(round(status_time/time_iter))
now=datetime.datetime.now()
time_stamp=str(now.year) +'-'+ str(now.month) +'-'+ str(now.day) +'-'+ str(now.hour)

time_lst=[]
init_time=time()
diff=1.e10

for i in range(num_iters):
    rough_pres=PGA_auto(controller=d1,channel=9)
    rough_hist=open('out/rough_hist-' + time_stamp,'a')
    with rough_hist as rough_csv:
        rough_writer=csv.writer(rough_csv)
        rough_writer.writerow([str(time()-init_time),str(rough_pres)])
    sleep(time_iter)

d1.close()
