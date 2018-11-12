'''Requires the python-drawnow package'''

import matplotlib.pyplot as plt
from drawnow import drawnow,figure
from time import sleep
import numpy as np

f=plt.figure()

x=[1.,2.]
y=[1.,2.]

def draw_fig():
    plt.subplot(111)
    plt.plot(x,y)
o=0
while True:
    o+=1
    with open('data_file.txt','a') as data_file:
        data_file.write('{0} {1}\n'.format(o,o**2))
    x,y=np.transpose(np.genfromtxt('data_file.txt'))
    drawnow(draw_fig)
    sleep(1)
