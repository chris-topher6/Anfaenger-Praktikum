import matplotlib.pyplot as plt 
import numpy as np 
import scipy.constants as const
import sympy 
from sympy import *
from uncertainties import ufloat

I, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt('data/stat.dat', unpack=True)
#hier bei der Reihnfolge unbedingt überpüfen!!!

t=I/5
plt.plot(t, T1, 'k.', markersize=1, label='Messing breit')
plt.plot(t, T4, 'g.', markersize=1, label='Messing schmal')
plt.plot(t, T5, 'b.', markersize=1, label='Aluminium')
plt.plot(t, T8, 'r.', markersize=1, label='Edelstahl')
plt.xlabel('t/$s$')
plt.ylabel('T/ °C')
plt.legend(loc='best')
plt.savefig('build/plot1.pdf')

plt.figure()
plt.plot(t, T2-T1, 'k.', markersize=1, label='Messing breit')
plt.plot(t, T7-T8, 'b.', markersize=1, label='Edelstahl')
plt.xlabel('t/$s$')
plt.ylabel('$\Delta T_{St}$/ °C')
plt.legend(loc='best')
plt.savefig('build/plot2.pdf')

np.savetxt('build/intervalla.txt',np.column_stack( [t, T1, T2, T3, T4, T5, T6, T7, T8] ), fmt='%10.2f' , delimiter='&',header='t statisch', newline='\\\\\n' )

np.savetxt('build/tabelle1.txt',np.column_stack( [ T1[139],T4[139],T5[139],T8[139] ] ), fmt='%10.2f' , delimiter='&',header='T(700s) T1 T4 T5 T8', newline='\\\\\n' )
d_x=0.03
k_messing=120 #W/mk
rho_messing=8520 #kg/m^3
c_messing=377
A_messingb=0.012*0.004
A_messings=0.007*0.004
k_aluminium=235
rho_aluminium=2800 #kg/m^3
c_aluminium=897
A_aluminium=0.012*0.004
k_edelstahl=21
rho_edelstahl=8000 #kg/m^3
c_edelstahl=400
A_edelstahl=0.012*0.004

#zeitpunkte: 100s, 200s, 300s, 400s, 500s
i=np.array([19,39,59,79,99])                #n/5-1
j=0
while j < 5:
    dQ=np.array([-k_messing*A_messingb*(T2[i[j]]-T1[i[j]])/d_x, -k_messing*A_messings*(T3[i[j]]-T4[i[j]])/d_x,-k_aluminium*A_aluminium*(T6[i[j]]-T5[i[j]])/d_x,  -k_edelstahl*A_edelstahl*(T7[i[j]]-T8[i[j]])/d_x])
    j=j+1
    print(dQ)

j=0
while j<5:
    print(f"{T2[i[j]]-T1[i[j]]:.3},{T3[i[j]]-T4[i[j]]:.3},{T6[i[j]]-T5[i[j]]:.3},{T7[i[j]]-T8[i[j]]:.3}")  
    j=j+1

print()
print(f"T1: {T1[19]+273.15:.4},{T1[39]+273.15:.4},{T1[59]+273.15:.4},{T1[79]+273.15:.4},{T1[99]+273.15:.4}")
print(f"T4: {T4[19]+273.15:.4},{T4[39]+273.15:.4},{T4[59]+273.15:.4},{T4[79]+273.15:.4},{T4[99]+273.15:.4}")
print(f"T5: {T5[19]+273.15:.4},{T5[39]+273.15:.4},{T5[59]+273.15:.4},{T5[79]+273.15:.4},{T5[99]+273.15:.4}")
print(f"T8: {T8[19]+273.15:.4},{T8[39]+273.15:.4},{T8[59]+273.15:.4},{T8[79]+273.15:.4},{T8[99]+273.15:.4}")
print()
