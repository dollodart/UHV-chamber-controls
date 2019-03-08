import u12
import time
import sys
sys.path.insert(0, '/home/albert/Documents/Albert Work/Scripts')
from thermocouple import temperature_read

d=u12.U12()
i=0
max=1000000
frequency=1
while i<max:
    t=temperature_read(d)
    if i%100==0:
        print t
    # time.sleep(frequency)
    i+=1
    if i==max:
        check=input("continue? press enter for yes, all else for no")
        if check=='':
            i=0
            continue
        else:
            break