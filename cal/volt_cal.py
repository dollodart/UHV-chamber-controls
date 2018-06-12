#magnitudes are not reported
import scipy.stats
import u12 
from time import sleep
import numpy as np
d=u12.U12()

vappl=[]
vout=[]
for i in np.linspace(0,5,30):
    d.eAnalogOut(i,0)
    vappl.append(i)  
    vout.append(d.eAnalogIn(4)['voltage']-d.eAnalogIn(5)['voltage'])
    if d.eAnalogIn(4)['voltage']-d.eAnalogIn(5)['voltage'] > 9.9: #saturation point
        break
    sleep(10)
np.savetxt('vappl',vappl)
np.savetxt('vout',vout)
d.eAnalogOut(0,0)
d.close()

    

