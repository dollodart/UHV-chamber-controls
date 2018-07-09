import os
import numpy as np
import matplotlib.pyplot as plt
from funcs import PID,plant

time_iter=0.1
T_SP=680
x_e=0
x_lst=[x_e] #the list is merely for record-keeping. The independent variable is tuned only to the response from the controller and its initial value
T_lst=[298]
num_hist=4 #this will speed convergence but give spurious higher order effects depending on the system
err_lst=[0]
t_range=range(1000)
for i in t_range:    
    T_lst.append(plant(old=T_lst[i],x=x_lst[i],time_iter=time_iter))
    err_lst.append(T_SP-T_lst[i+1]) #error is defined as the sign relative from desired set-point. + error -> y is too low, - error -> y is too high
    response=PID(err_lst=err_lst,num_hist=num_hist,time_iter=time_iter)
    x_lst.append(x_e+response) #the response is defined as the sign relative from the existing value of the independent variable
plt.plot(t_range+[t_range[-1] + 1],T_lst,'ko-')
plt.show()
