import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import unumpy
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy.stats import sem
from scipy.optimize import curve_fit
from scipy import optimize
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

#Messdaten einlesen
x1, A1 = np.genfromtxt("skript/einzelspalt.dat", unpack=True) #in mm und mikro Ampere
x2, A2 = np.genfromtxt("skript/doppelspalt.dat", unpack=True) #in mm und mikro Ampere

#Dunkelstrom
dunkelstrom = 1.35 #in nano Ampere
dunkelstrom = dunkelstrom*10**(-3) #in mikro Ampere

#Korrektur des Dunkelstroms
A1 = A1-dunkelstrom
A2 = A2-dunkelstrom

#Wellenlänge des Lasers
lambdalaser = 663*10**(-9) #in m umgerechnet

#Umrechnung in m
x1, x2 = x1*10**(-3), x2*10**(-3)

#Berechnung des Beugungswinkels
def beugungswinkel(l, l0, L):
    phi = (l-l0)/L
    return(phi)

phi1 = beugungswinkel(x1, 25.5*10**(-3), 1.25)
phi2 = beugungswinkel(x2, 25.5*10**(-3), 1.25)
phi11 = phi1[1:60]
phi22 = phi2[1:60]
A11  = A1[1:60]
A22  = A2[1:60]

#Theoretische Verteilung für den Einzelspalt
def theorieeinzel(phi,b, a):
    teil1=(a**2)*(b**2)*((lambdalaser/(np.pi*b*np.sin(phi)))**2)
    teil2=(np.sin((np.pi*b*np.sin(phi))/lambdalaser))**2
    return(teil1*teil2)

#Theoretische Verteilung für den Doppelspalt
def theoriedoppel(phi, b, A_0, s):
    teil1=(A_0**2)*np.cos((np.pi*s*np.sin(phi)/lambdalaser))**2
    teil2=(lambdalaser/(np.pi*b*np.sin(phi)))**2
    teil3=np.sin((np.pi*b*np.sin(phi))/lambdalaser)**2
    return(teil1*teil2*teil3)

#Fit der Theorie an die Messwerte des Einzelspaltes
params, covariance = curve_fit(theorieeinzel, phi11, A11, p0=[0.00015, 70])
errors = np.sqrt(np.diag(covariance))
print("Spaltbreite: ", params[0],'+-',errors[0])
print("Abweichung", abweichung(params[0],0.00015), "%")
print("A_0:", params[1],'+-',errors[1])

#Fit der Theorie an die Messwerte des Doppelspaltes
params2, covariance2 =curve_fit(theoriedoppel, phi22, A22, p0=[0.00015,10, 0.00065])
errors2 = np.sqrt(np.diag(covariance2))
print("Spaltbreite: ", params2[0],'+-',errors2[0])
print("Abweichung", abweichung(params2[0],0.00015), "%")
print("A_0:", params2[1],'+-',errors2[1])
print(params2[2], '+-', errors2[2])

#Plotte Verteilung für Einzelspalt
#plt.plot(x1, A1, "r+", label="Messreihe Einzespalt")
#plt.plot(xx1, theorieeinzel(xx1, *params), label="Fit der Theoriekurve")
#plt.xlabel("APosition des Detektors [mm]")
#plt.ylabel("Intensität [A]")
#plt.savefig("plot1.pdf")
#plt.close()

#Plotte Verteilung für den Doppelspalt
#plt.plot(x2, A2, label="Messreihe Doppelspalt")
#plt.xlabel("Position des Detektors [mm]")
#plt.ylabel("Intensität [A]")
#plt.savefig("plot2.pdf")
#plt.close()
