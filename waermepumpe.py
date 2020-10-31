import matplotlib.pyplot as plt
import numpy as np
import sympy
from uncertainties import ufloat
import scipy.constants as const

t, T1, p1, T2, p2, N = np.genfromtxt('Waermepumpe.txt', unpack=True)

#Umrechung in SI
t=t*60
p1=(p1+1)*(10)**5
p2=(p2+1)*(10)**5
T1=T1+273.15
T2=T2+273.15
R=const.N_A *const.k
########################################################################################

#a,b) Temperaturverläufe als Diagramm

#Parameter für Regression
params1, covariance_matrix1 = np.polyfit(t, T1, deg=2, cov=True)
params2, covariance_matrix2 = np.polyfit(t, T2, deg=2, cov=True)

#Unsicherheit der Regression
errors1 = np.sqrt(np.diag(covariance_matrix1))
errors2 = np.sqrt(np.diag(covariance_matrix2))
h=ufloat(0,0)
paramserr1=np.array([h, h, h]) #ufloatarrays um die Fehler zu speichern
paramserr2=np.array([h, h, h])
i=0
j=0
print("Die Parameter der Regression für T1:")
for name, value, error in zip('abc', params1, errors1):
    paramserr1[i]=ufloat(value, error)
    print(f'{name} = {value:.8f} ± {error:.8f}')
    i=i+1
print("\n")
print("Die Parameter der Regression für T2:")
for name, value, error in zip('abc', params2, errors2):
    paramserr2[j]=ufloat(value, error)
    print(f'{name} = {value:.8f} ± {error:.8f}')
    j=j+1
print("\n")

#Plotten der Regression
x_plot = np.linspace(0, 2100)
plt.plot(
    x_plot,
    params1[0] * (x_plot)**2 + params1[1] * x_plot + params1[2],
    color='orange',
    label='Regression T1',
    linewidth=3,
)
x_plot = np.linspace(0, 2100)
plt.plot(
    x_plot,
    params2[0] * (x_plot)**2 + params2[1] * x_plot + params2[2],
    color='blue',
    label='Regression T2',
    linewidth=3,
)
#Plotten der Messwerte
plt.plot(t, T1,  '.', color='red', label='T1')
plt.plot(t, T2,  '.', color='green', label='T2')

plt.xlabel(r"$t [s]$")
plt.ylabel(r"$T [K]$")
plt.legend(loc="best")
plt.savefig('Temperaturverlaeufe.pdf')
############################################################################################

#c, d) Differentailquotient und Güteziffer

#Berechnung von dT/dt
def difT1(x):
    return(2*paramserr1[0]*x+paramserr1[1])#Die Berechnung der quadratischen Funktion erfolgte per Hand
def difT2(x):
    return(2*paramserr2[0]*x+paramserr2[1])

#Berechnung der Güteziffern
i=1
j=0
a1=4*4183
a2=750
vreal1a=np.array([h,h,h,h])
vreal2a=np.array([h,h,h,h])
vid1a=np.array([0,0,0,0])
vid2a=np.array([0,0,0,0])
print("Berechnet mit T1 \n\n")
while(i<40): #4 unterschiedliche Zeiten mit 10s Abstand
    vid=T1[i]/(T1[i]-T2[i]) #ideale Güte
    vreal1=((a1+a2)*difT1(i)/N[i]) #Reale Güte
    p=(vid-vreal1)/vid #Berechnet die Abweichung zwischen vreal und vid in %
    print(f"die reale  Güte nach t={t[i]}s: v_re={vreal1:.3f}")
    print(f"die ideale Güte nach t={t[i]}s: v_id={vid:.3f}")
    print(f"die Abweichung beträgt {p*100:.2f}% vom Idealwert")
    print("\n")
    vreal1a[j]=vreal1
    vid1a[j]=vid
    i=i+10
    j=j+1
i=1
j=0
print("Berechnet mit T2 \n\n") #!!!!!!!!!!nochmal überprüfen!!!!!!!!!
while(i<40): #4 unterschiedliche Zeiten mit 10s Abstand
    vid=-T2[i]/(T2[i]-T1[i]) #ideale Güte
    vreal2=-((a1+a2)*difT2(i)/N[i]) #Reale Güte
    p=(vid-vreal2)/vid #Berechnet die Abweichung zwischen vreal und vid in %
    print(f"die reale  Güte nach t={t[i]}s: v_re={vreal2:.3f}")
    print(f"die ideale Güte nach t={t[i]}s: v_id= {vid:.3f}")
    print(f"die Abweichung beträgt {p*100:.2f}% vom Idealwert")
    print("\n")
    vreal2a[j]=vreal2
    vid2a[j]=vid
    i=i+10
    j=j+1
############################################################################################################

#e) Massendurchsatz, Verdampfungswärme, Dampfdruckkurve
# aus V203-"Verdampfungswärme" ist begkannt:
# ln(p/p0)=_-L/(R*T)+c
# aus V203-"Verdampfungswärme" ist begkannt:
# ln(p)= -L/(R*T)+c
# aus V203-"Verdampfungswärme" ist bekannt:
# ln(p)=_-L/(R*T)+c
# p=p0*exp(-L/(R*T))
# dabei ist R=ideale-Gaskonst., p=gemessener Druck, p0=Umgebungs-Druck, T=Temperatur, L=Verdampfungswärme, c=const.
# daher wählen wir
# x = 1/T
# y = ln(p/p0)
# Dann erhalten wir die Gerade: y=-(L/R)*x+c
# => L=-m*R mit m=Steigung der Regressionsgeraden

plt.figure("""first figure""")
p0=100300

plt.subplot(2,1,1) #Plot für die Messdaten 1

#Parameter für Regression
params3, covariance_matrix3 = np.polyfit(1/T1, np.log(p1/p0), deg=1, cov=True)

#Unsicherheit der Regression
i=0
paramserr3=np.array([h, h])
errors3 = np.sqrt(np.diag(covariance_matrix3))
print("Die Parameter der Regression für p1:")
for name, value, error in zip('ab', params3, errors3):
    paramserr3[i]=ufloat(value, error)
    print(f'{name} = {value:.8f} ± {error:.8f}')
    i=i+1

#Plotten der Regression
x_plot = np.linspace(np.min(1/T1), np.max(1/T1))
plt.plot(
    x_plot,
    params3[0]*x_plot+params3[1],
    color='b', 
    label='Regression'
    )
#Plotten der Messdaten
plt.plot(1/T1, np.log(p1/p0), '.', color='r', label='Messdaten 1')

plt.xlabel(r'$1/T_1 [K^{-1}]$') #nochmal überprüfen
plt.ylabel(r'$ln(p_1/p_0)$')
plt.legend(loc='best')



plt.subplot(2,1,2) #Plot für die Messdaten 2

#Parameter für Regression
params4, covariance_matrix4 = np.polyfit(1/T2, np.log(p2/p0), deg=1, cov=True)

#Unsicherheit für Regression
i=0
paramserr4=np.array([h, h])
errors4 = np.sqrt(np.diag(covariance_matrix4))
print("Die Parameter der Regression für p2:")
for name, value, error in zip('ab4', params4, errors4):
    paramserr4[i]=ufloat(value, error)
    print(f'{name} = {value:.8f} ± {error:.8f}')
    i=i+1

#Plotten der Regression
x_plot = np.linspace(np.min(1/T2), np.max(1/T2))
plt.plot(
    x_plot,
    params4[0]*x_plot+params4[1],
    color='b',
    label='Regression'
    )

#Plotten der Messdaten
plt.plot(1/T2, np.log(p2/p0), '.', color='r', label='Messdaten 2')

plt.xlabel(r'$1/T_2 [K^{-1}]$') #nochmal überprüfen
plt.ylabel(r'$ln(p_2/p_0)$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('Druckverlaeufe.pdf')

#Berechnung der Verdampfungswärme
L=-paramserr4[0]*R #Einheit: [R]=J/(K*mol) #Hier am besten mit R berechnen
print(f"Aus Messreihe 2 folgt: \n L={L:.3f}\n\n")

#Brechnung des Massendurchsatzes
# dQ/dt=L*dm/dt
#=> dm/dt=(1/L)(dQ2/dt)=(N*v/L)

#Einheiten:
#[L]=J/mol, [dm/dt]=mol/s
molmass=120.91 #g/mol
i=1
j=0
dmdt=np.array([h, h, h, h])
while(i<40):
    massdu=-((a1+a2)*difT2(i))/L #difQ2 #!!!warum difT2???
    print(f"Der Massendruchsatz nach t={i}s ist: dm/dt=({massdu:.5f})mol/s=({massdu*molmass:.4f})g/s")
    dmdt[j]=massdu*molmass
    i=i+10
    j=j+1
print("\n")
#################################################################################


#f) Die mechanische Leistung des Kompressors

#Unsicherheit der Temperatur 
T2err=np.array([h, h, h, h, h, h, h, h, h, h, h, h, h, h, h, h, h, h, h, h, h, h, h, h, h, h, h, h, h, h, h, h, h, h, h])
i=0
while(i<35):
    T2err[i]=ufloat(T2[i], 0.1)
    i=i+1

#Berechnung der mechanischen Leistung
i=1
j=0
k=1.14
rho0=5.51 * 10**3 #g/m^3
T0=273.15 #K
Nmecha=[h,h,h,h]
rhoa=[h,h,h,h]

while(i<40):
    rho=(rho0*T0*p1[i])/(T2err[i]*p0) #g/m^3
    Nmech1=(1/(k-1))
    Nmech2=Nmech1*(p2[i]*(p1[i]/p2[i])**(1/k)-p1[i]) #pa
    Nmech3=Nmech2*(1/rho) #pa*m^3/g
    Nmech4=Nmech3*((a1+a2)/L)*difT1(i)*molmass #W
    #print(rho*10**(-3))#kg/m^3
    print(f"die mechanische Leistung nach t={t[i]} Sekunden: Nmech=({Nmech4:.5f})W")
    Nmecha[j]=Nmech4
    rhoa[j]=rho
    i=i+10
    j=j+1

np.savetxt('tabelle1.txt', np.column_stack([t,T1,p1,T2,p2,N]),fmt='%10.2f', delimiter='  &  ', header="t T1 p1 T2 p2 N")
np.savetxt('tabelle2a.txt', np.column_stack([paramserr1, paramserr2]), fmt='%r' ,delimiter='     ' ,header='err1 err2')
np.savetxt('tabelle2b.txt', np.column_stack([paramserr3, paramserr4]), fmt='%r' ,delimiter='     ' ,header='err1 err2')
np.savetxt('tabelle3.txt', np.column_stack([vreal1a, vreal2a, vid1a, vid2a]), fmt='%r' ,delimiter='     ' ,header='vreal1 vreal2 vid1 vid2')
np.savetxt('tabelle4.txt', np.column_stack([L]), fmt='%r' ,delimiter='  ' ,header='L')
np.savetxt('tabelle5.txt', np.column_stack([dmdt, Nmecha, rhoa]), fmt='%r' ,delimiter='     ' ,header='dm/dt, Nmech, rho')