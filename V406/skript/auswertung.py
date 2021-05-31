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

#Kleines Beispiel für das Abspeichern
print('test')
plt.figure()
x = np.linspace(0, 1)
plt.plot(x, x**2)
plt.savefig('build/test.pdf')