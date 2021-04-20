import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp
import scipy.constants as const
from scipy.stats import sem
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy.signal import argrelextrema

# Konstanten der Messung
t = 90 * 10**(-6) # s Totzeit des GM-Zählers
d = 201.4 * 10**(-12) # m Gitterkonstante LiF
n = 1 # Beugungsordnung

#Literaturwerte
E_alit = 1.541*10**(-10) #m 
E_blit = 1.392*10**(-10) #m 


# Naturkonstanten
h = 4.136*10**(-15) # eV s
c = 2.998*10**(8) # m/s

#############################################################################################################
##Aufgabe1
theta, N = np.genfromtxt('EmissionCu.dat', unpack=True)

#die Stellen der Linien
i_max = argrelextrema(N, np.greater, order=20)[0]
dtheta = np.radians(0.1)
kalpha = theta[i_max[2]]
kbeta = theta[i_max[1]]

#plot1
plt.plot(theta, N, 'b.', label='Messwerte')

#kalpha und kbeta Linien
plt.plot([kbeta, kbeta], [0, 1599.0], color='red', linestyle='--')
plt.plot([kalpha, kalpha], [0, 5050.0], color='red', linestyle='--')
plt.scatter([kbeta], [1599.0], s=25, marker='o', color='red')
plt.scatter([kalpha], [5050.0], s=25, marker='o', color='red')
plt.annotate(r'$K_{\beta}$',
            xy = (kbeta, 1599.0), xycoords='data', xytext=(-50, -10),
            textcoords='offset points', fontsize=12,
            arrowprops=dict(arrowstyle="->"))
plt.annotate(r'$K_{\alpha}$',
            xy = (kalpha, 5050.0), xycoords='data', xytext=(+35, -10),
            textcoords='offset points', fontsize=12,
            arrowprops=dict(arrowstyle="->"))

#Bremsberg
plt.scatter([11.1], [420.0], s=25, marker='o', color='red')
plt.annotate(r'Bremsberg', 
            xy = (11.1, 420.0), xycoords='data', xytext=(-10, 20),
            textcoords='offset points', fontsize=12, 
            arrowprops=dict(arrowstyle="->"))

plt.xlabel(r'$\theta [°]$')
plt.ylabel('N [Imps/s]')
plt.tight_layout()
plt.legend()
plt.savefig('plot1.pdf')
plt.clf()

#zugehörigen Energien
l_alpha = 2*d/n * np.sin(kalpha)      # m Wellenlänge
l_beta  = 2*d/n * np.sin(kbeta)       # m Wellenlänge
E_alpha = h*c/l_alpha                 #eV Photonenenergie
E_beta  = h*c/l_beta                  #eV Photonenenergie
p_alpha = 100*(E_alit-E_alpha)/E_alit # % Abweichung von Literatur
p_beta  = 100*(E_blit-E_beta)/E_blit  # % Abweichung von Literatur

#############################################################################################################
#Aufgabe2

a_0, N_0_ = np.genfromtxt('ComptonOhne.txt', unpack=True)
a_Al, N_Al_ = np.genfromtxt('ComptonAl.txt', unpack=True)


N_0_err = np.sqrt(N_0_)
N_Al_err = np.sqrt(N_Al_)

N_0 = unp.uarray(N_0_, N_0_err)
N_Al = unp.uarray(N_Al_, N_Al_err)

# Totzeitkorrektur
I_o = N_0 / (1 - t * N_0)
I_Al = N_Al / (1 - t * N_Al)

# Transmission bestimmen
T = I_Al / I_o

# calcular taman~o de las ondas

lam = 2 * d * np.sin(a_0 * np.pi / 180)

# crear lineare Regression
params, cov = np.polyfit(lam, unp.nominal_values(T), deg=1, cov=True)
errs = np.sqrt(np.diag(cov))
for name, value, error in zip('ab', params, errs):
    print(f'{name} = {value:.3f} +- {error:.3f}')

# grafico
l_start = 2* d * np.sin(7 * np.pi /180)
l_fin = 2 * d *np.sin(10* np.pi/180)
lam_plot = np.linspace(l_start, l_fin)

plt.clf()
plt.plot(lam, unp.nominal_values(T), 'r.', label='Messwerte')
plt.plot(lam_plot, params[0]*lam_plot + params[1], '-', label='Lineare Regression')
plt.errorbar(lam, unp.nominal_values(T), yerr=unp.std_devs(T), fmt='r_')
plt.legend()
plt.xlabel(r'Wellenlänge $\lambda$')
plt.ylabel(r'Transmission')
plt.savefig('transmission.pdf')

# ----- Compton-Wellenlänge bestimmen ------

# Transmissionen
I_0 = 2731.0
I_1 = 1180.0
I_2 = 1024.0

T_1 = I_1/I_0
T_2 = I_2/I_0

print(f'T_1 = {T_1:.3f}, T_2 = {T_2:.3f}')

# calcular tamanos de ondas correspendientes
lam_1 = (T_1 - params[1])/params[0]
lam_2 = (T_2 - params[1])/params[0]

lam_c = lam_2 - lam_1

print(f'Lambda 1 = {lam_1}')
print(f'Lambda 2 = {lam_2}')
print(f'Compton = {lam_c}')