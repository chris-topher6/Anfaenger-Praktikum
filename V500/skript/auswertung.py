import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
import scipy.constants as const
import tools
import pint
ureg = pint.UnitRegistry()
ureg.setup_matplotlib()
from uncertainties import ufloat
from uncertainties import unumpy
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy.stats import sem
from scipy.optimize import curve_fit
from scipy import optimize
from scipy.signal import argrelextrema
from scipy.signal import find_peaks, peak_widths
#Wichtig um zu verhindern dass Matplotlib xLabels oder yLabels abschneidet
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

#Daten importieren
U_grün, I_grün = np.genfromtxt("Data/gruen.dat", unpack=True)
U_blaugrün, I_blaugrün = np.genfromtxt("Data/blaugruen.dat", unpack=True)
U_violett1, I_violett1 = np.genfromtxt("Data/violett1.dat", unpack=True)
U_violett2, I_violett2 = np.genfromtxt("Data/violett2.dat", unpack=True)
U_blau, I_blau = np.genfromtxt("Data/blau.dat", unpack=True)
U_gelb, I_gelb = np.genfromtxt("Data/gelb.dat", unpack=True)

#Fit an Grün
params1, cov1 = np.polyfit(U_grün, np.sqrt(I_grün), deg=1, cov=True)
errors = np.sqrt(np.diag(cov1))
#x-Werte für Plot der Regressionsgeraden
x1 = np.linspace(-1, 2.5, num=35)
#Plot der Regressionsgeraden
plt.plot(x1, params1[0]*x1+params1[1], "r", label="Lineare Regression", linewidth=1)
#Plot der Messwerte
plt.plot(U_grün, np.sqrt(I_grün),  "k.", label="Grün", linewidth=1)
plt.xlabel(r"$U_{Gruen} $")
plt.ylabel(r"$\sqrt{I_{gruen}} $")
plt.legend()
plt.savefig("build/plotgrün.pdf")
a= [0]
#Nullstellenberechnung
for i in range(0, (len(x1))):
    a[i] = params1[0]*x1[i]+params1[1]
    if i == 0:
        if a[i] < 0 and a[i+1] > 0:
            print("Die Nullstelle liegt zwischen ", a[i], " und ", a[i+1], ".")
    if i > 0:
        if a[i-1] < 0 and a[i] > 0:
            print("Die Nullstelle liegt zwischen ", a[i-1], " und ", a[i], ".")
