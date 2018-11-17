import u12
import numpy

def get_pressure(d):
    '''using AI0'''
    # d = u12.U12()
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

def pressure_read(d, time = 20):
    #needs to turn on and off
    #set fixed time, allow for variable input to change
    #10-15 seconds?
    
    #turn on
    #d.eAnalogOut()
    #wait time x
    from time import sleep
    sleep(time)
    p= get_pressure(d)
    #turn off

    return p

#print(pressure_read())