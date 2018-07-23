import u12
from time import sleep
import numpy as np
d=u12.U12(serialNumber=100054654)

resistance=5.7e2 #ohms
PSgain=6.5

for i in np.arange(1.0,3.0,0.25):
    d.eAnalogOut(i,0)
    PSV=i*PSgain
    meas_current=d.eAnalogIn(7)['voltage']
    actual_current=PSV/resistance
    print(meas_current-actual_current)
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
