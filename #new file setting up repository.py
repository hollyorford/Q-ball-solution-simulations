#new file setting up repository
 
#Damped Harmonic Oscillator Practice

import numpy as np
from matplotlib import pyplot as plt

# Basic Equation y.. + 2 gamma y. = -omega^2 y
# rewrite as a pair of coupled first order equations y. = z and y..=z.

y=10
dy=0
z=0
dz=0
t=0
dt=0.001
gamma = 0.01 #float(input('What is your damping factor?'))
omega = 1
y_list = []
t_list = []
x_line = []
b = 0
print('Data produced at times 8s, 25s, 5s, 78s')
while t <= 100:
    dy=z*dt
    dz=((-2*gamma*z)-((omega**2)*y))*dt
    z=z+dz
    if b == 8000:
        print('Time is ' + str(t) + 's')
        print('Time interval ' + str(dt) + 's')
        print('Position is ' + str(y) + 'm' + '\n')
    if b == 25000:
        print('Time is ' + str(t)+ 's')
        print('Time interval ' + str(dt)+ 's')
        print('Position is ' + str(y) + 'm' '\n')
    if b == 52000:
        print('Time is ' + str(t) + 's')
        print('Time interval ' + str(dt)+ 's')
        print('Position is ' + str(y) + 'm'+'\n')
    if b == 78000:
        print('Time is ' + str(t) + 's')
        print('Time interval ' + str(dt)+ 's')
        print('Position is ' + str(y) + 'm'+'\n')
    y=y+dy
    t=t+dt
    y_list.append(y)
    t_list.append(t)
    
    x_line.append(0)
    b = b + 1

plt.plot(t_list, y_list, color='#008080')
plt.plot(t_list, x_line, color='#000000')
plt.axvline(x=8, color='red', linestyle='--')
plt.xlabel('Time /s',fontsize=22)
plt.ylabel('Position /m',fontsize=22)
plt.show()