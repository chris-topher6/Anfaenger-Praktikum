import matplotlib.pyplot as plt 
import numpy as np 
import scipy.constants as const
import sympy 
from sympy import *
from uncertainties import ufloat

#Konstanten
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

print()
##########################################################################################################################################
#erste Messung

I, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt('data/dyn1.dat', unpack=True)
#I, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt('data/d1.dat', unpack=True)

t=2*I 
np.savetxt('build/intervallb.txt',np.column_stack( [t, T1, T2, T3, T4, T5, T6, T7, T8] ), fmt='%10.2f' , delimiter='&',header='t statisch', newline='\\\\\n' )


plt.figure()
plt.plot(I*2, T1, 'k.', markersize=1, label = '$T_{fern}$')
plt.plot(I*2, T2, 'r.', markersize=1, label = '$T_{nah}$')
plt.xlabel('t/$s$')
plt.ylabel('T/ °C')
plt.legend(loc='best')
#plt.grid()
plt.savefig('build/plot3.pdf')


plt.figure()
plt.plot(I*2, T5, 'k.', markersize=1, label = '$T_{fern}$')
plt.plot(I*2, T6, 'r.', markersize=1, label = '$T_{nah}$')
plt.xlabel('t/$s$')
plt.ylabel('T/ °C')
plt.legend(loc='best')
#plt.grid()
plt.savefig('build/plot4.pdf')

#########################################################################################################################################
#zweite Messung

#I, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt('data/d2.dat', unpack=True)
I, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt('data/dyn2.dat', unpack=True)

t=2*I 
np.savetxt('build/intervallc.txt',np.column_stack( [t, T1, T2, T3, T4, T5, T6, T7, T8] ), fmt='%10.2f' , delimiter='&',header='t statisch', newline='\\\\\n' )

plt.figure()
plt.plot(I*2, T7, 'k.', markersize=1, label = '$T_{nah}$')
plt.plot(I*2, T8, 'r.', markersize=1, label = '$T_{fern}$')
plt.xlabel('t/$s$')
plt.ylabel('T/ °C')
plt.legend(loc='best')
#plt.grid()
plt.savefig('build/plot5.pdf')

#Amplituden:
A1=np.array([3.83,4.23,4.16,3.39,3.96,3.60,3.31,3.08,2.91,2.73])
A1_m=np.mean(A1)
A1_s=np.std(A1, ddof=1)

A2=np.array([9.94,9.47,9.08,8.09,8.71,8.24,7.89,7.63,7.47,7.28])
A2_m=np.mean(A2)
A2_s=np.std(A2, ddof=1)

ln12=np.log(A2_m/A1_m)
#ln12=np.log(A2/A1)
dt12=np.array([18,18,18,18,18,16,14,16,16,14])

A5=np.array([7.53,7.23,6.72,5.53, 6.23,5.70,5.36,5.09,4.90,4.77])
A5_m=np.mean(A5)
A5_s=np.std(A5, ddof=1)

A6=np.array([10.83,10.46,9.97,8.81,9.46,9.23,8.61,8.34,8.19,8.06])
A6_m=np.mean(A6)
A6_s=np.std(A6, ddof=1)

ln56=np.log(A6_m/A5_m)
dt56=np.array([10,10,10,10,10,8,8,8,8,8])

A7=np.array([21.04, 17.61, 16.91,16.32])
A7_m=np.mean(A7)
A7_s=np.std(A7, ddof=1)

A8=np.array([6.65,5.01,4.04,3.50])
A8_m=np.mean(A8)
A8_s=np.std(A8, ddof=1)

ln78=np.log(A7_m/A8_m)
dt78=np.array([88,82,70,64])


dt12_m=np.mean(dt12)
dt56_m=np.mean(dt56)
dt78_m=np.mean(dt78)

dt12_s=np.std(dt12, ddof=1)
dt56_s=np.std(dt56, ddof=1)
dt78_s=np.std(dt78, ddof=1)


np.savetxt('build/tabelle2.txt',np.column_stack( [ A1_m, A1_s, A2_m,A2_s, ln12, dt12_m ,dt12_s] ), fmt='%10.2f' , delimiter='&',header='A1 A2 ln dt', newline='\\\\\n' )
np.savetxt('build/tabelle3.txt',np.column_stack( [ A5_m, A5_s, A6_m,A6_s, ln56, dt56_m ,dt56_s] ), fmt='%10.2f' , delimiter='&',header='A5 A6 ln dt', newline='\\\\\n' )
np.savetxt('build/tabelle4.txt',np.column_stack( [ A7_m, A7_s,A8_m,A8_s, ln78, dt78_m ,dt78_s] ), fmt='%10.2f' , delimiter='&',header='A7 A8 ln dt', newline='\\\\\n' )


k12=(rho_messing*c_messing*d_x**2)/(2*dt12_m*ln12)
k56=(rho_aluminium*c_aluminium*d_x**2)/(2*dt56_m*ln56)
k78=(rho_edelstahl*c_edelstahl*d_x**2)/(2*dt78_m*ln78)

k12_neu=(rho_messing*c_messing*d_x**2)/(2*dt12*np.log(A2/A1))
print('k12 neu:' ,k12_neu)
k56_neu=(rho_aluminium*c_aluminium*d_x**2)/(2*dt56*np.log(A6/A5))
print('k56 neu:' ,k56_neu)
k78_neu=(rho_edelstahl*c_edelstahl*d_x**2)/(2*dt78*np.log(A7/A8))
print('k78 neu:' ,k78_neu)
#np.savetxt('tabelle5.txt',np.column_stack( [ ln12_mean, ln12_std, dt12_mean, dt12_std,k12,ln56_mean, ln56_std, dt56_mean, dt56_std ,k56,ln78_mean, ln78_std, dt78_mean, dt78_std, k78 ] ), fmt='%10.2f' , delimiter='&',header='ln fehler dt fehler k von Messing, Aluminium und Edelstahl', newline='\\\\\n' )
np.savetxt('build/tabelle5.txt',np.column_stack( [ k12,k56,k78 ] ), fmt='%10.2f' , delimiter='&',header=' k von Messing, Aluminium und Edelstahl', newline='\\\\\n' )

#d_k12=np.sqrt(((rho_messing*c_messing*d_x**2)/(dt12_mean*ln12_mean**2))**2*ln12_std**2+((rho_messing*c_messing*d_x**2)/(dt12_mean**2*ln12_mean))**2*dt12_std**2)
d_k12=np.sqrt(((rho_messing*c_messing*d_x**2)/(2*dt12_m*ln12**2*A2_m))**2*A2_s**2+((rho_messing*c_messing*d_x**2)/(2*dt12_m*ln12**2*A1_m))**2*A1_s**2+((rho_messing*c_messing*d_x**2)/(dt12_m**2*ln12))**2*dt12_s**2)
#print(d_k12)

#d_k56=np.sqrt(((rho_aluminium*c_aluminium*d_x**2)/(dt56_mean*ln56_mean**2))**2*ln56_std**2+((rho_aluminium*c_aluminium*d_x**2)/(dt56_mean**2*ln56_mean))**2*dt56_std**2)
d_k56=np.sqrt(((rho_aluminium*c_aluminium*d_x**2)/(2*dt56_m*ln56**2*A5_m))**2*A5_s**2+((rho_aluminium*c_aluminium*d_x**2)/(2*dt56_m*ln56**2*A6_m))**2*A6_s**2+((rho_aluminium*c_aluminium*d_x**2)/(dt56_m**2*ln56))**2*dt56_s**2)
#print(d_k56)

#d_k78=np.sqrt(((rho_edelstahl*c_edelstahl*d_x**2)/(dt78_mean*ln78_mean**2))**2*ln78_std**2+((rho_edelstahl*c_edelstahl*d_x**2)/(dt78_mean**2*ln78_mean))**2*dt78_std**2)
d_k78=np.sqrt(((rho_edelstahl*c_edelstahl*d_x**2)/(2*dt78_m*ln78**2*A7_m))**2*A7_s**2+((rho_edelstahl*c_edelstahl*d_x**2)/(2*dt78_m*ln78**2*A8_m))**2*A8_s**2+((rho_edelstahl*c_edelstahl*d_x**2)/(dt78_m**2*ln78))**2*dt78_s**2)
#print(d_k78)

k_1=ufloat(k12, d_k12)
k_5=ufloat(k56, d_k56)
k_7=ufloat(k78, d_k78)

#v_1=((2*k_1)/(80*rho_messing*c_messing))**0.5
#v_5=((2*k_5)/(80*rho_aluminium*c_aluminium))**0.5
#v_7=((2*k_7)/(200*rho_edelstahl*c_edelstahl))**0.5

l_1=((4*np.pi *k_1*80)/(rho_messing*c_messing))**0.5
l_5=((4*np.pi *k_5*80)/(rho_aluminium*c_aluminium))**0.5
l_7=((4*np.pi *k_7*80)/(rho_edelstahl*c_edelstahl))**0.5

print()
print(f"d_k12={d_k12:.4}")
print(f"d_k56={d_k56:.4}")
print(f"d_k78={d_k78:.4}")
print()
print(f"l_1={l_1:.4}")
print(f"l_5={l_5:.4}")
print(f"l_7={l_7:.4}")
print()