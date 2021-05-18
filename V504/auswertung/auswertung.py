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
#hier noch die anderen beiden Funktionen ergänzen

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
plt.plot(Ua, I1, 'r', linewidth=0.2)
plt.plot(Ua, I2, 'g', linewidth=0.2)
plt.plot(Ua, I3, 'c', linewidth=0.2)
plt.plot(Ua, I4, 'b', linewidth=0.2)
plt.plot(Ua, I5, 'y', linewidth=0.2)
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