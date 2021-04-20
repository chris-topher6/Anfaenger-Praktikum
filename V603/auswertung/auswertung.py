import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp
import scipy.constants as const
from scipy.stats import sem
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy.signal import argrelextrema

#gerade für die Plots
def gerade(x, m, b):
    return m*x+b

# Konstanten der Messung
t = 90 * 10**(-6) # s Totzeit des GM-Zählers
d = 201.4 * 10**(-12) # m Gitterkonstante LiF
n = 1 # Beugungsordnung

#Literaturwerte
E_alit = 8.048*10**3 #eV 
E_blit = 8.907*10**3 #eV 

# Naturkonstanten
h = 4.136*10**(-15) # eV s
c = 2.998*10**(8) # m/s

#############################################################################################################
##Aufgabe1 - Plot des Emissionsspektrums
print()
print('Aufgabe1')

theta, N = np.genfromtxt('EmissionCu.dat', unpack=True) #Import

#die Stellen der Linien
i_max  = argrelextrema(N, np.greater, order=20)[0]
dtheta = np.radians(0.1)
kalpha = theta[i_max[2]]
kbeta  = theta[i_max[1]]

#plot1
plt.plot(theta, N, 'b.', label='Messwerte')

#k_alpha und k_beta Linien
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
l_alpha = 2*d/n * np.sin(kalpha*np.pi/180)    # m Wellenlänge
l_beta  = 2*d/n * np.sin(kbeta *np.pi/180)
E_alpha = h*c/l_alpha                         #eV Photonenenergie
E_beta  = h*c/l_beta                      
p_alpha = 100*(E_alit-E_alpha)/E_alit         # % Abweichung von Literatur
p_beta  = 100*(E_blit-E_beta)/E_blit 

#Ausgabe
print(f'Wellenlänge bei K_a: l_a={l_alpha*10**10:.4}Å')
print(f'Wellenlänge bei K_b: l_b={l_beta *10**10:.4}Å')
print(f'Energie bei K_a    : E_a={E_alpha*10**(-3):.4}keV')
print(f'Energie bei K_b    : E_b={E_beta *10**(-3):.4}keV')
print(f'Abweichung von Lit.: p_a={p_alpha:.4}')
print(f'Abweichung von Lit.: p_b={p_beta :.4}')

#############################################################################################################
#Aufgabe2
print()
print('Aufgabe 2')

a_0, N_0_   = np.genfromtxt('ComptonOhne.txt', unpack=True) #Import
a_Al, N_Al_ = np.genfromtxt('ComptonAl.txt', unpack=True)
N_0_err     = np.sqrt(N_0_)                                 #Unsicherheiten
N_Al_err    = np.sqrt(N_Al_)
N_0         = unp.uarray(N_0_, N_0_err)                     #ufloats
N_Al        = unp.uarray(N_Al_, N_Al_err)


I_0  = N_0 /(1-t*N_0)   # Totzeitkorrektur
I_Al = N_Al/(1-t*N_Al)
T    = I_Al/I_0         # Transmission bestimmen

#Wellenlänge
l = 2*d*np.sin(a_0*np.pi/180) #m
l = l*10**12                  #pm

#Regression
params, cov = np.polyfit(l, unp.nominal_values(T), deg=1, cov=True)
errs = np.sqrt(np.diag(cov))

#Plot
x = np.linspace(np.min(l), np.max(l))
plt.plot(l, unp.nominal_values(T), 'b.', label='Messwerte')
plt.plot(x, gerade(x, *params), 'k-', label='Lineare Regression')
plt.errorbar(l, unp.nominal_values(T), yerr=unp.std_devs(T), fmt='.', ecolor='red')
plt.legend()
plt.xlabel(r'$\lambda$ [pm]')
plt.ylabel(r'Transmission')
plt.savefig('plot2.pdf')

#Parameter
print('Die Parameter der Regression sind:')
for name, value, error in zip('ab', params, errs):
    print(f'{name} = {value:.3f} +- {error:.3f}')

#############################################################################################################
#Aufgabe3 - Compton-Wellenlänge bestimmen
print()
print('Aufgabe 3')

I_0 = 2731.0                        #ohne Al-Absorber
I_1 = 1180.0                        #Al-Absorber zwischen Röntgen-Röhre und Streuer
I_2 = 1024.0                        #Al-Absorber zwischen Streuer und Zählrohr

T_1 = I_1/I_0                       #Transmissionen
T_2 = I_2/I_0

l1 = (T_1 - params[1])/params[0]    #entsprechende Wellengröße
l2 = (T_2 - params[1])/params[0]

dl = l2 - l1

#Ausgabe
print(f'T_1 = {T_1:.3f}, T_2 = {T_2:.3f}')
print(f'Lambda 1 = {l1}')
print(f'Lambda 2 = {l2}')
print(f'Compton  = {dl}')