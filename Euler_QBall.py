#Euler_QBall

import numpy as np
import math as ma
from matplotlib import pyplot as plt



LOOP = True

#FIXED
f_a = 130 #MeV pion decay constant
m_pi = 135 #MeV pion mass
Lambda = np.sqrt(f_a*m_pi) #MeV QCD scale

#VARIABLES & STARTING VALUES CHANGE HERE
omega = 0.1
phi_0 = 0 # CHECK IF THIS IS 0
r = 0
dr_wig = 0.00000001
z = 0 # Notes pg.14 says to set dphi/dr to zero so z= 0 for r=0
x=6

E_wig = 0
Q_wig = 0


# DIMENSIONLESS PARAMETERS FOR RESCALING
r_wig = ((Lambda**2)*r)/f_a
omega_wig = (f_a*omega)/(Lambda**2)
b=1




phi_list = []
r_wig_list = []
V_wig_list = []


print1=0
print2=0
print3=0
print4=0


while LOOP == True:
    if r_wig ==0:
        z = 0
        y = 0 #since z = 0 at r=0 but term will blow up due to r denominator so set manually
    else:
        y = ((2/r)*z)

    dx = z*dr_wig

    dz = (np.sin(x) - ((omega_wig**2)*x) - y)*dr_wig

    ##########V = (Lambda**4)*(1-np.cos(x))

    #dE_wig = ((4*np.pi)*(0.5*(z**2)) + (((omega_wig**2)*(x**2))/2) + V_wig)*(r_wig**2)*(dr_wig)

    #dQ_wig = 4*np.pi*(x**2)*(r_wig**2)*dr_wig              # CHECK IF NEEDS *OMEGA_WIG FACTOR

    z = z + dz
    x = x + dx
    r_wig = r_wig + dr_wig
    #E_wig = E_wig + dE_wig
    #Q_wig = Q_wig = dQ_wig

    phi = x*f_a

    b = 2

    V_wig = 1 - np.cos(x)

    if x < 3:
        if print1==0:
            print('X value is' + str(x))
            print1 = 1
    if x < 1:
        if print2==0:
            print('X value is' + str(x))
            print2 = 1
    
    if x < 1e-6:
        if print3 == 0:
            print('X value is' + str(x))
            print3 = 1


    if x < 1e-6:
        phi_list.append(phi)
        r_wig_list.append(r_wig)
        V_wig_list.append(V_wig)

    else:
        LOOP = False


plt.plot(phi_list, r_wig_list, color='#008080')
plt.xlabel('Scalar Field',fontsize=22)
plt.ylabel('Rescaled Radius',fontsize=22)
plt.show()

plt.plot(V_wig_list, phi_list, color='#008080')
plt.xlabel('Potential /s',fontsize=22)
plt.ylabel('Position /m',fontsize=22)
plt.show()



