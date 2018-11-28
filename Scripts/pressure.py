import u12
import numpy
from time import sleep

def get_pressure(d):
    '''using AI0'''
    digital_readout=[]
    pins = [0, 1, 2 , 4]
    for x in pins:
        digital_readout.append(d.eDigitalIn(x, readD= 1))
    bcd=[]
    for x in digital_readout:
        bcd.append(x["state"])
    int_exp = bcd[0]*1+bcd[1]*2+bcd[2]*8+ bcd[3]*4

    analog_mantissa = d.eAnalogIn(0)
    flt_mantissa = analog_mantissa["voltage"]

    # print "Mantissa: " + str(flt_mantissa)
    # print "Exponent: " + str(int_exp)
    # print "Chamber Pressure Reading: " + str(flt_mantissa) + " * 10^ -" + str(int_exp)
    pressure = flt_mantissa * pow(10, -1*int_exp)
    # print pressure
    return pressure

def ion_on(d):
    d.eDigitalOut(0,1)
    d.eDigitalOut(1,1)

def ion_off(d):
    d.eDigitalOut(0,0)
    d.eDigitalOut(1,0)

def pressure_read(d, time = 10, state=False):
    '''uses AI0, passes a int time and bool state (try to make state a pointer/universal)'''
    #check if on
    if not state:
        #turn on
        ion_on(d)
        #wait for t: standard is 10 seconds
        sleep(time)
    p= get_pressure(d)
    #turn off
    ion_off(d)

    return p
# d=u12.U12()
# print(pressure_read(d,5))