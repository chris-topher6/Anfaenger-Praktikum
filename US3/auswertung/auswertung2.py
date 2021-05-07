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


#Herrausnahme der Ausreißer
v_stroem45neu = v_stroem45[np.where(v_stroem45!=0)] 
I45neu        = I45[np.where(I45<400000)]
dvneu         = d[np.where(d>13*0.000001)]
dIneu         = d[np.where(d<19*0.000001)]

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

print()
print('Aufgabe1')
c=(cl+cp)/2                                     #das ist so nicht richtig!!! aber vielleicht erstmal keine schlechte Näherung

def doppler(f, a):
    return f/np.cos(a)
def stroemung(f, theta): #Strömgeschwindigkeit 
    return (c/2)*(f/f0)/np.cos(theta)             #wie kommt man an das c? das sollte sich ja aus cl und cp zusammensetzten oder nicht?

#Parameter
print('Die Parameter der Regression sind:')
params15s, cov15s = np.polyfit(v_pump, doppler(f15s, a15), deg=1, cov=True) #s
params30s, cov30s = np.polyfit(v_pump, doppler(f30s, a30), deg=1, cov=True)
params45s, cov45s = np.polyfit(v_pump, doppler(f45s, a45), deg=1, cov=True)
params15m, cov15m = np.polyfit(v_pump, doppler(f15m, a15), deg=1, cov=True) #m
params30m, cov30m = np.polyfit(v_pump, doppler(f30m, a30), deg=1, cov=True)
params45m, cov45m = np.polyfit(v_pump, doppler(f45m, a45), deg=1, cov=True)
params15l, cov15l = np.polyfit(v_pump, doppler(f15l, a15), deg=1, cov=True) #l
params30l, cov30l = np.polyfit(v_pump, doppler(f30l, a30), deg=1, cov=True)
params45l, cov45l = np.polyfit(v_pump, doppler(f45l, a45), deg=1, cov=True)
errs15s = np.sqrt(np.diag(cov15s))
errs30s = np.sqrt(np.diag(cov30s))
errs45s = np.sqrt(np.diag(cov45s))
errs15m = np.sqrt(np.diag(cov15m))
errs30m = np.sqrt(np.diag(cov30m))
errs45m = np.sqrt(np.diag(cov45m))
errs15l = np.sqrt(np.diag(cov15l))
errs30l = np.sqrt(np.diag(cov30l))
errs45l = np.sqrt(np.diag(cov45l))

#Parameter als ufloat
params15s0 = ufloat(params15s[0], errs15s[0]) #s
params15s1 = ufloat(params15s[1], errs15s[1])
params30s0 = ufloat(params30s[0], errs30s[0])
params30s1 = ufloat(params30s[1], errs30s[1])
params45s0 = ufloat(params45s[0], errs45s[0])
params45s1 = ufloat(params45s[1], errs45s[1])
params15m0 = ufloat(params15m[0], errs15m[0]) #m
params15m1 = ufloat(params15m[1], errs15m[1])
params30m0 = ufloat(params30m[0], errs30m[0])
params30m1 = ufloat(params30m[1], errs30m[1])
params45m0 = ufloat(params45m[0], errs45m[0])
params45m1 = ufloat(params45m[1], errs45m[1])
params15l0 = ufloat(params15l[0], errs15l[0]) #l
params15l1 = ufloat(params15l[1], errs15l[1])
params30l0 = ufloat(params30l[0], errs30l[0])
params30l1 = ufloat(params30l[1], errs30l[1])
params45l0 = ufloat(params45l[0], errs45l[0])
params45l1 = ufloat(params45l[1], errs45l[1])

print(f'a15s = {params15s0}\t\tHz/rpm') #s
print(f'b15s = {params15s1}\tHz')
print(f'a30s = {params30s0}\t\tHz/rpm')
print(f'b30s = {params30s1}\tHz')
print(f'a45s = {params45s0}\t\tHz/rpm')
print(f'b45s = {params45s1}\tHz')
print(f'a15m = {params15m0}\t\tHz/rpm') #m
print(f'b15m = {params15m1}\t\tHz')
print(f'a30m = {params30m0}\t\tHz/rpm')
print(f'b30m = {params30m1}\tHz')
print(f'a45m = {params45m0}\t\tHz/rpm')
print(f'b45m = {params45m1}\tHz')
print(f'a15l = {params15l0}\t\tHz/rpm') #l
print(f'b15l = {params15l1}\t\tHz')
print(f'a30l = {params30l0}\t\tHz/rpm')
print(f'b30l = {params30l1}\t\tHz')
print(f'a45l = {params45l0}\t\tHz/rpm')
print(f'b45l = {params45l1}\t\tHz')

#Plots
plt.figure()#Plot 15
x=np.linspace(np.min(v_pump), np.max(v_pump))
plt.plot(x, gerade(x, *params15s), 'r', label="Regression 7mm")
plt.plot(x, gerade(x, *params15m), 'g', label="Regression 10mm")
plt.plot(x, gerade(x, *params15l), 'b', label="Regression 16mm")
plt.plot(v_pump, doppler(f15s, a15), 'r.',  label='Messdaten 7mm')
plt.plot(v_pump, doppler(f15m, a15), 'g.',  label='Messdaten 10mm')
plt.plot(v_pump, doppler(f15l, a15), 'b.',  label='Messdaten 16mm')
plt.xlabel(r"$v_{pump} [rpm]$")
plt.ylabel(r"$\Delta\nu/cos(\pi/12)[Hz]$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot1.pdf')

plt.figure()#Plot 30
plt.plot(x, gerade(x, *params30s), 'r', label="Regression")
plt.plot(x, gerade(x, *params30m), 'g', label="Regression")
plt.plot(x, gerade(x, *params30l), 'b', label="Regression")
plt.plot(v_pump, doppler(f30s, a30), 'r.',  label='Messdaten 7mm')
plt.plot(v_pump, doppler(f30m, a30), 'g.',  label='Messdaten 10mm')
plt.plot(v_pump, doppler(f30l, a30), 'b.',  label='Messdaten 16mm')
plt.xlabel(r"$v_{pump} [rpm]$")
plt.ylabel(r"$\Delta\nu/cos(\pi/6)[Hz]$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot2.pdf')

plt.figure()#Plot 45
plt.plot(x, gerade(x, *params45s), 'r', label="Regression 7mm")
plt.plot(x, gerade(x, *params45m), 'g', label="Regression 10mm")
plt.plot(x, gerade(x, *params45l), 'b', label="Regression 16mm")
plt.plot(v_pump, doppler(f45s, a45), 'r.',  label='Messdaten 7mm')
plt.plot(v_pump, doppler(f45m, a45), 'g.',  label='Messdaten 10mm')
plt.plot(v_pump, doppler(f45l, a45), 'b.',  label='Messdaten 16mm')
plt.xlabel(r"$v_{pump} [rpm]$")
plt.ylabel(r"$\Delta\nu/cos(\pi/4)[Hz]$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot3.pdf')

#############################################################################################################
##Aufgabe2
print()
print('Aufgabe2')

#Parameter
print('Die Parameter der Regression sind:')
params45V,    cov45V    = np.polyfit(d,       v_stroem45,     deg=1, cov=True)
params45Vneu, cov45Vneu = np.polyfit(dvneu,   v_stroem45neu,  deg=1, cov=True)
params70V,    cov70V    = np.polyfit(d,       v_stroem70,     deg=1, cov=True)
params45I,    cov45I    = np.polyfit(d,       I45,            deg=1, cov=True)
params45Ineu, cov45Ineu = np.polyfit(dIneu,   I45neu,         deg=1, cov=True)
params70I,    cov70I    = np.polyfit(d,       I70,            deg=1, cov=True)
errs45V    = np.sqrt(np.diag(cov45V))
errs45Vneu = np.sqrt(np.diag(cov45Vneu))
errs70V    = np.sqrt(np.diag(cov70V))
errs45I    = np.sqrt(np.diag(cov45I))
errs45Ineu = np.sqrt(np.diag(cov45Ineu))
errs70I    = np.sqrt(np.diag(cov70I))

params45V0    = ufloat(params45V[0],    errs45V[0])
params70V0    = ufloat(params70V[0],    errs70V[0])
params45I0    = ufloat(params45I[0],    errs45I[0])
params70I0    = ufloat(params70I[0],    errs70I[0])
params45V1    = ufloat(params45V[1],    errs45V[1])
params70V1    = ufloat(params70V[1],    errs70V[1])
params45I1    = ufloat(params45I[1],    errs45I[1])
params70I1    = ufloat(params70I[1],    errs70I[1])
params45V0neu = ufloat(params45Vneu[0], errs45Vneu[0])
params45I0neu = ufloat(params45Ineu[0], errs45Ineu[0])
params45V1neu = ufloat(params45Vneu[1], errs45Vneu[1])
params45I1neu = ufloat(params45Ineu[1], errs45Ineu[1])

print(f'a45V    = {params45V0}    \t m/s^2  ')
print(f'b45V    = {params45V1}    \t m/s    ')
print(f'a45Vneu = {params45V0neu} \t\t m/s^2  ')
print(f'b45Vneu = {params45V1neu} \t m/s    ')
print(f'a70V    = {params70V0}    \t\t m/s^2  ')
print(f'b70V    = {params70V1}    \t\t m/s    ')
print(f'a45I    = {params45I0}    \t V^2/s^2')
print(f'b45I    = {params45I1}    \t V^2/s  ')
print(f'a45Ineu = {params45I0neu} \t V^2/s^2')
print(f'b45Ineu = {params45I1neu} \t V^2/s  ')
print(f'a70I    = {params70I0}    \t V^2/s^2')
print(f'b70I    = {params70I1}    \t V^2/s  ')

#Plot
plt.figure()#v_stroem
x=np.linspace(np.min(d), np.max(d))
xvneu=np.linspace(np.min(dvneu), np.max(dvneu))
xIneu=np.linspace(np.min(dIneu), np.max(dIneu))

plt.plot(x,     gerade(x,     *params45V),     'gray',  label="Regression 45%")
plt.plot(xvneu, gerade(xvneu, *params45Vneu),  'r',     label="bereinigt 45%")
plt.plot(x,     gerade(x,     *params70V),     'g',     label="Regression 70%")
plt.plot(d,     v_stroem45,                    'r.',    label='Messdaten 45%')
plt.plot(d[0],  v_stroem45[0],                 'r*',    label='Ausreißer 45%')
plt.plot(d[1],  v_stroem45[1],                 'r*')    
plt.plot(d,     v_stroem70,                    'g.',    label='Messdaten 70%')
plt.xlabel(r"$d [s]$")
plt.ylabel(r"$v_{ström}[m/s]$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot4.pdf')

plt.figure()#v_stroem
plt.plot(x, gerade(x, *params45I),            'gray',  label="Regression 45%")
plt.plot(xIneu, gerade(xIneu, *params45Ineu), 'r',     label="bereinigt 45%")
plt.plot(x, gerade(x, *params70I),            'g',     label="Regression 70%")
plt.plot(d,     I45,                          'r.',    label='Messdaten 45%')
plt.plot(d[7],  I45[7],                       'r*',    label='Ausreißer 45%')
plt.plot(d,     I70,                          'g.',    label='Messdaten 70%')
plt.xlabel(r"$d [s]$")
plt.ylabel(r"$I [V^2/s]$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot5.pdf')