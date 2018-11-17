import u12
import numpy

c0a=0.000
c0b=0.000
c0c=-1.318058e2
c1a=2.5173462e-2
c1b=2.508355e-2
c1c=4.830222e-2
c2a=-1.1662878e-6
c2b=7.860106e-8
c2c=-1.646031e-6
c3a=-1.0833638e-9
c3b=-2.503131e-10
c3c=5.464731e-11
c4a=-8.9773540e-13
c4b=8.315270e-14
c4c=-9.650715e-16
c5a=-3.7342377e-16
c5b=-1.228034e-17
c5c=8.802193e-21
c6a=-8.6632643e-20
c6b=9.804036e-22
c6c=-3.110810e-26
c7a=-1.0450598e-23
c7b=-4.413030e-26
c8a=-5.1920577e-28
c8b=1.057734e-30
c9b=-1.052755e-35
cb=[c0b,c1b,c2b,c3b,c4b,c5b,c6b,c7b,c8b,c9b]
cc=[c0c,c1c,c2c,c3c,c4c,c5c,c6c]

def t(v):
    '''Valid for 0 to 1372 deg C, Temperature in deg. C and thermovoltage in uV.'''
    res=0
    if 0. < v < 20644.:
        for i in range(len(cb)):
            res+=cb[i]*v**i
    elif 20644. < v < 54886.:
        for i in range(len(cc)):
            res+=cc[i]*v**i
    else:
        return None 
    return res
def temperature_read(d): 
    '''using channel AI 1'''
    #d = u12.U12()
    reading = d.eAnalogIn(1) 
    # print(reading)
    voltage = reading["voltage"]
    # print(voltage)
    uv=(voltage/213.77 + 0.001)* 1000000
    # print(uv)
    # print(t(uv))
    return t(uv)