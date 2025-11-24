#Find Radius

#Scan_graph_check

import numpy as np
from matplotlib import pyplot as plt


f_a = 10e12
m_pi = 135 #MeV
f_pi = 130 #MeV
Lambda = np.sqrt(m_pi*f_pi)

x = 6 #6 #CHANGE X_0 HERE AND BELOW
x_mid = x

r_tl = 0
omega_tl = 0.4723751033 #0.72122648 #CHANGE OMEGA HERE AND BELOW

dx = 0
dr_tl = 0.001
dr_tl_mid = dr_tl
dz = 0

z = 0
z_mid = z

V = 0
E = 0 
Q = 0 

x_list = []
r_list = []

Q_list = []
E_list = []

energy_data = 0
energy_sum = 0
n=0

print('Value of omega used for graph: ' + str(omega_tl))
while r_tl < 50:
    print('Rescaled field value: ' + str(x) + '\n')
    print('Rescaled radius: ' + str(r_tl) + '\n')
    print('   ')

    #MIDS
    if r_tl == 0:
        y_mid = 0 
    else:
        y_mid = (2/r_tl)*z
    
    dx_mid = 0.5*z*dr_tl
    dz_mid = (np.sin(x) - ((omega_tl**2)*x) - y_mid)*0.5*dr_tl
    
    V_mid = 1-np.cos(x)
    dE_mid = 4*np.pi*((0.5*(z**2))+(((omega_tl**2)*(x**2))/2)+V_mid)*(r_tl**2)*dr_tl 
    dQ_mid = 4*np.pi*omega_tl*((x**2)*(r_tl**2))*dr_tl 

    x_mid = x + dx_mid
    z_mid = z + dz_mid
    r_tl_mid = r_tl + 0.5*dr_tl


    E_mid = E + dE_mid #NEW
    Q_mid = Q + dQ_mid #NEW

    if r_tl_mid == 0:
        y = 0 
    else:
        y = (2/r_tl_mid)*z_mid
    
    dx = z_mid*dr_tl
    dz= (np.sin(x_mid) - ((omega_tl**2)*x_mid) - y)*dr_tl
    
    V = 1-np.cos(x_mid) #NEW
    dE = 4*np.pi*((0.5*(z_mid**2))+(((omega_tl**2)*(x_mid**2))/2)+V)*(r_tl_mid**2)*dr_tl #NEW
    dQ = 4*np.pi*omega_tl*((x_mid**2)*(r_tl_mid**2))*dr_tl #NEW

    x = x + dx
    z = z + dz
    r_tl = r_tl + dr_tl

    E = E + dE 
    Q = Q + dQ 
    if r_tl > 20:    #CHANGE HERE FOR DIFFERENT MODEL USE GRRAPH TO FIND BOUNDS
        if r_tl < 25:    #CHANGE HERE FOR DIFFERENT MODEL
            energy_data = E
            energy_sum = energy_sum + energy_data
            n = n + 1

av_tot_qball_E = energy_sum/n
energy_99 = av_tot_qball_E*0.99


x = 6 #CHANGE x_0 HERE
x_mid = x

r_tl = 0
omega_tl = 0.4723751033 #CHANGE OMEGA HERE

dx = 0
dr_tl = 0.001
dr_tl_mid = dr_tl
dz = 0

z = 0
z_mid = z

V = 0
E = 0 
Q = 0 

x_list = []
r_list = []

Q_list = []
E_list = []

Select_R_99 = True

print('Value of omega used for graph: ' + str(omega_tl))
while r_tl < 50:
    print('Rescaled field value: ' + str(x) + '\n')
    print('Rescaled radius: ' + str(r_tl) + '\n')
    print('   ')

    #MIDS
    if r_tl == 0:
        y_mid = 0 
    else:
        y_mid = (2/r_tl)*z
    
    dx_mid = 0.5*z*dr_tl
    dz_mid = (np.sin(x) - ((omega_tl**2)*x) - y_mid)*0.5*dr_tl
    
    V_mid = 1-np.cos(x)
    dE_mid = 4*np.pi*((0.5*(z**2))+(((omega_tl**2)*(x**2))/2)+V_mid)*(r_tl**2)*dr_tl
    dQ_mid = 4*np.pi*omega_tl*((x**2)*(r_tl**2))*dr_tl 

    x_mid = x + dx_mid
    z_mid = z + dz_mid
    r_tl_mid = r_tl + 0.5*dr_tl


    E_mid = E + dE_mid 
    Q_mid = Q + dQ_mid 

    if r_tl_mid == 0:
        y = 0 
    else:
        y = (2/r_tl_mid)*z_mid
    
    dx = z_mid*dr_tl
    dz= (np.sin(x_mid) - ((omega_tl**2)*x_mid) - y)*dr_tl
    
    V = 1-np.cos(x_mid)
    dE = 4*np.pi*((0.5*(z_mid**2))+(((omega_tl**2)*(x_mid**2))/2)+V)*(r_tl_mid**2)*dr_tl 
    dQ = 4*np.pi*omega_tl*((x_mid**2)*(r_tl_mid**2))*dr_tl 

    x = x + dx
    z = z + dz
    r_tl = r_tl + dr_tl

    E = E + dE
    Q = Q + dQ 

    if E < energy_99:
        if Select_R_99 == True:
            R_99 = r_tl
            Select_R_99 = False

    x_list.append(x)
    r_list.append(r_tl)
    
    E_list.append(E)
    Q_list.append(Q)



real_qbR = R_99 * (f_a/(Lambda**2))
        

print('Value of omega used for graph: ' + str(omega_tl))
print('99 percent of total energy is: ' + str(energy_99))
print('Radius of qball found to be: ' + str(real_qbR))



plt.plot(r_list, x_list, color='#008080')
plt.xlabel('Rescaled Radius $\\tilde{r}$',fontsize=22)
plt.ylabel('Rescaled Scalar Field $\phi /f_a$',fontsize=22)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()

plt.plot(r_list, Q_list, color="#CA8C05")
plt.xlabel('Rescaled Radius $\\tilde{r}$',fontsize=22)
plt.ylabel('Internal Charge',fontsize=22)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()

plt.plot(r_list, E_list, color="#CA0564")
plt.xlabel('Rescaled Radius $\\tilde{r}$',fontsize=22)
plt.ylabel('Energy',fontsize=22)
plt.xticks(fontsize=20)  
plt.yticks(fontsize=20)
plt.show()