import numpy as np
from time import sleep

def plant(old,x,time_iter):
    ''' a plant model which returns temperature based on Joule heating, the previous value, the time interval. COnsiders conduction and radiation effects '''
    density=5.61 # g/cm^3
    mol_mass=81.4 # g/mol
    area=0.5*1 #cm^3
    thickness=0.4e-1 #cm
    volume=area*thickness
    emissivity=0.98
    R=8.314 # J/(mol K)
    heat_capacity=3*R/mol_mass # J/(g K), order of magnitude estimate by Dulong-Petit
    sigma=5.67e-12 # W/(cm^2 K^4)
    T_inf=298. #K
    U=0.005 #overall heat transfer coefficient, W/K
    thermal_inertia=density*heat_capacity*volume
    dt=thermal_inertia
    num_loop=int(round(time_iter/dt))
    for i in range(num_loop):
        old+= dt/thermal_inertia*(x-U*(old-T_inf)-sigma*area*emissivity*(old**4-T_inf**4))
    return old
    
def PID(err_lst,time_iter,num_hist):
    ''' returns the manipulated variable given the error using PID. Ensure that the parameters are optimized for the control of interest.'''
    kP=0.1
    kI=0.01
    kD=0.0

    time=time_iter*len(err_lst)

    try:
        P=kP*np.average(err_lst[-num_hist:]) 
        I=kI*np.trapz(err_lst,x=None,dx=time_iter)/time
        D=kD*np.average(np.gradient(err_lst,time_iter)[-num_hist:])
    except: #initially, when there is no history
        P=kP*np.average(err_lst)
        I=kI*np.trapz(err_lst,x=None,dx=time_iter)/time
        D=kD*np.average(np.gradient(err_lst,time_iter))

    return P+I+D

def PGA_auto(controller,channel):
    '''adjusts the gain of the programmable gain amplifier prior to digitization for signals that vary in voltage. Assumes positive differential signal.'''
    signal=abs(controller.eAnalogIn(channel=channel,gain=1)['voltage'])
    gains=np.array([1.,2.,4.,5.,8.,10.,16.,20.])
    ranges=20./gains
    ratios=signal/ranges
    valid_gains=gains[np.where(ratios<1)]
    try:
        gain=int(max(valid_gains))
    except TypeError:
        gain=20
    sleep(0.0800) #sleep 80 milliseconds prior to querying channel again
#    print('signal='+str(signal)+',gain='+str(gain))
    return controller.eAnalogIn(channel=channel,gain=gain)['voltage']
