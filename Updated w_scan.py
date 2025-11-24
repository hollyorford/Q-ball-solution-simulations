#Updated w_scan

#Automated_scan

import numpy as np
from matplotlib import pyplot as plt

x = 6 # OLD VALUES6.3466 #x = phi/f_a for phi
x_0 = x
x_mid = x

r_tl = 0
omega_tl = 0.72122 #0.72

dx = 0
dr_tl = 0.001 #0.0001
dr_tl_mid = dr_tl
dz = 0

z = 0
z_mid = z

x_list = []
r_list = []

dw_0 = 0.00000001
dw_0_stop = dw_0/1000
LOOP = True
changew=False
reduce_step = False

while LOOP == True:
    while r_tl < 100 and changew == False:
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
        dz= (np.sin(x_mid) - ((omega_tl**2)*x_mid) - y)*dr_tl

        x_1 = x

        x = x + dx
        z = z + dz
        r_tl = r_tl + dr_tl

        x_2 = x 
        
        if r_tl < 80:
            if x_2 > x_1:
                changew = True
        if r_tl > 8:
            if x < 0:
                changew = True
                reduce_step = True
        if x_2 < x_1:
            x_min = x_2
            r_min = r_tl

        if x < 0:
            LOOP = False
        if x > x_0:
            LOOP = False
    if reduce_step == True:
        omega_tl = omega_tl - dw_0
        dw_0 = dw_0/10
        reduce_step = False
    omega_tl = omega_tl + dw_0
    changew = False

    if dw_0 < dw_0_stop:
        LOOP = False

    x = x_0
    r_tl = 0

    dx = 0
    dr_tl = 0.001
    dr_tl_mid = dr_tl
    dz = 0

    z = 0
    z_mid = z

    print('Last omega value used was: ' +  str(omega_tl-dw_0))
    print('Minimum x acheieved was: ' + str(x_min) + ' At r value of: ' + str(r_min))
    its = (0.73 - omega_tl)/dw_0
    print('w_0 lies between 0.47 and 0.48, up to ' + str(its) + ' iterations remaining\n')

print('\n \n Field just crossed into negative due to Omega value: ' + str(omega_tl))
omega_tl = omega_tl - dw_0
print('Ideal value of omega is: ' + str(omega_tl))
x = x_0

print('Value of omega used for graph: ' + str(omega_tl))
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
    dz= (np.sin(x_mid) - ((omega_tl**2)*x_mid) - y)*dr_tl

    x = x + dx
    z = z + dz
    r_tl = r_tl + dr_tl

    x_list.append(x)
    r_list.append(r_tl)


print('Value of omega used for graph: ' + str(omega_tl))


plt.plot(r_list, x_list, color='#008080')
plt.xlabel('Rescaled Radius $\\tilde{r}$',fontsize=22)
plt.ylabel('Rescaled Scalar Field $\phi /f_a$',fontsize=22)
plt.xticks(fontsize=20)  
plt.yticks(fontsize=20)
plt.show()