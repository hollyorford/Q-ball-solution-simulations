while r_tl < 25:
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
    
    eq_ratio = E/Q
    eq_ratio_list.append(eq_ratio)
