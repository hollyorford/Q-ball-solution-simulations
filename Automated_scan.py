#Automated_scan

import numpy as np
from matplotlib import pyplot as plt

x = 6.3466 #x = phi/f_a for phi
x_0 = x
x_mid = x

r_tl = 0
omega_tl = 0.1

dx = 0
dr_tl = 0.0001
dr_tl_mid = dr_tl
dz = 0

z = 0
z_mid = z

x_list = []
r_list = []

dx_0 = 0.0000001
LOOP = True

while LOOP == True:
    x = x_0 + dx_0
    x_0 = x
    changex = False
    while r_tl < 100 and changex == False:
        if r_tl == 0:
            y_mid = 0 
        else:
            y_mid = (2/r_tl)*z
        

        dx_mid = 0.5*z*dr_tl
        dz_mid = (np.sin(x) - ((omega_tl**2)*x) - y_mid)*0.5*dr_tl

        x_mid = x + dx_mid
        z_mid = z + dz_mid
        r_tl_mid = r_tl + 0.5*dr_tl

        if r_tl_mid == 0:
            y = 0 
        else:
            y = (2/r_tl_mid)*z_mid
        
        dx = z_mid*dr_tl
        dz= (np.sin(x_mid) - ((omega_tl**2)*x_mid) - y_mid)*0.5*dr_tl

        x_1 = x

        x = x + dx
        z = z + dz
        r_tl = r_tl + dr_tl

        x_2 = x 
        
        if x_2 < 1:
            if x_2 < x_1:
                x_min = x_2
                r_min = r_tl

        if r_tl > 25:
            if x > 1:
                changex = True
        elif r_tl > 40:
            if x > 1:
                changex = True
        

        if x < 0:
            LOOP = False
        

    r_tl = 0
    omega_tl = 0.1

    dx = 0
    dr_tl = 0.0001
    dr_tl_mid = dr_tl
    dz = 0

    z = 0
    z_mid = z

    print('Last x_0 value used was: ' +  str(x_0))
    print('Minimum x acheieved was: ' + str(x_min) + ' At r value of: ' + str(r_min))
    its = (6.3467 - x_0)/dx_0
    print('x_0 lies between 6.3466 and 6.3467, up to ' + str(its) + ' iterations remaining\n')


x = x_0

while r_tl < 100:

    print('Rescaled field value: ' + str(x) + '\n')
    print('Rescaled Scalar field: ' + str(r_tl) + '\n')
    print('   ')

    #MIDS
    if r_tl == 0:
        y_mid = 0 
    else:
        y_mid = (2/r_tl)*z
    
    dx_mid = 0.5*z*dr_tl
    dz_mid = (np.sin(x) - ((omega_tl**2)*x) - y_mid)*0.5*dr_tl

    x_mid = x + dx_mid
    z_mid = z + dz_mid
    r_tl_mid = r_tl + 0.5*dr_tl

    if r_tl_mid == 0:
        y = 0 
    else:
        y = (2/r_tl_mid)*z_mid
    
    dx = z_mid*dr_tl
    dz= (np.sin(x_mid) - ((omega_tl**2)*x_mid) - y_mid)*0.5*dr_tl

    x = x + dx
    z = z + dz
    r_tl = r_tl + dr_tl

    x_list.append(x)
    r_list.append(r_tl)

plt.plot(r_list, x_list, color='#008080')
plt.xlabel('Rescaled Radius $\\tilde{r}$',fontsize=22)
plt.ylabel('Rescaled Scalar Field $\phi /f_a$',fontsize=22)
plt.show()