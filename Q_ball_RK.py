#Real Q-Ball simulation Runge Kutta Method

import numpy as np
from matplotlib import pyplot as plt

x = 7 # x = phi/f_a for phi = 6 start
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