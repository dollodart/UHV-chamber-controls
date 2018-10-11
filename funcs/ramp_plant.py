import u12
import sys
from time import sleep
sys.path.insert(0, '/home/egs/UHV-chamber-controls/funcs')
from funcs import PGA_auto
import csv

d1=u12.U12(serialNumber=100054654)
d2=u12.U12(serialNumber=100035035)

Vhist=[]
Thist=[]
v=0.0
with open('ramp_history.csv','w') as out_file:
    writer=csv.writer(out_file)
    while v < 0.5: #0.5*6.5=3.25 maximum voltage
        v+=0.00875
        vPS=v*6.5
        d1.eAnalogOut(analogOut0=v,analogOut1=0)
        a=0
        while a < 15:
            read=PGA_auto(d2,10)
            T=(read-1.25)/0.005
            if T > 200.:
                d1.eAnalogOut(analogOut0=0.,analogOut1=0.)
                break
                print('run-away aborted')
            print(vPS,T)
            writer.writerow([T,vPS])
            sleep(1)
            a+=1
d1.eAnalogOut(analogOut0=0.,analogOut1=0.)
