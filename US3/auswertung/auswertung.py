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

def dopplerwinkel(theta):
    return np.pi/2-np.arcsin(np.sin(theta)*cl/cp)

a15 = dopplerwinkel(theta15)
a30 = dopplerwinkel(theta30)
a45 = dopplerwinkel(theta45)

print('Dopplerwinkel')
print(f'a15 = {grad(a15):.4}°')
print(f'a30 = {grad(a30):.4}°')
print(f'a45 = {grad(a45):.4}°')

#############################################################################################################
##Aufgabe1
print()
print('Aufgabe1')
c=(cl+cp)/2                             #das ist so nicht richtig!!! aber vielleicht erstmal keine schlechte Näherung
def stroemung(f, theta):    
    return f*c/(2*f0*np.cos(theta))     #wie kommt man an das c? das sollte sich ja aus cl und cp zusammensetzten oder nicht?


#das hier muss noch ordentlich repariert werden 

print()
print('Aufgabe2')
plt.figure()#Plot
x=np.linspace(-600, 500)
params15s, covariance_matrix15s=np.polyfit(f15s/np.cos(a15), stroemung(f15s, theta15), deg=1, cov=True)
params30s, covariance_matrix30s=np.polyfit(f30s/np.cos(a30), stroemung(f30s, theta30), deg=1, cov=True)
params45s, covariance_matrix45s=np.polyfit(f45s/np.cos(a45), stroemung(f45s, theta45), deg=1, cov=True)
plt.plot(x/np.cos(a15), gerade(x/np.cos(a15), *params15s), "k", label="Regression")
plt.plot(x/np.cos(a30), gerade(x/np.cos(a30), *params30s), "k", label="Regression")
plt.plot(x/np.cos(a45), gerade(x/np.cos(a45), *params45s), "k", label="Regression")
plt.plot(f15s/np.cos(a15), stroemung(f15s, theta15), '.', label='Messdaten')
plt.plot(f30s/np.cos(a30), stroemung(f15s, theta30), '.', label='Messdaten')
plt.plot(f45s/np.cos(a45), stroemung(f15s, theta45), '.', label='Messdaten')
plt.xlabel(r"$???$")
plt.ylabel(r"$???$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot1.pdf')

#############################################################################################################
##Aufgabe2