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

#Gewichte
m_al=163.1 #g
m_fe=454.6 #g
m_me=394.1 #g

g_alu1=800
g_fe1=1250
g_me1=550
g_me2=1550

#Volumen berechnen
L_al=59.3 #cm
L_fe=59.3 #cm
L_me=60.2 #cm
V_al= 0.520**2 * L_al            #cm^3
#V_al= 1.3208**2*59.3
V_fe= 0.505**2 * L_fe            #cm^3
#V_fe= 1.2827**2 * 59.3
V_me= (0.52/2)**2 * np.pi * L_me  #cm^3
#V_me= (1.3208/2)**2 * np.pi *60.2 
 
#Dichte
rho_al=m_al/V_al
rho_fe=m_fe/V_fe
rho_me=m_me/V_me

print(f"Dichten der Metalle")
print(f"Al: rho={rho_al:.4}")
print(f"Fe: rho={rho_fe:.4}")
print(f"Me: rho={rho_me:.4}")

#Daten importieren
x1, D_al1 = np.genfromtxt('data/al1.dat',   unpack=True)
x1, D_fe1 = np.genfromtxt('data/fe1.dat',   unpack=True)
x1, D_me1 = np.genfromtxt('data/me1.dat',   unpack=True)
x2, D_me2 = np.genfromtxt('data/me2.dat',   unpack=True)

#Flächenträgheitsmoment

#Funktionen für 8,9,10
def arg8(x, L):
    return L*x**2-x**3
def arg9(x, L):
    return 3*L**2*x-4*x**3
def arg10(x, L):
    return 4*x**3-12*L*x**2+9*L**2*x-L**3

#Regression
params_al8, cov_al8   = np.polyfit(arg8(x1 ,L_al), D_al1, deg=1, cov=True)
params_al9, cov_al9   = np.polyfit(arg9(x1 ,L_al), D_al1, deg=1, cov=True)
params_al10, cov_al10 = np.polyfit(arg10(x1,L_al), D_al1, deg=1, cov=True)

print(params_al8)
print(params_al9)
print(params_al10)

#Plots 
plt.figure()
x=np.linspace(np.min(arg10(x1, L_al)), np.max(arg10(x1, L_al)))
plt.plot(arg8(x , L_al), tools.gerade(arg8(x , L_al), *params_al8),    'r',   label="Regression 8")
plt.plot(arg9(x , L_al), tools.gerade(arg9(x , L_al), *params_al9),    'g',   label="Regression 9")
plt.plot(arg10(x, L_al), tools.gerade(arg10(x, L_al), *params_al10),   'b',   label="Regression 10")
plt.plot(arg8(x1 , L_al), D_al1, 'r.',  label='Messdaten 8')
plt.plot(arg9(x1 , L_al), D_al1, 'g.',  label='Messdaten 9')
plt.plot(arg10(x1, L_al), D_al1, 'b.',  label='Messdaten 10')
plt.xlabel(r"$??$")
plt.ylabel(r"$??$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot1.pdf')