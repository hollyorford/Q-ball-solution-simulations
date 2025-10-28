#Real Q-Ball simulation

#Euler method

import numpy as np
from matplotlib import pyplot as plt


x = 6 # x = phi/f_a for phi = 6 start

r_tl = 0
omega_tl = 0.1

dx = 0
dr_tl = 0.0001
dz = 0

z = 0


x_list = []
r_list = []



while r_tl < 200:

    print('Rescaled field value: ' + str(x) + '\n')
    print('Rescaled Scalar field: ' + str(r_tl) + '\n')
    print('   ')

    if r_tl == 0:
        y = 0 
    else:
        y = (2/r_tl)*z
    
    dx = z*dr_tl
    dz = (np.sin(x) - ((omega_tl**2)*x) - y)*dr_tl

    x = x + dx
    z = z + dz
    r_tl = r_tl + dr_tl

    x_list.append(x)
    r_list.append(r_tl)



plt.plot(r_list, x_list, color='#008080')
plt.xlabel('Rescaled Radius $\\tilde{r}$',fontsize=22)
plt.ylabel('Rescaled Scalar Field $\phi /f_a$',fontsize=22)
plt.show()