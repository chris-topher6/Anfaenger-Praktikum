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
V_al= 0.520**2 * 59.3            #cm^3
#V_al= 1.3208**2*59.3
V_fe= 0.505**2 * 59.3            #cm^3
#V_fe= 1.2827**2 * 59.3
V_me= (0.52/2)**2 * np.pi *60.2  #cm^3
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