#nominally 5*V-2 in 10 times less whatever, since magnitudes are not recorded. 
import scipy.stats
import numpy as np
# old ICG controller
#r=[0.67,0.83,1.04,1.21,1.37,1.54,1.74,2.45]
#p=[1,2,3,4,5,6,7.1,10.2]

#s,i,r,p,sigma=scipy.stats.linregress(r,p)

#varian model
p=np.arange(3.0,6.5,0.5)
print(p)
r=[-1.46484375, #why negative voltages with non-unity slope? see manual
-1.6650390625,
-1.9189453125,
-2.177734375,
-2.4169921875,
-2.65625,
-2.9296875]
#failed for lower pressures, why?

s,i,r,p,sigma=scipy.stats.linregress(r,p)
print(s,i,r,p,sigma)
