import u12
import numpy
d = u12.U12()
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
# d.localID(2)
# print(d.eAnalogIn(0))
# k=d.digitalIO()

# print(d.eDigitalIn(0))
# print(digital_readout)

print "Mantissa: " + str(flt_mantissa)
print "Exponent: " + str(int_exp)
print "Chamber Pressure Reading: " + str(flt_mantissa) + " * 10^ -" + str(int_exp)
pressure = flt_mantissa * pow(10, -1*int_exp)
print pressure

