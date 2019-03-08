import u12
import time
import sys
import datetime
import csv
sys.path.insert(0, '/home/albert/Documents/Albert Work/Scripts')
from thermocouple import temperature_read
from pressure import pressure_read

def write_to_csv(row, name):
    ''' data order=[times, temps, pressures]'''
    file_temp = open(name,'a')
    with file_temp as temp_csv:
        temp_writer=csv.writer(temp_csv)
        temp_writer.writerow(row)
        # temp_writer.writerow([str(times),str(amps),str(volts),str(power),str(temps), str(pressures)])
    file_temp.close()
    return


d=u12.U12()
i=0
max=1000000000000
# frequency=1

now=datetime.datetime.now()
time_stamp=str(now.year) +'-'+ str(now.month) +'-'+ str(now.day)
filename="history_" + time_stamp
labels=["time", "temps", "pressure"]
write_to_csv(labels, filename)

while i<max:
    t=temperature_read(d)
    p=pressure_read(d)
    i+=1
    if(i%10==0):
        tp=[time.time(),t,p]
        write_to_csv(tp, filename)
    if(i%25==0):
        # tp=[time.time(),t,p]
        #write_to_csv(tp, filename)
        print t
        print p
    # time.sleep(frequency)
    if(i==max):
        check=raw_input("continue? press enter for yes, all else for no")
        if check=="":
            i=0
            continue
        else:
            break