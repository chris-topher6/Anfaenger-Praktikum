 
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp
import scipy.constants as const
from scipy.stats import sem
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

U, N = np.genfromtxt('Kennlinie.dat', unpack=True)
N=N/60
################################################################################################
#a)

#Gerade für Platau
def gerade(x, m, b):
    return m*x+b
Up = np.array(U[5:33])
Np = np.array(N[5:33])
x = np.linspace(np.min(Up), np.max(Up))
params, covariance_matrix = np.polyfit(Up, Np, deg=1, cov=True)
uncertainties = np.sqrt(np.diag(covariance_matrix))

#Ausgeben der Parameter
i=0
h=ufloat(0,0)
paramserr = np.array([h, h])
errors = np.sqrt(np.diag(covariance_matrix))
for name, value, error in zip('ab', params, errors):
    paramserr[i]=ufloat(value, error)
    print(f'{name} = {value:.8f} ± {error:.8f}')
    i=i+1
#Umrechnen in % pro 100V
paramserr[0]=paramserr[0]*100
print(f'a={paramserr[0]:.8f}s%/V') ##Richtige Einheit????????

#Plot von Messdaten und Gerade
errN=np.sqrt(N)
plt.plot(x, gerade(x, *params), "k", linewidth=1, label="Regression Plateau")
plt.errorbar(U, N, xerr=0, yerr=errN, fmt = "x", markersize = 3, ecolor='red', label="Messdaten")
plt.xlabel(r"$U[V]$")
plt.ylabel(r"$N[1/60s]$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot1.pdf')

###################################################################################################
#b)
tprim=120*10**(-6) #abgelesen vom Osz
tnach=170*10**(-6)
dt=tnach-tprim #zeitlicher Abstand zwischen Primär und Nachentladungsimpuls

ttot1=160*10**(-6) #abgelesen vom Osz

N1=96041/120
N12=158479/120
N2=76518/120
N1u=ufloat(N1, np.sqrt(N1))
N12u=ufloat(N12, np.sqrt(N12))
N2u=ufloat(N2, np.sqrt(N2))

ttot2=(N1+N2-N12)/(2*N1*N2)
ttot2u=(N1u+N2u-N12u)/(2*N1u*N2u)

abw=100*(ttot2-ttot1)/ttot2
print(f'Totzeit Osz: t1={ttot1*10**(6):.3f} micro s')
print(f'Totzeit 2Q: t2={ttot2u*10**(6):.3f} micro s')
print(f'Die Abweichung von t1 bezüglich t2 ist p={abw:.3f}%')

##################################################################################################
#c)
U2, N3, I = np.genfromtxt('Zaehlrohrstrom.dat', unpack=True)
#in SI
I=I*10**(-6)
Im=np.mean(I)
N3=N3/60
#als ufloats
Iu= unp.uarray(I, 0.05*10**(-6))
Imu=ufloat(np.mean(I), sem(I))
N3u = unp.uarray(N3, np.sqrt(N3))

Qu=Imu/N3u
Qu=Qu/const.e
#print(f'die pro einfallendem Teilchen freigesetzte Ladung beträgt Q={Qu:.8f}e')
print("\nDie Q sind:")
print(Qu)

Z=I/(N3*const.e)
Zu=Iu/(N3u*const.e)
print("\nDie Z sind:")
print(Zu)

plt.figure()
plt.errorbar(I, Z, xerr=stds(Iu), yerr=stds(Zu), fmt = "x", ecolor='red', label="Messdaten")
x=np.linspace(np.min(I), np.max(I))
params,covariance_matrix=np.polyfit(I, Z, deg=1, cov=True)
plt.plot(x, gerade(x, *params), "k", label="Regression")
plt.xlabel(r"$I[A]$")
plt.ylabel(r"$Z$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot2.pdf')