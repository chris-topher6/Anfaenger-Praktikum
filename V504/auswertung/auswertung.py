import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp
from uncertainties import unumpy
import scipy.constants as const
from scipy.stats import sem
from scipy.optimize import curve_fit
from scipy import optimize
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy.signal import argrelextrema

#Funktionen
def rad(grad):
    return grad*np.pi/180
def grad(rad):
    return rad*180/np.pi
def gerade(x, m, b):
    return m*x+b
def abweichung(lit, mess):
    return abs(100*(lit-mess)/lit)

def richardson(T, js):
    return -np.log(js/(c1*T**2))*k*T/const.e#=Phi mit c1=4*pi*e0*m0*k^2/h^3
def leistung(Uf, If):
    return ((If*Uf-Nwl)/c2)**(1/4)#=T mit c2=f*eta*sigma
def langschott(V, ex):
    return c3*V**(ex)#=j mit c3=4/9*epsilon0*sqrt(2e0/m0)/a

#Naturkonstanten
e = const.value('electron volt')
k = const.value('Boltzmann constant')
h = const.value('Planck constant')
m = const.value('electron mass')

#Konstanten der Messung
Nwl   = 0.95 #W
sigma = 5.7  * 10**(-8) #W/m^2K^4
f1    = 0.32 * 10**(-4) #m
f2    = 0.35 * 10**(-4) #m
eta   = 0.28
a     = 0.01                                                    #"""m ????????? nochmal nachfragen!!!"""
Ri    = 10**6           #Ohm
c1    = 4*np.pi*e*m*k**2/h**3
c2    = f1*eta*sigma                                            #"""welches f soll man nehmen???"""
c3    = 4/9*const.epsilon_0*np.sqrt(2*const.e/const.m_e)/a

#Messwerte 
Ua, I1, I2, I3, I4, I5 = np.genfromtxt('a.dat', unpack=True)
Uf, If                 = np.genfromtxt('c.dat', unpack=True)
Uc, Ic                 = np.genfromtxt('d.dat', unpack=True)

#Umrechnung in SI
I1 = I1*10**(-3)
I2 = I2*10**(-3)
I3 = I3*10**(-3)
I4 = I4*10**(-3)
I5 = I5*10**(-3)
Ic = Ic*10**(-9)

#__________________________________________________________________________________________________________________________________________
#Aufgabe a
print("Aufgabe a")
plt.figure()
plt.plot(Ua, I1, 'r.', label='I=2.1')
plt.plot(Ua, I2, 'g.', label='I=2.2')
plt.plot(Ua, I3, 'c.', label='I=2.3')
plt.plot(Ua, I4, 'b.', label='I=2.4')
plt.plot(Ua, I5, 'y.', label='I=2.5')
plt.plot(Ua, I1, 'r', linewidth=0.08)
plt.plot(Ua, I2, 'g', linewidth=0.08)
plt.plot(Ua, I3, 'c', linewidth=0.08)
plt.plot(Ua, I4, 'b', linewidth=0.08)
plt.plot(Ua, I5, 'y', linewidth=0.08)
plt.xlabel(r"Anodenspannung $U_a [V]$")
plt.ylabel(r"Anodenstromstärke $I_a [A]$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot1.pdf')

print('der Sättigungsstrom Is ist')
print(f'für 2.1: {0.28}')
print(f'für 2.2: {0.65}')
print(f'für 2.3: {1.18}')
print(f'für 2.4: {2.12}')#Wendepunkt ist in etwa bei (125, 1.06) => Is=2*1.06=2.12
print(f'für 2.5: {3.12}')#Wendepunkt ist in etwa bei (150, 1.56) => Is=2*1.56=3.12

#__________________________________________________________________________________________________________________________________________
#Aufgabe b
print("\nAufgabe b")
#der Wp ist bei (150, 1.56) => das Raumladungsgebiet ist im Intervall [0, 150]
Uaneu = Ua[np.where(Ua<151)] #zuschneiden der Arrays auf das Intervall
I5neu = I5[np.where(I5<1.57*10**(-3))]

#  normale Darstellung
#  #Exponenten fitten
#  params, cov = curve_fit(langschott, Uaneu, I5neu)
#  errs        = np.sqrt(np.diag(cov))
#  params_err  = ufloat(params, errs)
#  
#  #Literaturwert
#  lit         = 1.5
#  p           = 100*(lit-params)/lit
#  
#  #Plot
#  plt.figure()
#  x = np.linspace(np.min(Uaneu), np.max(Uaneu))
#  plt.plot(x, langschott(x, params), 'g', label='Regression')
#  plt.plot(Ua, I5, 'k.', label='I=2.5')
#  plt.xlabel(r"Anodenspannung $U_a [V]$")
#  plt.ylabel(r"Anodenstromstärke $I_a [mA]$")
#  plt.legend(loc='best')
#  plt.tight_layout()
#  plt.savefig('plot2.pdf')

#Doppellog-Darstellung
x = np.log(Uaneu)
y = np.log(I5neu)

param, cov = np.polyfit(x, y, deg=1, cov=True)
err        = np.sqrt(np.diag(cov))
print('Die Parameter der Regression sind:')
for name, value, error in zip('ab', param, err):
    print(f'{name} = {value:.3f} +- {error:.5f}')

exponent   = ufloat(param[0], err[0])

plt.figure()
x_plot = np.linspace(np.min(x), np.max(x))
plt.plot(x_plot, gerade(x_plot, *param), 'b-', label='Regression')
plt.plot(x, y, 'r.', label='Messwerte')
plt.xlabel(r'$\log{(U/V)}$')
plt.ylabel(r'$\log{(I/A)}$')
plt.legend()
plt.savefig('plot2-2.pdf')

print(f"der Exponent des Langmuir-Schottkyschen Gesetzes ist nach der Regression: \nex={exponent}")
print(f"die Abweichung vom Literaturwert beträgt: p={abweichung(3/2, param[0]):.4}%")

#__________________________________________________________________________________________________________________________________________
#Aufgabe c
print("\nAufgabe c")

x  = Uc+Ic/Ri
y  = np.log(Ic*10**(-9))

param, cov = np.polyfit(x, y, deg=1, cov=True)
err = np.sqrt(np.diag(cov))
print('Die Parameter der Regression sind:')
for name, value, error in zip('ab', param, err):
    print(f'{name} = {value:.3f} +- {error:.5f}')

plt.figure()
x_plot = np.linspace(np.min(x), np.max(x))
plt.plot(x_plot, gerade(x_plot, *param), 'b-', label='Fit')
plt.plot(x, y, 'r.', label='Messwerte')
plt.xlabel(r'$U \,/\, \mathrm{V}$')
plt.ylabel(r'$\log{(I)}$')
plt.legend()
plt.savefig('plot3.pdf')

paramerr0 = ufloat(param[0], err[0])
T         = e/(k*paramerr0)
print(f'Die Temperatur beträgt nach dem Anlaufstromgebiet: T={T:.6}K')

#__________________________________________________________________________________________________________________________________________
#Aufgabe d
print("\nAufgabe d")

Uf=Uf+If/Ri
T  = leistung(Uf, If)
print("Die Temperaturen betragen nach der Leistungsbilanz:")
print(f'{T[0]:.2f}')
print(f'{T[1]:.2f}')
print(f'{T[2]:.2f}')
print(f'{T[3]:.2f}')
print(f'{T[4]:.2f}')

#__________________________________________________________________________________________________________________________________________
#Aufgabe e
print("\nAufgabe e")

Is   = [0.28, 0.65, 1.18, 2.12, 3.12]
phi  = richardson(T,Is)
phim = ufloat(np.mean(phi), sem(phi))
lit  = 4.54 #https://www.spektrum.de/lexikon/physik/austrittsarbeit/1067

print(f'Austrittsarbeit Wolfram: Phi={phim}')
print(f'Abweichung: p={abweichung(lit, np.mean(phi)):.4}%')
#__________________________________________________________________________________________________________________________________________