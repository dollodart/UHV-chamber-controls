import numpy as np
import matplotlib.pyplot as plt
import pylab
from scipy import stats

x=np.genfromtxt('vappl')
y=np.genfromtxt('vout')

x=x[:,np.newaxis]
a, _, _, _ = np.linalg.lstsq(x,y,rcond=None)

plt.plot(x,y)
plt.plot(x,a*x)
pylab.show()
print(a)

