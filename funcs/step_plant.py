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
with open('step_history.csv','w') as out_file:
    writer=csv.writer(out_file)
    o=0
    v=0.5
    d1.eAnalogOut(analogOut0=v,analogOut1=0)
    while o < 100:
        read=PGA_auto(d2,10)
        T=(read-1.25)/0.005
        vPS=v*6.5
        print(vPS,T)
        writer.writerow([T,vPS])
        sleep(1)
d1.eAnalogOut(analogOut0=0,analogOut1=0)
