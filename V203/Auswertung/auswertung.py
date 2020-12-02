import matplotlib.pyplot as plt
import numpy as np
import sympy
from uncertainties import ufloat
import scipy.constants as const

Th, ph = np.genfromtxt("MessungHoheDruecke2.txt", unpack = True)
pn, Tn = np.genfromtxt("MessungNiedrigeDruecke.txt", unpack = True)

#Umrechnung in SI
Th=Th+273.15
Tn=Tn+273.15
pn=pn*(10)**2 #Achtung beim umrechnen!!
ph=ph*(10)**5
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

plt.xlabel(r'$1/T [K^{-1}]$') #nochmal überprüfen
plt.ylabel(r'$ln(p/p_0)$')
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

plt.xlabel(r'$1/T [K^{-1}]$') #nochmal überprüfen
plt.ylabel(r'$ln(p/p_0)$')
plt.legend(loc='best')
plt.tight_layout()

plt.savefig('a.pdf')

################################################################################################################################
#b)
#Berechnung der Verdampfungswärme
Ln=-paramserr1[0]*R #Einheit: [R]=J/(K*mol) 
print(paramserr1[0])
print(f"Verdampfungswärme für p<1bar: \n L={Ln:.3f}J/mol \n\n")

################################################################################################################################
#c) 
#La=W=pV=RT
T0=373
La=R*T0
Li=Ln-La #J/mol
Li=Li/(6.02214076*10**23) #J/Molekül
Li=Li*6.242*10**18 #eV/Molekül
print(f"La={La}")
print(f"Arbeit zur Verdampfung pro Molekül: \n Li={Li:.3f}eV \n\n")

################################################################################################################################
#d)

#Das Ploynom 3. Grades
plt.figure("""second figure""")

#Parameter für Regression
params3, covariance_matrix3 = np.polyfit(Th, ph, deg=3, cov=True)

#Unsicherheit der Regression
i=0
paramserr3=np.array([h, h, h, h])
errors3 = np.sqrt(np.diag(covariance_matrix3))
print("")
for name, value, error in zip('abcd', params3, errors3):
    paramserr3[i]=ufloat(value, error)
    print(f'{name} = {value:.8f} ± {error:.8f}')
    i=i+1

#Plotten der Regression
x_plot = np.linspace(np.min(Th), np.max(Th))
plt.plot(
    x_plot,
    params3[0]*(x_plot**3)+params3[1]*(x_plot**2)+params3[2]*(x_plot)+params3[3],
    color='b', 
    label='Regression'
    )
#Plotten der Messdaten
plt.plot(Th, ph, '.', color='r', label='Messdaten')

plt.xlabel(r'$T [K]$') #nochmal überprüfen
plt.ylabel(r'$p [Pa]$')
plt.legend(loc='best')
plt.tight_layout()

plt.savefig('d1.pdf')

#Ableiten
dpdT=3*params3[0]*(Th**2)+2*params3[1]*(Th)+params3[2]

#(Vd-Vf)dp=L/T dT
#L=T(Vd-Vf) dp/dT #Vf wird vernachlässigt
#L=T(Vd) dp/dT
Vd=(R*Th)/(2*ph) + np.sqrt(((R*Th)/(2*ph))**2 - 0.9/ph)
Lh1=Th*(Vd)*dpdT

#Plots für Lh
plt.figure("""third figure""")
plt.subplot(2,1,1) #für die positive Lösung
plt.plot(Th, Lh1, 'bx', label='L1')

plt.xlabel(r'$T [K]$') 
plt.ylabel(r'$L [J/mol]$')
plt.legend(loc='best')
plt.tight_layout()

Vd=(R*Th)/(2*ph) - np.sqrt(((R*Th)/(2*ph))**2 - 0.9/ph)
Lh2=Th*(Vd)*dpdT

plt.subplot(2,1,2) #für die negative Lösung
plt.plot(Th, Lh2, 'bx', label='L2')

plt.xlabel(r'$T [K]$') 
plt.ylabel(r'$L [J/mol]$')
plt.legend(loc='best')
plt.tight_layout()

#Vergleich mit den Literaturwerten
Lnl=40657
Lnab=100*(Lnl-Ln)/Lnl #bei 100°C https://physik.cosmos-indirekt.de/Physik-Schule/Verdampfungsw%C3%A4rme
Lil=0
print(f"L & {Ln} & {Lnl} & {Lnab} \\")

plt.savefig('d2.pdf')

#Daten in txt Datein spichern:
np.savetxt("1niedrig.txt", np.column_stack([pn, Tn]), fmt = "%10.2f", delimiter = " & ", header = " pn Tn")
np.savetxt("1hoch.txt", np.column_stack([ph, Th]), fmt = "%10.2f", delimiter = " & ", header = " ph Th")
np.savetxt("d.txt", np.column_stack([Th, Lh1, Lh2]), fmt = "%10.2f", delimiter = " & ", header = " Th Lh1 Lh2")
#np.savetxt("e.txt", np.column_stack([Ln, Lnl, Lnab]), fmt = "%10.2f", delimiter = " & ", header = "Ln Lnl Lnab")