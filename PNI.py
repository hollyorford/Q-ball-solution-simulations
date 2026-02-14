#Scan_graph_check

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D

p = 3
M_pl= 1.22e+19 #GeV
F=0.01*M_pl

x = 4.89
omega_tl = 0.777
r_max=15

x_0=x
x_mid = x

r_tl = 0
dx = 0
dr_tl = 0.0001
dr_tl_mid = dr_tl
dz = 0

z = 0
z_mid = z

V_resc = 0 #NEW
E = 0 #NEW
Q = 0 #NEW

x_list = []
r_list = []

Q_list = []
E_list = []
eq_ratio_list = []
eq_ratio = 0
V_list = []

const_EQ = True
const_E = E
const_Q = Q

noprint = False
findEQ = True
EQ_plateau_ratio = 0

print('PURE NATURAL INFLATION MODEL NOW RUNNING')

print('Value of omega used for graph: ' + str(omega_tl))
while r_tl < r_max: #Change for more accuracy, reduced for speed in calculations
    print('Rescaled field value: ' + str(x) + '\n')
    print('Rescaled radius: ' + str(r_tl) + '\n')
    print('E/Q Ratio is: ' + str(eq_ratio))
    print('   ')

    #MIDS
    if r_tl == 0:
        y_mid = 0 
    else:
        y_mid = (2/r_tl)*z
    
    dx_mid = 0.5*z*dr_tl
    dz_mid = ((2*x*p*((1+(x)**2)**(-p-1))) - ((omega_tl**2)*x) - y_mid)*0.5*dr_tl
    
    V_mid_resc = (1-((1+(x**2))**(-p))) #Removed M^4 since drops out in energy eq. due to E rescaling, technically also rescaled potentially
    dE_mid = 4*np.pi*((0.5*(z**2))+(((omega_tl**2)*(x**2))/2)+V_mid_resc)*(r_tl**2)*0.5*dr_tl #NEW
    dQ_mid = 4*np.pi*omega_tl*((x**2)*(r_tl**2))*0.5*dr_tl #NEW

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
    dz= ((2*x_mid*p*((1+(x_mid)**2)**(-p-1))) - ((omega_tl**2)*x_mid) - y)*dr_tl
    
    V_resc = (1-((1+(x_mid**2))**(-p))) #Removed M^4 since drops out in rescaled E equation where this is used
    dE = 4*np.pi*((0.5*(z_mid**2))+(((omega_tl**2)*(x_mid**2))/2)+V_resc)*(r_tl_mid**2)*dr_tl #NEW
    dQ = 4*np.pi*omega_tl*((x_mid**2)*(r_tl_mid**2))*dr_tl #NEW

    x = x + dx
    z = z + dz
    r_tl = r_tl + dr_tl

    if x < 0:
        noprint = True
        break
   
    E = E + dE #NEW
    Q = Q + dQ #NEW

    x_list.append(x)
    r_list.append(r_tl)
    V_list.append(V_resc)
    
    E_list.append(E)
    Q_list.append(Q)
    
    eq_ratio = E/Q
    eq_ratio_list.append(eq_ratio)

    if findEQ == True:
        if r_tl > 5.5: #For a stable solution, r=10 is comfortably in plateau so this gives approximate E/Q
            E_val = E
            Q_val = Q
            EQ_plateau_ratio = E/Q
            findEQ = False

print('Initial field value x_0 used: ' + str(x_0))
print('Value of omega used for graph: ' + str(omega_tl))
print('Total E/Q ratio of qball is: ' + str(EQ_plateau_ratio))

#Graphs

labelleg = '$x(0) = $' +  str(x_0) + '\n' + '$\\tilde{{\omega}}$ = ' + str(omega_tl) + '\n' + '$d\\tilde{{r}} = $'+str(dr_tl)
labelleg2 = '$x(0) = $' +  str(x_0) + '\n' + '$\\tilde{{\omega}}$ = ' + str(omega_tl)
labelEQ = '\nE/Q ratio for plateau:\n' + str(round(EQ_plateau_ratio,6))

if noprint == False:
    plt.plot(r_list, x_list, color='#008080', label = labelleg, linewidth=2.0 )
    plt.xlabel('Rescaled Radius $\\tilde{r}$',fontsize=22)
    plt.ylabel('Rescaled Scalar Field $\phi /f_a$',fontsize=22)
    plt.title('Graph showing rescaled scalar field plotted against rescaled radius', fontsize=22)
    plt.legend(fontsize=20, loc= 'upper right')
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.show()

    plt.plot(r_list, E_list, color="#CA0564", label= 'Energy', linewidth=2.0)
    plt.plot(r_list, Q_list, color="#EA822C", label= 'Charge' + labelEQ, linewidth=2.0)
    plt.xlabel('Rescaled Radius $\\tilde{r}$',fontsize=22)
    plt.title('Graph for Energy and Charge with x(0)=' + str(x_0) + ' and $\\tilde{{\omega}}$ =' + str(omega_tl), fontsize=22)
    plt.ylabel('Energy and Charge',fontsize=22)
    plt.legend(fontsize=20, loc='upper left')
    plt.xticks(fontsize=20)  
    plt.yticks(fontsize=20)
    plt.show()

    plt.plot(r_list, V_list, color="#0B830B", label= 'Potential', linewidth=2.0)
    plt.xlabel('Rescaled Radius $\\tilde{r}$',fontsize=22)
    plt.title('Graph of Pure Natural Inflation Potential against Radius', fontsize=22)
    plt.ylabel('Rescaled Potential',fontsize=22)
    plt.legend(fontsize=20, loc='upper left')
    plt.xticks(fontsize=20)  
    plt.yticks(fontsize=20)
    plt.show()

    plt.plot(r_list, eq_ratio_list, color="#5D3691", label= labelleg2, linewidth=2.0)
    plt.xlabel('Rescaled Radius $\\tilde{r}$',fontsize=22)
    plt.ylabel('Energy/Charge Ratio',fontsize=22)
    plt.axhline(1.0, color="#FF0000", linestyle='--')
    plt.title('Graph showing stable ratio of Energy to Charge for Q-ball', fontsize=22)
    plt.legend(fontsize=20, loc= 'lower right')
    plt.xticks(fontsize=20)  
    plt.yticks(fontsize=20)
    plt.show()

    plt.plot(Q_list, E_list, color="#3ACA05", label=labelleg, linewidth=2.0)
    plt.xlabel('Charge $\\tilde{r}$',fontsize=22)
    plt.legend(fontsize=20, loc= 'upper left')
    plt.title('Graph showing Q-ball Charge plotted against Energy', fontsize=22)
    plt.ylabel('Energy',fontsize=22)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.show()

    plt.plot(r_list, Q_list, color="#CA8C05", label= labelleg, linewidth=2.0)
    plt.xlabel('Rescaled Radius $\\tilde{r}$',fontsize=22)
    plt.ylabel('Internal Charge',fontsize=22)
    plt.title('Graph showing Q-ball Charge plotted against rescaled Radius', fontsize=22)
    plt.legend(fontsize=20, loc= 'upper left')
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.show()

    plt.plot(r_list, E_list, color="#CA0564", label=labelleg, linewidth=2.0)
    plt.xlabel('Rescaled Radius $\\tilde{r}$',fontsize=22)
    plt.ylabel('Energy',fontsize=22)
    plt.legend(fontsize=20, loc= 'upper left')
    plt.title('Graph showing Q-ball Energy plotted against rescaled Radius', fontsize=22)
    plt.xticks(fontsize=20)  
    plt.yticks(fontsize=20)
    plt.show()

else:
    print('\n Scalar field turned negative adjust omega')