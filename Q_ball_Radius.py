
from Scan_graph_check import E_list
from Scan_graph_check import r_list
from Scan_graph_check import E_val
from Scan_graph_check import Q_val
from Scan_graph_check import x_0

f_a = 10e15 #10e12 for QCD in GeV but converted to MeV
Lambda = 150 #MeV

print('For initial value x(0)=' + str(x_0))
print('\n Energy of Q-ball Plateau = ' + str(E_val))
print('\n Charge of Q-ball Plateau = ' + str(Q_val))
i = 0
energy_val = E_list[i]

Radius_energy = 0.99*E_val

while energy_val < Radius_energy:
    i = i+1
    energy_val = E_list[i]

percentage = energy_val/E_val
resc_Radius = r_list[i]
Radius_MeV = (f_a*resc_Radius)/(Lambda**2)
Radius_length = (197.3/Radius_MeV)*(10e-12) #fm converted to m


if 10e-15 < Radius_length < 10e-12:
    unit = 'fm'
    Radius_length=Radius_length*(10e12)
elif 10e-12 < Radius_length < 10e-9:
    unit = 'pm'
    Radius_length=Radius_length*(10e9)
elif 10e-9 < Radius_length < 10e-6:
    unit = 'micrometers'
    Radius_length=Radius_length*(10e6)
elif 10e-6 < Radius_length < 10e-2:
    unit = 'mm'
    Radius_length=Radius_length*(10e3)
elif 10e-2 < Radius_length < 0:
    unit = 'cm'
    Radius_length=Radius_length*(10e2)
elif 0 < Radius_length < 10e3:
    unit = 'm'
elif 10e3 < Radius_length:
    unit = 'km'
    Radius_length=Radius_length/10e3


print('\n Radius of Q-ball in MeV is ' + str(Radius_length) + unit)
