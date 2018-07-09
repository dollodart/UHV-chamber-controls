import os
import numpy as np
import matplotlib.pyplot as plt
from funcs import plant

q=0.# Watts
T0=1000. #response to change in heat value based on change in independent variable
T_lst=[T0]
t_range=range(100)
t_iter=0.1
for i in t_range:    
    T_lst.append(plant(old=T_lst[i],x=q,time_iter=t_iter))
plt.xlabel('time in s')
plt.ylabel('temperature (K)')
plt.title('joule heating ='+str(q)+' W, ambient temperature =298 K')
plt.plot(t_range+[t_range[-1] + 1],T_lst,'ko-')
plt.show()
