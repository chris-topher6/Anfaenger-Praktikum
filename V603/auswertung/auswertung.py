import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp
import scipy.constants as const
from scipy.stats import sem
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

a, N  = np.genfromtxt('EmissionCu.dat', unpack=True)

#grad in rad
a     = a*np.pi/180

#gerade für die Plots
def gerade(x, m, b):
    return m*x+b

############################################################################################################
#Aufgabe1
print()
print("Aufgabe 1")

plt.figure()#Plot
x=np.linspace(np.min(a), np.max(a))
plt.plot(a ,N, '.', label='Messdaten')
plt.xlabel(r"$\alpha [rad]$")
plt.ylabel(r"$N [Imp/s]$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot1.pdf')
