import numpy as np
import matplotlib.pyplot as plt
import pylab as pylab

c0=-1.7600413686e1
c1=3.8921204975e1
c2=1.8558770032e-2
c3=-9.9457592874e-5
c4=3.1840945719e-7
c5=-5.6072844889e-10
c6=5.6075059059e-13
c7=-3.2020720003e-16
c8=9.7151147152e-20
c9=-1.2104721275e-23
alpha0=1.185976e2
alpha1=-1.183432e-4
c=[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9]

def v(t):
    '''Valid for 0 to 1372 deg C, temperature in deg C and thermovoltage in uV.'''
    res=alpha0*np.exp(alpha1*(t-127.9686)**2)
    for i in range(len(c)): 
        res+=c[i]*t**i
    return res

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

thermovoltages=np.arange(1.,54885.,1.)
temps=[t(tv) for tv in thermovoltages]
plt.plot(thermovoltages,temps)
plt.xlabel('Thermovoltage in uV')
plt.ylabel('Temperature in deg. C')
pylab.show()
