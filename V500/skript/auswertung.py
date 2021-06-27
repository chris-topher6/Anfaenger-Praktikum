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
errors1 = np.sqrt(np.diag(cov1))
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
plt.clf()


#Fit an Blaugrün
params2, cov2 = np.polyfit(U_blaugrün, np.sqrt(I_blaugrün), deg=1, cov=True)
errors2 = np.sqrt(np.diag(cov2))
#x-Werte für Plot der Regressionsgeraden
x2 = np.linspace(-1, 2, num=30)
#Plot der Regressionsgeraden
plt.plot(x2, params2[0]*x2+params2[1], "r", label="Lineare Regression", linewidth=1)
#Plot der Messwerte
plt.plot(U_blaugrün, np.sqrt(I_blaugrün),  "k.", label="Blaugrün", linewidth=1)
plt.xlabel(r"$U_{Blaugruen} $")
plt.ylabel(r"$\sqrt{I_{Blaugruen}} $")
plt.legend()
plt.savefig("build/plotblaugrün.pdf")
plt.clf()

#Fit an Blau
params3, cov3 = np.polyfit(U_blau, np.sqrt(I_blau), deg=1, cov=True)
errors3 = np.sqrt(np.diag(cov3))
#x-Werte für Plot der Regressionsgeraden
x3 = np.linspace(-1.4, 2, num=34)
#Plot der Regressionsgeraden
plt.plot(x3, params3[0]*x3+params3[1], "r", label="Lineare Regression", linewidth=1)
#Plot der Messwerte
plt.plot(U_blau, np.sqrt(I_blau),  "k.", label="Blau", linewidth=1)
plt.xlabel(r"$U_{Blau} $")
plt.ylabel(r"$\sqrt{I_{Blau}} $")
plt.legend()
plt.savefig("build/plotblau.pdf")
plt.clf()

#Fit an Gelb
params4, cov4 = np.polyfit(U_gelb[0:12], np.sqrt(I_gelb[0:12]), deg=1, cov=True)
errors4 = np.sqrt(np.diag(cov4))
#x-Werte für Plot der Regressionsgeraden
x4 = np.linspace(-0.2, 20, num=21)
#Plot der Regressionsgeraden
plt.plot(x4, params4[0]*x4+params4[1], "r", label="Lineare Regression", linewidth=1)
#Plot der Messwerte
plt.plot(U_gelb, np.sqrt(I_gelb),  "k.", label="Gelb", linewidth=1)
plt.xlabel(r"$U_{Gelb} $")
plt.ylabel(r"$\sqrt{I_{Gelb}} $")
plt.legend()
plt.savefig("build/plotgelb.pdf")
plt.clf()
