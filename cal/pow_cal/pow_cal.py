#nominally 5*V-2 in 10 times less whatever, since magnitudes are not recorded. 
import scipy.stats
import numpy as np
import matplotlib.pyplot as plt
temperature,c,voltage,resistance,power=np.transpose(np.genfromtxt('pow_dat.csv',delimiter=','))
s,i,r,p,sigma=scipy.stats.linregress(power,temperature)
plt.plot(power,temperature,'ko')
plt.plot(power,power*s+i,'k-')
plt.title('slope='+str(np.round(s,2))+',intercept='+str(np.round(i,2))+',r-value='+str(np.round(r,2)))
plt.show()
