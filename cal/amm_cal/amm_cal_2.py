import u12
from time import sleep
import numpy as np
import matplotlib.pyplot as plt

d=u12.U12(serialNumber=100054654)
load_res=7.5 
for i in np.arange(0.0,1.0,0.1):
    d.eAnalogOut(i,0)
    curr=i/load_res
    meas=d.eAnalogIn(channel=11,gain=20)['voltage']
    ratio=meas/curr
    print('calculated shunt resistance')
    print(ratio*load_res)
    sleep(5)
d.eAnalogOut(0,0)
d.close()

#output
#1.0432839912280703
#0.9818393640350878
#0.9301603618421053
#0.9175438596491228
#0.9098101699561404
#0.7214124177631579
#0.5769599780701754
#0.583874725877193
