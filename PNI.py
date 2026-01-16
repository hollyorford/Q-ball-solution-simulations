#Scan_graph_check

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D

x = 4.9 #SOL 1: 6.00 
x_0=x
x_mid = x

r_tl = 0
omega_tl = 0.839 #SOL 1: 0.72122648

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
eq_ratio_list = []
eq_ratio = 0

const_EQ = True
const_E = E
const_Q = Q

noprint = False
findEQ = True
EQ_plateau_ratio = 0

print('PURE NATURAL INFLATION MODEL NOW RUNNING')

print('Value of omega used for graph: ' + str(omega_tl))
while r_tl < 11: #Change for more accuracy, reduced for speed in calculations
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
    dz_mid = (np.sin(x) - ((omega_tl**2)*x) - y_mid)*0.5*dr_tl
    
    V_mid = 1-np.cos(x) #NEW
    dE_mid = 4*np.pi*((0.5*(z**2))+(((omega_tl**2)*(x**2))/2)+V_mid)*(r_tl**2)*0.5*dr_tl #NEW
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
    dz= (np.sin(x_mid) - ((omega_tl**2)*x_mid) - y)*dr_tl
    
    V = 1-np.cos(x_mid) #NEW
    dE = 4*np.pi*((0.5*(z_mid**2))+(((omega_tl**2)*(x_mid**2))/2)+V)*(r_tl_mid**2)*dr_tl #NEW
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
    
    E_list.append(E)
    Q_list.append(Q)
    
    eq_ratio = E/Q
    eq_ratio_list.append(eq_ratio)

    if findEQ == True:
        if r_tl > 10: #For a stable solution, r=10 is comfortably in plateau so this gives approximate E/Q
            E_val = E
            Q_val = Q
            EQ_plateau_ratio = E/Q
            findEQ = False

print('Initial field value x_0 used: ' + str(x_0))
print('Value of omega used for graph: ' + str(omega_tl))
print('Total E/Q ratio of qball is: ' + str(EQ_plateau_ratio))


#Radius finder

f_a = 1e15 #1e12 for QCD in GeV but converted to MeV
Lambda = 150 #MeV

print('For initial value x(0)=' + str(x_0))
print('\nEnergy of Q-ball Plateau = ' + str(E_val))
print('Charge of Q-ball Plateau = ' + str(Q_val))
i = 0
energy_val = E_list[i]

Radius_energy = 0.99*E_val

while energy_val < Radius_energy:
    i = i+1
    energy_val = E_list[i]

percentage = (energy_val/E_val)*100
resc_Radius = r_list[i]
Radius_MeV = (f_a*resc_Radius)/(Lambda**2)
Radius_length = (197.3*Radius_MeV)/(1e15) #Converted fm to m

if Radius_length <= 1e-12:
    unit = 'pm'
    Radius_length=Radius_length*(1e12)
elif 1e-12 < Radius_length <= 1e-9:
    unit = 'nm'
    Radius_length=Radius_length*(1e9)
elif 1e-9 < Radius_length <= 1e-6:
    unit = 'micrometers'
    Radius_length=Radius_length*(1e6)
elif 1e-6 < Radius_length <= 1e-2:
    unit = 'mm'
    Radius_length=Radius_length*(1e3)
elif 1e-2 < Radius_length <= 1:
    unit = 'cm'
    Radius_length=Radius_length*(1e2)
elif 1 < Radius_length <= 1e3:
    unit = 'm'
elif 1e3 < Radius_length:
    unit = 'km'
    Radius_length=Radius_length/1e3

print('\nRadius of Q-ball is ' + str(Radius_length) + unit)
print('This radius contains ' + str(percentage) + '%' + ' of the Q-ball energy')


#Graphs


labelleg = '$x(0) = $' +  str(x_0) + '\n' + '$\\tilde{{\omega}}$ = ' + str(omega_tl) + '\n' + '$d\\tilde{{r}} = $'+str(dr_tl)
labelleg2 = '$x(0) = $' +  str(x_0) + '\n' + '$\\tilde{{\omega}}$ = ' + str(omega_tl)

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
    plt.plot(r_list, Q_list, color="#EA822C", label= 'Charge', linewidth=2.0)
    plt.xlabel('Rescaled Radius $\\tilde{r}$',fontsize=22)
    plt.title('Graph for Energy and Charge with x(0)=' + str(x_0) + ' and $\\tilde{{\omega}}$ =' + str(omega_tl), fontsize=22)
    plt.ylabel('Energy and Charge',fontsize=22)
    plt.legend(fontsize=20, loc='upper left')
    plt.xticks(fontsize=20)  
    plt.yticks(fontsize=20)
    plt.show()

    plt.plot(r_list, eq_ratio_list, color="#5D3691", label= labelleg2, linewidth=2.0)
    plt.xlabel('Rescaled Radius $\\tilde{r}$',fontsize=22)
    plt.ylabel('Energy/Charge Ratio',fontsize=22)
    plt.axhline(1.0, color="#FF0000", linestyle='--')
    plt.title('Graph showing stable ratio of Energy to Charge for Q-ball', fontsize=22)
    plt.legend(fontsize=20, loc= 'bottom right')
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