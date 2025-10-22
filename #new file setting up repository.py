#new file setting up repository
 
#Damped Harmonic Oscillator Practice

import numpy as np
import matplotlib as plt

# Basic Equation y.. + 2 gamma y. = -omega^2 y
# rewrite as a pair of coupled first order equations y. = z and y..=z.

y=0
dy=0
z=0
dz=0
t=0
dt=0.1
gamma = 0.1 #float(input('What is your damping factor?'))
omega = 1
y_list = []
t_list = []

while t >= 500:
    dy=z*dt
    dz=((-2*gamma*z)-((omega^2)*y))*dt
    z=z+dz
    y=y+dy
    t=t+dt
    y_list.append(y)
    t_list.append(t)


#plt.title('Path of Proton in Synchrocyclotron', fontsize=16)
plt.plot(y_list, t_list, color='#008080')
plt.xlabel('Position',fontsize=16)
plt.ylabel('Time',fontsize=16)
#plt.tick_params(axis='both', labelsize=16) 
plt.show()