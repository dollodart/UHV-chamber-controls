import u12
import sys
from time import sleep
from time import time

d1=u12.U12(serialNumber=100039255)
d1.eAnalogOut(analogOut0=0,analogOut1=5)
burst_data=d1.rawAIBurst(NumberOfScans=128,SampleInterval=int(6000000.0/(128*4)))['Channel2']
pulse_hist=[None]*len(burst_data)
for index,voltage in enumerate(burst_data):
	if voltage > 4:
		pulse_hist[index]=1
	else:
		pulse_hist[index]=0
pulse_num=0
if pulse_hist[0] == 1:
	pulse_num+=1
for index,x in enumerate(pulse_hist):
	if index < len(pulse_hist)-1:
		if x == 0:
			if pulse_hist[index+1] == 1:
				pulse_num+=1
print(len(burst_data))
frequency=pulse_num
Q=(frequency+5)/8.1
print('Flow rate is '+str(Q)+' L/min')
d1.eAnalogOut(analogOut0=0,analogOut1=0)
