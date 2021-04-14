import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp
import scipy.constants as const
from scipy.stats import sem
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

a1, b1             = np.genfromtxt('Reflexion.dat', unpack=True)
a2, b2             = np.genfromtxt('Brechung1.dat', unpack=True)
a3, b3             = np.genfromtxt('Brechung2.dat', unpack=True)
a4, b4g, b4r = np.genfromtxt('Prisma.dat', unpack=True)

#grad in rad
a1=a1*np.pi/180
a2=a2*np.pi/180
a3=a3*np.pi/180
a4=a4*np.pi/180
b1=b1*np.pi/180
b2=b2*np.pi/180
b3=b3*np.pi/180
b4g=b4g*np.pi/180
b4r=b4r*np.pi/180

#gerade für die Plots
def gerade(x, m, b):
    return m*x+b

############################################################################################################
#Aufgabe1
print()
print("Aufgabe 1")

plt.figure()#Plot
x=np.linspace(np.min(a1), np.max(a1))
params,covariance_matrix=np.polyfit(a1, b1, deg=1, cov=True)
plt.plot(x, gerade(x, *params), "k", label="Regression")
plt.plot(a1 ,b1, '.', label='Messdaten')
plt.xlabel(r"$\alpha_1 [rad]$")
plt.ylabel(r"$\alpha_2 [rad]$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot1.pdf')

print("Die Parameter der ersten Regression sind:")
i          = 0
h          = ufloat(0,0)
paramserr1 = np.array([h, h])
errors     = np.sqrt(np.diag(covariance_matrix))
for name, value, error in zip('ab', params, errors):
    paramserr1[i]=ufloat(value, error)
    print(f'{name} = {value:.8f} ± {error:.8f}')
    i      = i+1

############################################################################################################
#Aufgabe2
print()
print("Aufgabe 2")

n   =  np.sin(a2)/np.sin(b2) #n berechnen
nm  =  np.mean(n)
nf  =  sem(n)
nu  =  ufloat(nm,nf)
nid =  1.4931 #vergleichen mit Literatur
p   =  100*(nid-n)/nid

plt.figure() #Plot von n
x=np.linspace(np.min(a2), np.max(a2))
params,covariance_matrix=np.polyfit(a2, n, deg=1, cov=True)
plt.plot(x, gerade(x, *params), "k", label="Regression")
plt.plot(a2, n, '.', label='Messdaten')
plt.xlabel(r"$\alpha [rad]$")
plt.ylabel(r"$n$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot2.pdf')

print("Die Parameter der zweiten Regression sind:")
i         = 0 #Ausgeben der Parameter
h         = ufloat(0,0)
paramserr2 = np.array([h, h])
errors    = np.sqrt(np.diag(covariance_matrix))
for name, value, error in zip('ab', params, errors):
    paramserr2[i]=ufloat(value, error)
    print(f'{name} = {value:.8f} ± {error:.8f}')
    i     = i+1

c   = 2.9979*10**8 #berechnen der Lichtgeschwindigkeit
v   = c/nu
print(f'Die Lichtgeschwindigkeit in Plexiglas beträgt: v={v}')
print("Der Brechungsindex beträgt: ", nu)
############################################################################################################
#Aufgabe3
print()
print("Aufgabe 3")

d   = 5.85*10**(-3)
s1  = d*np.sin(a3-b3)/np.cos(b3)     #Strahlenversatz Methode 1
b31 = np.arcsin(np.sin(a3)/nm)       #Strahlenversatz Methode 2
s2  = d*np.sin(a3-b31)/np.cos(b31)
p   = 100*(s1-s2)/s1                 #vergleichen

plt.figure()                         #Plot
x=np.linspace(np.min(a3), np.max(a3))
params3,covariance_matrix3   =   np.polyfit(a3, s1*1000, deg=1, cov=True)
params4,covariance_matrix4   =   np.polyfit(a3, s2*1000, deg=1, cov=True)
plt.plot(x, gerade(x, *params3), color='green',                   label='Regression s_1')
plt.plot(x, gerade(x, *params4), color='red',                     label='Regression s_2')
plt.plot(a4, s1*1000, '.',       color='orange',  markersize = 3, label='s_1')
plt.plot(a4, s2*1000, '.',       color='blue',    markersize = 3, label='s_2')
plt.xlabel(r"$\alpha [rad]$")
plt.ylabel(r"$s [mm]$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot3.pdf')

print("Die Parameter der dritten Regression sind:")
i          = 0
h          = ufloat(0,0)
paramserr3 = np.array([h, h])
errors     = np.sqrt(np.diag(covariance_matrix3))
for name, value, error in zip('ab', params3, errors):
    paramserr3[i]=ufloat(value, error)
    print(f'{name} = {value:.8f} ± {error:.8f}')
    i      = i+1
i          = 0
h          = ufloat(0,0)
paramserr4 = np.array([h, h])
errors     = np.sqrt(np.diag(covariance_matrix4))
for name, value, error in zip('ab', params4, errors):
    paramserr4[i]=ufloat(value, error)
    print(f'{name} = {value:.8f} ± {error:.8f}')
    i      = i+1

print(f'Strahlenversatz Methode 1: s1  = {s1}')
print(f'Strahlenversatz Methode 2: s2  = {s2}')
print(f'Prozentuale Abweichung   : p   = {p }')
#Speichern in .txt
np.savetxt("strahlenversatz.txt", np.column_stack([s1*1000, s2*1000, p]), fmt = "%10.2f", delimiter = " & ", header = " s1/mm, s2/mm, p/%")

############################################################################################################
#Aufgabe4
print()
print("Aufgabe 4")

nkron  = 1.61282
g      = 60
k1    = np.arcsin(np.sin(a4)/nkron) #in Prismaskizze: beta1=k1
deltag = (a4+b4g)-(2*k1-g)          #grün
deltar = (a4+b4r)-(2*k1-g)          #rot

plt.figure()                         #Plot von Ablenkung
x=np.linspace(np.min(a4), np.max(a4))
paramsg,covariance_matrixg   =   np.polyfit(a4, deltag, deg=1, cov=True)
paramsr,covariance_matrixr   =   np.polyfit(a4, deltar, deg=1, cov=True)
plt.plot(x, gerade(x, *paramsg), color='green',   label='Regression grün')
plt.plot(x, gerade(x, *paramsr), color='red',     label='Regression rot')
plt.plot(a4, deltag, '.',        color='orange',  label='Messdaten grün')
plt.plot(a4, deltar, '.',        color='blue',    label='Messdaten rot')
plt.xlabel(r"$\alpha [rad]$")
plt.ylabel(r"$\delta [rad]$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot4.pdf')

print("Die Parameter der vierten Regression sind:")
i          = 0
h          = ufloat(0,0)
paramserrg = np.array([h, h])
errors     = np.sqrt(np.diag(covariance_matrixg))
for name, value, error in zip('ab', paramsg, errors):
    paramserrg[i]=ufloat(value, error)
    print(f'{name} = {value:.8f} ± {error:.8f}')
    i      = i+1
i          = 0
h          = ufloat(0,0)
paramserrr = np.array([h, h])
errors     = np.sqrt(np.diag(covariance_matrixr))
for name, value, error in zip('ab', paramsr, errors):
    paramserrr[i]=ufloat(value, error)
    print(f'{name} = {value:.8f} ± {error:.8f}')
    i      = i+1
############################################################################################################s
#Aufgabe5
print()
print("Aufgabe 5")
