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

#___________________________________________________________________________________________________________________________________________
#Definiton wichtiger Größen

#Gewichte in g
m_al=163.1 #Masse der Metalle
m_fe=454.6
m_me=394.1

g_al1=800 #Masse der Gewichte
g_fe1=1250
g_me1=550 
g_me2=1550

#Längen in cm
L_al=59.3
L_fe=59.3   
L_me=60.2   
a_al=0.52   
a_fe=0.505  
R_me=0.52/2 

#Volumen in cm^3
V_al= a_al**2 * L_al          
V_fe= a_fe**2 * L_fe         
V_me= R_me**2 * np.pi * L_me 
 
#Dichte in g/cm^3
rho_al=m_al/V_al
rho_fe=m_fe/V_fe
rho_me=m_me/V_me

print(f"Dichten der Metalle")
print(f"Al: rho={rho_al:.4}")
print(f"Fe: rho={rho_fe:.4}")
print(f"Me: rho={rho_me:.4}")
print()

#Flächenträgheitsmoment cm^4
I_al=a_al**4/12
I_fe=a_fe**4/12
I_me=np.pi/4*R_me**4

print(f"Flächenträgheitsmomente")
print(f"Al: I=({I_al*10**(-8):.4})m^4")
print(f"Fe: I=({I_fe*10**(-8):.4})m^4")
print(f"Me: I=({I_me*10**(-8):.4})m^4")
print()

#__________________________________________________________________________________________________________________________________________
#Vorbereitung

#Daten importieren
x1,  D_al1  = np.genfromtxt('data/al1.dat',    unpack=True) #x in cm
x1,  D_fe1  = np.genfromtxt('data/fe1.dat',    unpack=True) #D in mm
x1,  D_me1  = np.genfromtxt('data/me1.dat',    unpack=True)
x2,  D_me2  = np.genfromtxt('data/me2.dat',    unpack=True)
x9,  D_me9  = np.genfromtxt('data/me9.dat',    unpack=True)
x10, D_me10 = np.genfromtxt('data/me10.dat',   unpack=True)

D_al1 =D_al1 /10 #D in cm
D_fe1 =D_fe1 /10
D_me1 =D_me1 /10
D_me2 =D_me2 /10
D_me9 =D_me9 /10
D_me10=D_me10/10

#Funktionen
def arg8(x, L):
    return L*x**2-x**3/3
def arg9(x, L):
    return 3*L**2*x-4*x**3
def arg10(x, L):
    return 4*x**3-12*L*x**2+9*L**2*x-L**3
def elast1(a,m,I):
    return m*9.81/(2*a*I)
def elast2(a,m,I):
    return m*9.81/(48*a*I)

#__________________________________________________________________________________________________________________________________________
#Regression
params_al8,  cov_al8  = np.polyfit(arg8(x1,  L_al), D_al1,  deg=1, cov=True) # a in cm^-2
params_fe8,  cov_fe8  = np.polyfit(arg8(x1,  L_fe), D_fe1,  deg=1, cov=True) # b in cm
params_me8,  cov_me8  = np.polyfit(arg8(x1,  L_me), D_me1,  deg=1, cov=True)
params_me9,  cov_me9  = np.polyfit(arg9(x9,  L_me), D_me9,  deg=1, cov=True)
params_me10, cov_me10 = np.polyfit(arg10(x10,L_me), D_me10, deg=1, cov=True)

err_al8  = np.sqrt(np.diag(cov_al8))
err_fe8  = np.sqrt(np.diag(cov_fe8))
err_me8  = np.sqrt(np.diag(cov_me8))
err_me9  = np.sqrt(np.diag(cov_me9))
err_me10 = np.sqrt(np.diag(cov_me10))

#Ab jetzt alles erstmal in SI
params0_al8  = ufloat(params_al8[0],  err_al8[0])  *10**(4)#in m^-2
params1_al8  = ufloat(params_al8[1],  err_al8[1])  *10**(-2) #in m
params0_fe8  = ufloat(params_fe8[0],  err_fe8[0])  *10**(4)
params1_fe8  = ufloat(params_fe8[1],  err_fe8[1])  *10**(-2)
params0_me8  = ufloat(params_me8[0],  err_me8[0])  *10**(4)
params1_me8  = ufloat(params_me8[1],  err_me8[1])  *10**(-2)
params0_me9  = ufloat(params_me9[0],  err_me9[0])  *10**(4)
params1_me9  = ufloat(params_me9[1],  err_me9[1])  *10**(-2)
params0_me10 = ufloat(params_me10[0], err_me10[0]) *10**(4)
params1_me10 = ufloat(params_me10[1], err_me10[1]) *10**(-2)

print(f"Parameter für der Regression")
print(f"Al: \n a=({params0_al8})m^-2 \n b=({params1_al8})m \n")
print(f"Fe: \n a=({params0_fe8})m^-2 \n b=({params1_fe8})m \n")
print(f"Me: \n a=({params0_me8})m^-2 \n b=({params1_me8})m")
print(f" a=({params0_me9 })m^-2  \n b={params1_me9}m")
print(f" a=({params0_me10})m^-2 \n b={params1_me10}m \n")

m_al=m_al*10**(-3) #in kg
m_fe=m_fe*10**(-3)
m_me=m_me*10**(-3)
g_al1=g_al1*10**(-3)
g_fe1=g_fe1*10**(-3)
g_me1=g_me1*10**(-3)
g_me2=g_me2*10**(-3)

I_al=I_al*10**(-8) #in m^4
I_fe=I_fe*10**(-8)
I_me=I_me*10**(-8)
#_________________________________________________________________________________________________________________________________________

print(f"Elastizitätsmodul")

#Literaturwerte in kNmm^-2
Elit_al=70
Elit_fe=196
Elit_me_min=78
Elit_me_max=123

E_al8 =elast1(params0_al8 , g_al1, I_al)*10**(-9) #kNmm^-2
E_fe8 =elast1(params0_fe8 , g_fe1, I_fe)*10**(-9) #kNmm^-2
E_me8 =elast1(params0_me8 , g_me1, I_me)*10**(-9) #kNmm^-2
E_me9 =elast2(params0_me9 , g_me2, I_me)*10**(-9) #kNmm^-2
E_me10=elast2(params0_me10, g_me2, I_me)*10**(-9) #kNmm^-2

print(f"Al: \n E=({E_al8 :.3f})kNmm^-2")
print(f"Fe: \n E=({E_fe8 :.3f})kNmm^-2")
print(f"Me: \n E=({E_me8 :.3f})kNmm^-2")
print(f" E=({E_me9 :.3f})kNmm^-2")
print(f" E=({E_me10:.3f})kNmm^-2")

print(f"\nprozentuale Abweichungen der Elastizitätsmoduln")
print(f"abw von me10 bzgl me9: p={tools.abweichung(E_me9, E_me10)}%")
print(f"abw von me9  bzgl me8: p={tools.abweichung(E_me8, E_me9) }%")
print(f"abw von me10 bzgl me8: p={tools.abweichung(E_me8, E_me10)}%")
print(f"abw von al8 bzgl Lit:  p={tools.abweichung(Elit_al, E_me10)}%")
print(f"abw von fe8 bzgl Lit:  p={tools.abweichung(Elit_fe, E_me10)}%")
print(f"abw von me8 bzgl Lit:  p={tools.abweichung(Elit_me_min, E_me8)} bis {tools.abweichung(Elit_me_max, E_me8)}%")

#___________________________________________________________________________________________________________________________________________
#Plots 

#einseitig
plt.figure() #alle Daten einfach so 
xal = np.linspace(np.min(x1), np.max(x1))
xfe = np.linspace(np.min(x1), np.max(x1))
xme = np.linspace(np.min(x1), np.max(x1))
plt.plot(x1, D_al1, 'r.',  label='Messdaten Al')
plt.plot(x1, D_fe1, 'b.',  label='Messdaten Fe')
plt.plot(x1, D_me1, 'g.',  label='Messdaten Me')
plt.xlabel(r"$x/\;\si{\centi\metre}$")
plt.ylabel(r"$D(x)/\;\si{\centi\metre}$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot1-daten1.pdf')

plt.figure() #alle
xal = np.linspace(np.min(arg8(x1, L_al)), np.max(arg8(x1, L_al)))
xfe = np.linspace(np.min(arg8(x1, L_fe)), np.max(arg8(x1, L_fe)))
xme = np.linspace(np.min(arg8(x1, L_me)), np.max(arg8(x1, L_me)))
plt.plot(xal, tools.gerade(xal,  *params_al8),    'r',   label="Regression Al")
plt.plot(arg8(x1 , L_al), D_al1, 'r.',  label='Messdaten Al')
plt.plot(xfe, tools.gerade(xfe,  *params_fe8),    'b',   label="Regression Fe")
plt.plot(arg8(x1 , L_fe), D_fe1, 'b.',  label='Messdaten Fe')
plt.plot(xme, tools.gerade(xme,  *params_me8),    'g',   label="Regression Me")
plt.plot(arg8(x1 , L_me), D_me1, 'g.',  label='Messdaten Me')
plt.xlabel(r"$\xi/\;\si{\cubic\centi\metre}$")
plt.ylabel(r"$D(\xi)/\;\si{\centi\metre}$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot2-alle1.pdf')

plt.figure() #Al
x =np.linspace(np.min(arg8(x1, L_al)), np.max(arg8(x1, L_al)))
plt.plot(x, tools.gerade(x,  *params_al8),    'darkred',   label="Regression")
plt.plot(arg8(x1 , L_al), D_al1, 'r.',  label='Messdaten')
plt.xlabel(r"$\xi/\;\si{\cubic\centi\metre}$")
plt.ylabel(r"$D(\xi)/\;\si{\centi\metre}$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot3-al1.pdf')

plt.figure() #Fe
x =np.linspace(np.min(arg8(x1, L_fe)), np.max(arg8(x1, L_fe)))
plt.plot(x, tools.gerade(x,  *params_fe8),    'darkblue',   label="Regression")
plt.plot(arg8(x1 , L_fe), D_fe1, 'b.',  label='Messdaten')
plt.xlabel(r"$\xi/\;\si{\cubic\centi\metre}$")
plt.ylabel(r"$D(\xi)/\;\si{\centi\metre}$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot4-fe1.pdf')

plt.figure() #Me
x =np.linspace(np.min(arg8(x1, L_me)), np.max(arg8(x1, L_me)))
plt.plot(x, tools.gerade(x,  *params_me8),    'darkgreen',   label="Regression")
plt.plot(arg8(x1 , L_me), D_me1, 'g.',  label='Messdaten')
plt.xlabel(r"$\xi/\;\si{\cubic\centi\metre}$")
plt.ylabel(r"$D(\xi)/\;\si{\centi\metre}$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot5-me1.pdf')

#beidseitig
plt.figure() #Me 9
x =np.linspace(np.min(arg9(x9, L_me)), np.max(arg9(x9, L_me)))
plt.plot(x, tools.gerade(x,  *params_me9),    'forestgreen',   label="Regression")
plt.plot(arg9(x9 , L_me), D_me9, 'g.',  label='Messdaten')
plt.xlabel(r"$\eta/\;\si{\cubic\centi\metre}$")
plt.ylabel(r"$D(\eta)/\;\si{\centi\metre}$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot6-me9.pdf')

plt.figure() #Me 10 
x =np.linspace(np.min(arg10(x10, L_me)), np.max(arg10(x10, L_me)))
plt.plot(x, tools.gerade(x,  *params_me10),    'limegreen',   label="Regression")
plt.plot(arg10(x10 , L_me), D_me10, 'g.',  label='Messdaten')
plt.xlabel(r"$\eta/\;\si{\cubic\centi\metre}$")
plt.ylabel(r"$D(\eta)/\;\si{\centi\metre}$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot7-me10.pdf')
