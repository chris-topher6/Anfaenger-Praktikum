import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp
from uncertainties import unumpy
import scipy.constants as const
from scipy.stats import sem
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy.signal import argrelextrema

#Funktionen
def rad(grad): #grad in rad
    return grad*np.pi/180
def grad(rad): #rad in grad
    return rad*180/np.pi
def gerade(x, m, b): #Geraden für Plots
    return m*x+b
def richardson(T, js):
    return -np.log(js/(c1*T**2))*k*T#=e0*Phi mit c1=4*pi*e0*m0*k^2/h^3
def leistung(If, Uf):
    return ((If*Uf-Nwl)/c2)**(1/4)#=T mit c2=f*eta*sigma

#Konstanten der Messung
c1 = 4*np.pi*const.e*const.m_e*const.k**2/const.h**3 # was ist k??
#Messwerte 
Ua, I1, I2, I3, I4, I5 = np.genfromtxt('a.dat', unpack=True)
Uc, Ic                 = np.genfromtxt('c.dat', unpack=True)

#Umrechnung in SI
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
#__________________________________________________________________________________________________________________________________________
#Aufgabe b
print("Aufgabe b")
#__________________________________________________________________________________________________________________________________________
#__________________________________________________________________________________________________________________________________________
#Aufgabe c
print("Aufgabe c")
#__________________________________________________________________________________________________________________________________________
#__________________________________________________________________________________________________________________________________________
#Aufgabe d
print("Aufgabe d")
#__________________________________________________________________________________________________________________________________________
#__________________________________________________________________________________________________________________________________________
#Aufgabe e
print("Aufgabe e")
#__________________________________________________________________________________________________________________________________________