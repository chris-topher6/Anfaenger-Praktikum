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
def unsicherheit(f): #Sollte für arrays erweitert werden
    return ufloat(f, 10)

#Konstanten der Messung
f0      = 2    * 10**(6)   #1/s
ro      = 1.15 * 10**(3)   #kg/m^3
cl      = 1800             #m/s
n       = 12   * 10**(-3)  #Pas
cp      = 2700             #m/s
l       = 30.7 * 10**(-3)  #m
r1      = 7    * 10**(-3)  #m
r2      = 10   * 10**(-3)  #m
r3      = 16   * 10**(-3)  #m
theta15 = rad(15)          #rad
theta30 = rad(30)          #rad
theta45 = rad(45)          #rad

#Messwerte
v_pump, f15s, f30s, f45s = np.genfromtxt('a-dünn.dat',   unpack=True)
v_pump, f15m, f30m, f45m = np.genfromtxt('a-mittel.dat', unpack=True)
v_pump, f15l, f30l, f45l = np.genfromtxt('a-dick.dat',   unpack=True)
d, v_stroem45, I45       = np.genfromtxt('b-45%.dat',    unpack=True)
d, v_stroem70, I70       = np.genfromtxt('b-70%.dat',    unpack=True)

#in SI-Einheiten
v_stroem45  = v_stroem45 * 0.001    #m/s
v_stroem70  = v_stroem70 * 0.001    #m/s
I45         = I45        * 1000     #V^2/s
I70         = I70        * 1000     #V^2/s
d           = d          * 0.000001 #s
#f      [1/s]
#V_pump [rpm]

#############################################################################################################
##Vorbereitung
print()
print('Vorbereitung')

def alpha(theta): #Dopplerwinkel
    return np.pi/2-np.arcsin(np.sin(theta)*cl/cp)

a15 = alpha(theta15)
a30 = alpha(theta30)
a45 = alpha(theta45)

print('Dopplerwinkel')
print(f'a15 = {grad(a15):.4}°')
print(f'a30 = {grad(a30):.4}°')
print(f'a45 = {grad(a45):.4}°')

#############################################################################################################
##Aufgabe1

"""
Das Problem bei der Aufgabe ist, dass die Plots sich komplett im Kreis drehen. Das erklärt auch den extrem niedrigen Fehler und das b
praktisch null ist. Die einzige Information die man in die Plots rein steckt sind nämlich die f. Alles andere sind Konstanten. Denn sowohl
die x-, als auch die y-Achse setzten sich Konstanten mal f zusammen. Von daher sind alle Plots nicht aussagekräftig!
"""
print()
print('Aufgabe1')
c=(cl+cp)/2                                     #das ist so nicht richtig!!! aber vielleicht erstmal keine schlechte Näherung

def doppler(f, a):
    return f/np.cos(a)
def stroemung(f, theta): #Strömgeschwindigkeit 
    return (c/2)*(f/f0)/np.cos(theta)             #wie kommt man an das c? das sollte sich ja aus cl und cp zusammensetzten oder nicht?

#Parameter
print('Die Parameter der Regression sind:')
params15s, cov15s = np.polyfit(doppler(f15s, a15), stroemung(f15s, a15), deg=1, cov=True) #Parameter berechnen
errs15s     = np.sqrt(np.diag(cov15s))
params30s, cov30s = np.polyfit(doppler(f30s, a30), stroemung(f30s, a30), deg=1, cov=True)
errs30s     = np.sqrt(np.diag(cov30s))
params45s, cov45s = np.polyfit(doppler(f45s, a45), stroemung(f45s, a45), deg=1, cov=True)
errs45s     = np.sqrt(np.diag(cov45s))

params15s0=ufloat(params15s[0], errs15s[0]) #Parameter als ufloat
params15s1=ufloat(params15s[1], errs15s[1])
params30s0=ufloat(params30s[0], errs30s[0])
params30s1=ufloat(params30s[1], errs30s[1])
params45s0=ufloat(params45s[0], errs45s[0])
params45s1=ufloat(params45s[1], errs45s[1])

print(f'a15={params15s0}') #Ausgabe
print(f'b15={params15s1}')
print(f'a30={params30s0}')
print(f'b30={params30s1}')
print(f'a45={params45s0}')
print(f'b45={params45s1}')

#Plots
plt.figure()#Plot 15s
x=np.linspace(-600, 500)
x15=np.linspace(-3000, -1600) 
plt.plot(x15, gerade(x15, *params15s), 'r', label="Regression")
plt.plot(doppler(f15s, a15), stroemung(f15s, a15), 'r.', label='Messdaten')
plt.xlabel(r"$\Delta\nu/cos(\pi/12)$")
plt.ylabel(r"v [m/s]")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot1.pdf')

plt.figure()#Plot 30s
x30=np.linspace(1300, 2500)
plt.plot(x30, gerade(x30, *params30s), 'g', label="Regression")
plt.plot(doppler(f30s, a30), stroemung(f30s, a30), 'g.', label='Messdaten')
plt.xlabel(r"$\Delta\nu/cos(\pi/6)$")
plt.ylabel(r"v [m/s]")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot2.pdf')

plt.figure()#Plot 45s
x45=np.linspace(-3060, -1560)
plt.plot(x45, gerade(x45, *params45s), 'b', label="Regression")
plt.plot(doppler(f45s, a45), stroemung(f45s, a45), 'b.', label='Messdaten')
plt.xlabel(r"$\Delta\nu/cos(\pi/4)$")
plt.ylabel(r"v [m/s]")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot3.pdf')

#############################################################################################################
##Aufgabe2
print()
print('Aufgabe2')