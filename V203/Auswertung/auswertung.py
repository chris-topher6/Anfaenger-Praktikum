import matplotlib.pyplot as plt
import numpy as np
import sympy
from uncertainties import ufloat
import scipy.constants as const

Th, ph = np.genfromtxt("MessungHoheDruecke2.txt", unpack = True)
Tn, pn = np.genfromtxt("MessungNiedrigeDruecke.txt", unpack = True)

#Umrechnung in SI
Th=Th+273.15
Tn=Tn+273.15
ph=ph*(10)**2
pn=pn*(10)**5
R=const.N_A *const.k

####################################################################################################################################
#a) 
#Plot der Dampfdruckkurve (mit log skala)

#1) p<1bar
plt.figure("""first figure""")
p0=100300
h=ufloat(0,0)

plt.subplot(2,1,1) #Plot für die Messdaten

#Parameter für Regression
params1, covariance_matrix1 = np.polyfit(1/Tn, np.log(pn/p0), deg=1, cov=True)

#Unsicherheit der Regression
i=0
paramserr1=np.array([h, h])
errors1 = np.sqrt(np.diag(covariance_matrix1))
print("")
for name, value, error in zip('ab', params1, errors1):
    paramserr1[i]=ufloat(value, error)
    print(f'{name} = {value:.8f} ± {error:.8f}')
    i=i+1

#Plotten der Regression
x_plot = np.linspace(np.min(1/Tn), np.max(1/Tn))
plt.plot(
    x_plot,
    params1[0]*x_plot+params1[1],
    color='b', 
    label='Regression'
    )
#Plotten der Messdaten
plt.plot(1/Tn, np.log(pn/p0), '.', color='r', label='Messdaten')

plt.xlabel(r'$1/T_1 [K^{-1}]$') #nochmal überprüfen
plt.ylabel(r'$ln(p_1/p_0)$')
plt.legend(loc='best')

#2) p>1bar
plt.subplot(2,1,2) #Plot für die Messdaten

#Parameter für Regression
params2, covariance_matrix2 = np.polyfit(1/Th, np.log(ph/p0), deg=1, cov=True)

#Unsicherheit der Regression
i=0
paramserr2=np.array([h, h])
errors1 = np.sqrt(np.diag(covariance_matrix2))
print("")
for name, value, error in zip('ab', params2, errors1):
    paramserr2[i]=ufloat(value, error)
    print(f'{name} = {value:.8f} ± {error:.8f}')
    i=i+1

#Plotten der Regression
x_plot = np.linspace(np.min(1/Th), np.max(1/Th))
plt.plot(
    x_plot,
    params2[0]*x_plot+params2[1],
    color='b', 
    label='Regression'
    )
#Plotten der Messdaten
plt.plot(1/Th, np.log(ph/p0), '.', color='r', label='Messdaten')

plt.xlabel(r'$1/T_1 [K^{-1}]$') #nochmal überprüfen
plt.ylabel(r'$ln(p_1/p_0)$')
plt.legend(loc='best')
plt.tight_layout()

plt.savefig('a.pdf')

################################################################################################################################
#b)
#Berechnung der Verdampfungswärme
L=-paramserr1[0]*R #Einheit: [R]=J/(K*mol) 
print(paramserr1[0])
print(f"Verdampfungswärme für p<1bar: \n L={L:.3f}J/mol \n\n")

################################################################################################################################
#c) 
#La=W=pV=RT
T0=373
La=R*T0
Li=L-La #J/mol
Li=Li/(6.02214076*10**23) #J/Molekül
Li=Li*6.242*10**18 #eV/Molekül
print(f"Arbeit zur Verdampfung pro Molekül: \n Li={Li:.3f}eV \n\n")

################################################################################################################################
#d)
#(Vd-Vf)dp=L/T dT
#L=T(Vd-Vf) dp/dT