import matplotlib.pyplot as plt 
import numpy as np 
import scipy.constants as const
import sympy 
from sympy import *
from uncertainties import ufloat
from scipy.signal import find_peaks

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

t=I/2 
np.savetxt('build/intervallb.txt',np.column_stack( [t, T1, T2, T3, T4, T5, T6, T7, T8] ), fmt='%10.2f' , delimiter='&',header='t statisch', newline='\\\\\n' )

#Amplituden 
#print()
#print(find_peaks(T1, height=0))
#print()

plt.figure()
plt.plot(I/2, T1, 'k.', markersize=1, label = '$T_{fern}$')
plt.plot(I/2, T2, 'r.', markersize=1, label = '$T_{nah}$')
plt.xlabel('t/$s$')
plt.ylabel('T/ °C')
plt.legend(loc='best')
#plt.grid()
plt.savefig('build/plot3.pdf')


plt.figure()
plt.plot(I/2, T5, 'k.', markersize=1, label = '$T_{fern}$')
plt.plot(I/2, T6, 'r.', markersize=1, label = '$T_{nah}$')
plt.xlabel('t/$s$')
plt.ylabel('T/ °C')
plt.legend(loc='best')
plt.grid()
plt.savefig('build/plot4.pdf')

#########################################################################################################################################
#zweite Messung

#I, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt('data/d2.dat', unpack=True)
I, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt('data/dyn2.dat', unpack=True)

t=I/2 
np.savetxt('build/intervallc.txt',np.column_stack( [t, T1, T2, T3, T4, T5, T6, T7, T8] ), fmt='%10.2f' , delimiter='&',header='t statisch', newline='\\\\\n' )

plt.figure()
plt.plot(I/2, T7, 'k.', markersize=1, label = '$T_{nah}$')
plt.plot(I/2, T8, 'r.', markersize=1, label = '$T_{fern}$')
plt.xlabel('t/$s$')
plt.ylabel('T/ °C')
plt.legend(loc='best')
plt.grid()
plt.savefig('build/plot5.pdf')

#Amplituden:

A1max=np.array([34.06, 40.15, 44.77, 48.52, 51.65, 54.30, 56.54, 57.61, 59.51, 61.11])
A1min=np.array([33.96, 39.58, 43.85, 47.34, 50.26, 52.73, 54.86, 55.69, 57.67, 59.19])
A1=A1max-A1min
A1_m=np.mean(A1)
A1_s=np.std(A1, ddof=1)
A2max=np.array([41.64, 47.72, 52.15, 55.83, 58.97, 61.63, 63.85, 63.97, 66.98, 68.51])
A2min=np.array([35.65, 40.80, 44.88, 48.26, 51.14, 53.63, 55.79, 56.42, 58.64, 60.20])
A2=A2max-A2min
A2_m=np.mean(A2)
A2_s=np.std(A2, ddof=1)
argA1max=np.array([228, 373, 531, 686, 845, 1005, 1166, 1316, 1486, 1646])
argA2max=np.array([171, 332, 493, 654, 815,  976, 1137, 1279, 1459, 1619])
dt12=0.5*np.abs(argA1max-argA2max)


A5max=np.array([40.22, 47.83, 52.33, 55.75, 58.56, 61.11, 63.02, 63.15, 65.61, 67.25])
A5min=np.array([37.96, 43.87, 47.80, 50.90, 53.53, 55.82, 57.82, 57.97, 60.30, 61.89])
A5=A5max-A5min
A5_m=np.mean(A5)
A5_s=np.std(A5, ddof=1)
A6max=np.array([46.6 , 53.7 , 57.98, 61.32, 64.14, 66.58, 68.60, 68.33, 71.37, 72.92])
A6min=np.array([37.54, 42.97, 46.78, 49.85, 52.46, 54.79, 56.81, 57.08, 59.40, 60.98])
A6=A6max-A6min
A6_m=np.mean(A6)
A6_s=np.std(A6, ddof=1)
argA5max=np.array([190, 345, 504, 664, 825, 986, 1147, 1302, 1469, 1630])
argA6max=np.array([167, 328, 489, 650, 811, 972, 1133, 1274, 1455, 1616])
dt56=0.5*np.abs(argA5max-argA6max)

A7max=np.array([57.79, 64.39, 69.56, 73.49, 76.50, 78.65, 80.35, 81.74])
A7min=np.array([42.04, 47.86, 52.49, 56.02, 58.68, 60.63, 62.17, 63.28])
A7=A7max-A7min
A7_m=np.mean(A7)
A7_s=np.std(A7, ddof=1)
A8max=np.array([36.13, 42.08, 46.91, 50.79, 53.91, 56.25, 58.12, 59.63])
A8min=np.array([36.03, 41.66, 46.19, 49.79, 52.61, 54.73, 56.41, 57.77])
A8=A8max-A8min
A8_m=np.mean(A8)
A8_s=np.std(A8, ddof=1)
argA7max=np.array([416, 815, 1218, 1619, 2022, 2425, 2826, 3229])
argA8max=np.array([578, 957, 1344, 1735, 2132, 2530, 2926, 3327])
dt78=0.5*np.abs(argA7max-argA8max)

ln12=np.log(A2_m/A1_m)
ln56=np.log(A6_m/A5_m)
ln78=np.log(A7_m/A8_m)


dt12_m=np.mean(dt12)
dt56_m=np.mean(dt56)
dt78_m=np.mean(dt78)

dt12_s=np.std(dt12, ddof=1)
dt56_s=np.std(dt56, ddof=1)
dt78_s=np.std(dt78, ddof=1)

dt12_u=ufloat(dt12_m, dt12_s)
dt56_u=ufloat(dt56_m, dt56_s)
dt78_u=ufloat(dt78_m, dt78_s)

np.savetxt('build/tabelle2.txt',np.column_stack( [ A1_m, A1_s, A2_m,A2_s, ln12, dt12_m ,dt12_s] ), fmt='%10.2f' , delimiter='&',header='A1 A2 ln dt', newline='\\\\\n' )
np.savetxt('build/tabelle3.txt',np.column_stack( [ A5_m, A5_s, A6_m,A6_s, ln56, dt56_m ,dt56_s] ), fmt='%10.2f' , delimiter='&',header='A5 A6 ln dt', newline='\\\\\n' )
np.savetxt('build/tabelle4.txt',np.column_stack( [ A7_m, A7_s, A8_m,A8_s, ln78, dt78_m ,dt78_s] ), fmt='%10.2f' , delimiter='&',header='A7 A8 ln dt', newline='\\\\\n' )

k12=(rho_messing*c_messing*d_x**2)/(2*dt12_u*ln12)
k56=(rho_aluminium*c_aluminium*d_x**2)/(2*dt56_u*ln56)
k78=(rho_edelstahl*c_edelstahl*d_x**2)/(2*dt78_u*ln78)

k12_neu=(rho_messing*c_messing*d_x**2)/(2*dt12*np.log(A2/A1))
print('k12 neu:' ,k12_neu)
print()
k56_neu=(rho_aluminium*c_aluminium*d_x**2)/(2*dt56*np.log(A6/A5))
print('k56 neu:' ,k56_neu)
print()
k78_neu=(rho_edelstahl*c_edelstahl*d_x**2)/(2*dt78*np.log(A7/A8))
print('k78 neu:' ,k78_neu)

#np.savetxt('tabelle5.txt',np.column_stack( [ ln12_mean, ln12_std, dt12_mean, dt12_std,k12,ln56_mean, ln56_std, dt56_mean, dt56_std ,k56,ln78_mean, ln78_std, dt78_mean, dt78_std, k78 ] ), fmt='%10.2f' , delimiter='&',header='ln fehler dt fehler k von Messing, Aluminium und Edelstahl', newline='\\\\\n' )
np.savetxt('build/tabelle5.txt',np.column_stack( [ k12.n, k12.s, k56.n, k56.s, k78.n, k78.s ] ), fmt='%10.2f' , delimiter='&',header=' k von Messing, Aluminium und Edelstahl mit Unsicherheit', newline='\\\\\n' )

#Ronjas manuelle Berechnung der Unsicherheiten
#   #d_k12=np.sqrt(((rho_messing*c_messing*d_x**2)/(dt12_mean*ln12_mean**2))**2*ln12_std**2+((rho_messing*c_messing*d_x**2)/(dt12_mean**2*ln12_mean))**2*dt12_std**2)
#   d_k12=np.sqrt(((rho_messing*c_messing*d_x**2)/(2*dt12_m*ln12**2*A2_m))**2*A2_s**2+((rho_messing*c_messing*d_x**2)/(2*dt12_m*ln12**2*A1_m))**2*A1_s**2+((rho_messing*c_messing*d_x**2)/(dt12_m**2*ln12))**2*dt12_s**2)
#   #print(d_k12)
#   
#   #d_k56=np.sqrt(((rho_aluminium*c_aluminium*d_x**2)/(dt56_mean*ln56_mean**2))**2*ln56_std**2+((rho_aluminium*c_aluminium*d_x**2)/(dt56_mean**2*ln56_mean))**2*dt56_std**2)
#   d_k56=np.sqrt(((rho_aluminium*c_aluminium*d_x**2)/(2*dt56_m*ln56**2*A5_m))**2*A5_s**2+((rho_aluminium*c_aluminium*d_x**2)/(2*dt56_m*ln56**2*A6_m))**2*A6_s**2+((rho_aluminium*c_aluminium*d_x**2)/(dt56_m**2*ln56))**2*dt56_s**2)
#   #print(d_k56)
#   
#   #d_k78=np.sqrt(((rho_edelstahl*c_edelstahl*d_x**2)/(dt78_mean*ln78_mean**2))**2*ln78_std**2+((rho_edelstahl*c_edelstahl*d_x**2)/(dt78_mean**2*ln78_mean))**2*dt78_std**2)
#   d_k78=np.sqrt(((rho_edelstahl*c_edelstahl*d_x**2)/(2*dt78_m*ln78**2*A7_m))**2*A7_s**2+((rho_edelstahl*c_edelstahl*d_x**2)/(2*dt78_m*ln78**2*A8_m))**2*A8_s**2+((rho_edelstahl*c_edelstahl*d_x**2)/(dt78_m**2*ln78))**2*dt78_s**2)
#   #print(d_k78)
#   
#   k_1=ufloat(k12.n, d_k12)
#   k_5=ufloat(k56.n, d_k56)
#   k_7=ufloat(k78.n, d_k78)

#v_1=((2*k_1)/(80*rho_messing*c_messing))**0.5
#v_5=((2*k_5)/(80*rho_aluminium*c_aluminium))**0.5
#v_7=((2*k_7)/(200*rho_edelstahl*c_edelstahl))**0.5

l12=((4*np.pi *k12*80)/(rho_messing*c_messing))**0.5
l56=((4*np.pi *k56*80)/(rho_aluminium*c_aluminium))**0.5
l78=((4*np.pi *k78*80)/(rho_edelstahl*c_edelstahl))**0.5

print()
print(f"k12={k12:.4}")
print(f"k56={k56:.4}")
print(f"k78={k78:.4}")
print()
print(f"l12={l12:.4}")
print(f"l56={l56:.4}")
print(f"l78={l78:.4}")
print()