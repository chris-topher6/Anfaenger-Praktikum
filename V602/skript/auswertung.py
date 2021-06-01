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

#Konstanten
e   = const.e
Ryd = 13.6 # eV
R_y = ureg.h * ureg.c * ureg.R_inf # Rydberg-Energie
a   = const.alpha
#d   = 201.4*10**(-12)
d = ureg('201.4 pm') # Gitterebenenabstand
h = ureg.h
c = ureg.c

# etwas lesbarer so, finde ich
def sqrt(x):
    return x**.5

#Vorbereitungsaufgaben
print("Vorbereitungsaufgabe:")
Z, theta, E = np.genfromtxt("data/Vorbereitung.dat", unpack=True)
theta = tools.rad(theta)
E     = E*10**3

sigma = Z-np.sqrt(E/Ryd-a**2*Z**4/4)
i=0
while(i<6):
    print(f"sigma={sigma[i]:.3f}")
    i=i+1

#_____________________________________________________________________________________________________________________________
#Aufgabe 1
print("\nAufgabe 1")
theta, N = np.genfromtxt("data/Bragg.dat", unpack=True)
#theta = tools.rad(theta)
i_max  = argrelextrema(N, np.greater, order=20)[0]

plt.figure()
plt.plot(theta, N, 'b.', label='Messdaten')
plt.plot(theta[i_max], N[i_max], 'r.', label='Maximum')
plt.xlabel(r'$\theta [°]$')
plt.ylabel('N [Imps/s]')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot1.pdf')

#Theoriewert
theta_theorie = 28
p = tools.abweichung(theta_theorie, theta[i_max])

print(f"Max: ({theta[i_max]}, {N[i_max]})")
print(f"Theorie: {theta_theorie}")
print(f"Abweichung von {p}%")

#_____________________________________________________________________________________________________________________________
#Aufgabe 2
print("\nAufgabe 2")
theta, N = np.genfromtxt('data/Emissionsspektrum.dat', unpack=True)
theta *= ureg.deg

#K-Linien
peak_indices, _ = find_peaks(N, height=1000)
assert len(peak_indices) == 2

peaks = theta[peak_indices]

print(tools.fmt_compare_to_ref(peaks[1], ureg('22.323 °'), name="θ_Kα"))
print(tools.fmt_compare_to_ref(peaks[0], ureg('20.217 °'), name="θ_Kβ"))

#Halbwertsbreite
results_half = peak_widths(N, peak_indices, rel_height=0.5) 
w_h, l, r = results_half[1:]   
# TODO hard-coden ist doof :/
l = (l/10 + 8) * ureg.deg
r = (r/10 + 8) * ureg.deg
print(f"Halbwertsbreiten: {(r-l):.3f}°")

#Energien
def energie(theta):
    return (h * c / (2 * d * np.sin(theta.to('rad')))).to('keV') 
E = energie(peaks)
dE = energie(l)-energie(r)
print(f"Energien für die Peaks: {E:.2f}")
print(f"Energiedifferenzen über die Halbwertsbreiten: {dE:.3f}")
print(f"Auflösungsvermögen: {E/dE:.2f}")

Z = 29 # für Kupfer
sigma_K = (Z - (E/(1*ureg.h * ureg.c * ureg.R_inf) - (((1*ureg.α)**2 * Z**4) / 4))**.5).to('dimensionless')

E_abs = ufloat(8987.96, 15) * ureg('eV') # → NIST Wo kommt das her?
E_a = E[1]
E_b  = E[0]
assert E_a < E_b

# nach Formeln von YanickKi
sigma_1 = Z - sqrt(E_abs / R_y)
sigma_2 = Z - 2 * sqrt((Z - sigma_1)**2 - (E_a / R_y))
sigma_3 = Z - 3 * sqrt((Z - sigma_1)**2 - (E_b  / R_y))

print(f"sigma1={sigma_1}")
print(f"sigma2={sigma_2}")
print(f"sigma3={sigma_3}")

plt.figure()
#plt.hlines(w_h, l, r, color="green", label='Halbwertsbreiten')
#K-Linien
plt.scatter([20.2], [1599.0], s=25, marker='o', color='red')
plt.scatter([22.5], [5050.0], s=25, marker='o', color='red')
plt.plot([20.2, 20.2], [0, 1599.0], color='red', linestyle='--')
plt.plot([22.5, 22.5], [0, 5050.0], color='red', linestyle='--')
plt.annotate(r'$K_{\beta}$',
            xy = (20.2, 1599.0), xycoords='data', xytext=(-50, -10),
            textcoords='offset points', fontsize=12,
            arrowprops=dict(arrowstyle="->"))
plt.annotate(r'$K_{\alpha}$',
            xy = (22.5, 5050.0), xycoords='data', xytext=(+35, -10),
            textcoords='offset points', fontsize=12,
            arrowprops=dict(arrowstyle="->"))
#Bremsberg
plt.scatter([11.1], [420.0], s=25, marker='o', color='red')
plt.annotate(r'Bremsberg', 
            xy = (11.1, 420.0), xycoords='data', xytext=(-10, 20),
            textcoords='offset points', fontsize=12, 
            arrowprops=dict(arrowstyle="->"))
plt.plot(theta, N, 'b.', label='Messdaten')
plt.xlabel(r'$θ \;[°]$')
plt.ylabel(r'$N$')
plt.legend()
plt.tight_layout()
plt.savefig('build/plot2.pdf')

#_____________________________________________________________________________________________________________________________
#Aufgabe 3
print("\nAufgabe 3")
thetaZn, NZn = np.genfromtxt('data/Zink.dat'     , unpack=True)
thetaGe, NGe = np.genfromtxt('data/Gallium.dat'  , unpack=True)
thetaBr, NBr = np.genfromtxt('data/Brom.dat'     , unpack=True)
thetaRb, NRb = np.genfromtxt('data/Rubidium.dat' , unpack=True)
thetaSr, NSr = np.genfromtxt('data/Strontium.dat', unpack=True)
thetaZr, NZr = np.genfromtxt('data/Zirkonium.dat', unpack=True)

plt.figure()
plt.plot(thetaZn, NZn, 'b.', label='Messdaten Zn')
plt.xlabel(r'$θ \;[°]$')
plt.ylabel(r'$N$')
plt.savefig('build/Zn.pdf')

plt.figure()
plt.plot(thetaGe, NGe, 'g.', label='Messdaten Ge')
plt.xlabel(r'$θ \;[°]$')
plt.ylabel(r'$N$')
plt.savefig('build/Ge.pdf')

plt.figure()
plt.plot(thetaBr, NBr, 'r.', label='Messdaten Br')
plt.xlabel(r'$θ \;[°]$')
plt.ylabel(r'$N$')
plt.savefig('build/Br.pdf')

plt.figure()
plt.plot(thetaRb, NRb, 'c.', label='Messdaten Rb')
plt.xlabel(r'$θ \;[°]$')
plt.ylabel(r'$N$')
plt.savefig('build/Rb.pdf')

plt.figure()
plt.plot(thetaSr, NSr, 'm.', label='Messdaten Sr')
plt.xlabel(r'$θ \;[°]$')
plt.ylabel(r'$N$')
plt.savefig('build/Sr.pdf')

plt.figure()
plt.plot(thetaZr, NZr, 'y.', label='Messdaten Zr')
plt.xlabel(r'$θ \;[°]$')
plt.ylabel(r'$N$')
plt.savefig('build/Zr.pdf')

plt.figure()
plt.plot(thetaZn, NZn, 'b.', label='Messdaten Zn')
plt.plot(thetaGe, NGe, 'g.', label='Messdaten Ge')
plt.plot(thetaBr, NBr, 'r.', label='Messdaten Br')
plt.plot(thetaRb, NRb, 'c.', label='Messdaten Rb')
plt.plot(thetaSr, NSr, 'm.', label='Messdaten Sr')
plt.plot(thetaZr, NZr, 'y.', label='Messdaten Zr')
plt.xlabel(r'$θ \;[°]$')
plt.ylabel(r'$N$')
plt.legend()
plt.tight_layout()
plt.savefig('build/plot3.pdf')

#Mitten der Kanten
