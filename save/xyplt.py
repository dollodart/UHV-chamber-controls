import numpy as np
import matplotlib.pyplot as plt

x,y=np.transpose(np.genfromtxt('ramp_history_2.csv',delimiter=','))
plt.plot(y,x)
plt.show()
