#Scan_graph_check

import numpy as np
from matplotlib import pyplot as plt

x = 6.00 # x = phi/f_a for phi = 6 start
x_0=x
x_mid = x

r_tl = 0
omega_tl = 0.72122648 #0.72 #0.4723751033 #0.472375 #0.4721 #0.412294939 for 6.3466, 0.001 #0.412295 #0.4123 #0.41204 MAKE LESS

dx = 0
dr_tl = 0.0001
dr_tl_mid = dr_tl
dz = 0

z = 0
z_mid = z

V = 0 #NEW
E = 0 #NEW
Q = 0 #NEW

x_list = []
r_list = []

Q_list = []
E_list = []

const_EQ = True
const_E = E
const_Q = Q

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
    
    V_mid = 1-np.cos(x) #NEW
    dE_mid = 4*np.pi*((0.5*(z**2))+(((omega_tl**2)*(x**2))/2)+V_mid)*(r_tl**2)*dr_tl #NEW
    dQ_mid = 4*np.pi*omega_tl*((x**2)*(r_tl**2))*dr_tl #NEW

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

    E = E + dE #NEW
    Q = Q + dQ #NEW

    x_list.append(x)
    r_list.append(r_tl)
    
    E_list.append(E)
    Q_list.append(Q)

    if r_tl > 20: #CHANGE HERE FOR DIFFERENT MODELS
        if const_EQ == True:
            const_E = E
            const_Q = Q
            const_EQ = False

        

print('Value of omega used for graph: ' + str(omega_tl))
print('Total constant energy of qball is: ' + str(const_E))
print('Total constant charge of qball is: ' + str(const_Q))

labelleg = '$x(0) = $' +  str(x_0) + '\n' + '$\\tilde{{\omega}}$ = ' + str(omega_tl) + '\n' + '$d\\tilde{{r}} = $'+str(dr_tl)

plt.plot(r_list, x_list, color='#008080', label = labelleg, linewidth=2.0 )
plt.xlabel('Rescaled Radius $\\tilde{r}$',fontsize=22)
plt.ylabel('Rescaled Scalar Field $\phi /f_a$',fontsize=22)
plt.legend(fontsize=20, loc= 'upper right')
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()

plt.plot(r_list, Q_list, color="#CA8C05", label= labelleg, linewidth=2.0)
plt.xlabel('Rescaled Radius $\\tilde{r}$',fontsize=22)
plt.ylabel('Internal Charge',fontsize=22)
plt.legend(fontsize=20, loc= 'upper left')
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()

plt.plot(r_list, E_list, color="#CA0564", label=labelleg, linewidth=2.0)
plt.xlabel('Rescaled Radius $\\tilde{r}$',fontsize=22)
plt.ylabel('Energy',fontsize=22)
plt.legend(fontsize=20, loc= 'upper left')
plt.xticks(fontsize=20)  
plt.yticks(fontsize=20)
plt.show()

plt.plot(Q_list, E_list, color="#3ACA05", label=labelleg, linewidth=2.0)
plt.xlabel('Charge $\\tilde{r}$',fontsize=22)
plt.legend(fontsize=20, loc= 'upper left')
plt.ylabel('Energy',fontsize=22)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()
