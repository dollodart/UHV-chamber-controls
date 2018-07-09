#nominally 5*V-2 in 10 times less whatever, since magnitudes are not recorded. 
import scipy.stats
import numpy as np
import matplotlib.pyplot as plt
#Granville-Phillips model IGC 
#r=[0.67,0.83,1.04,1.21,1.37,1.54,1.74,2.45]
#p=[1,2,3,4,5,6,7.1,10.2]

#s,i,r,p,sigma=scipy.stats.linregress(r,p)

#varian model IGC
# problem with ground reference?
#p in microtorr
pres=np.array([3.0,3.5,4.0,4.5,5.0,5.5,6.0,#data 1
        1.50,
        2.80
        ])
read=np.array([-1.46484375,
-1.6650390625,
-1.9189453125,
-2.177734375,
-2.4169921875,
-2.65625,
-2.9296875, #data 1
-0.7470703125,
-1.34765625
])
#1e-7 torr
#pres,read=np.transpose(np.genfromtxt('pres_cal_2.csv',delimiter=','))
#pres=pres*10**7
s,i,r,p,sigma=scipy.stats.linregress(read,pres)
plt.plot(read,pres,'ko')
plt.plot(read,read*s+i,'k-')
plt.title('slope='+str(np.round(s,2))+',intercept='+str(np.round(i,2))+',r-value='+str(np.round(r,2)))
plt.show()
