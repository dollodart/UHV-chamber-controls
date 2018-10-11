import u12
import numpy
d = u12.U12()
digital_readout=[]
for x in range(4):
    digital_readout.append(d.eDigitalIn(x))
bcd=[]
for x in digital_readout:
    bcd.append(x["state"])
decimal = bcd[0]*1+bcd[1]*2+bcd[2]*4+ bcd[3]*8
# d.localID(2)
# print(d.eAnalogIn(0))
# k=d.digitalIO()

# print(d.eDigitalIn(0))
print(digital_readout)
print(decimal)

