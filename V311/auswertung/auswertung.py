import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const
from uncertainties import ufloat
#Einlesen der Messdaten(1,3: nicht umgepolt; 2,4: umgepolt)
stromstärke1, hallspannung1 = np.genfromtxt("Halleffekt1.txt", unpack=True)
stromstärke2, hallspannung2 = np.genfromtxt("Halleffekt2.txt", unpack=True)
stromstärke3, hallspannung3 = np.genfromtxt("Halleffekt3.txt", unpack=True)
stromstärke4, hallspannung4 = np.genfromtxt("Halleffekt4.txt", unpack=True)
#Berechnung des Mittelwertes der Hall-Spannung
uhplatineconst = np.array([hallspannung1, hallspannung2])
uhspuleconst = np.array([hallspannung3, hallspannung4])
uhmeanplatinec = ufloat(np.mean(uhplatineconst), np.std(uhplatineconst))
uhmeanspulec = ufloat(np.mean(uhspuleconst), np.std(uhspuleconst))
#Berechnung des Mittelwertes der Magnetischen Flussdichte(1,3: nicht umgepolt; 2,4: umgepolt)
stromstärkem1, magflussd1 = np.genfromtxt("Magnetfeldstärke1.txt", unpack=True)
stromstärkem2, magflussd2 = np.genfromtxt("Magnetfeldstärke2.txt", unpack=True)
magflussd = np.array([magflussd1, magflussd2])
magflussdmean = ufloat(np.mean(magflussd), np.std(magflussd))
#in SI-Einheiten
magflussdmean = magflussdmean/1000
#Konstanter Spuhlenstrom
Bc = np.array([1.1546, 1.0319])
Bc = ufloat(np.mean(Bc), np.std(Bc))
#Platinenstrom
I = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
I = ufloat(np.mean(I),np.std(I))
#Berechnung der Ladungsträger pro Volumen
def ladtrprovol(U,B,I,d):
    n = -((B*I)/(U*d*const.e))
    return(n)
#Berechnung der Ladungsträger pro Volumen für konstanten Platinenstrom
print("Ladungsträger pro Volumen bei konstantem Platinenstrom: ")
n1 = ladtrprovol(uhmeanplatinec, magflussdmean, 5, 0.000022)
print(n1)
#Berechnung der ladungsträger pro Volumen für konstanten Spulenstrom
print("Ladungsträger pro Volumen für konstanten Spulenstrom: ")
n2 = ladtrprovol(uhmeanspulec, Bc, I, 0.000022)
print(n2)
#Berechnung der Ladungsträger pro Atom
#Volumen der Probe in Kubikmeter
VAg = 8.21775715*(10**(-9))
#Dichte von Silber bei 20C° in kg/m^3
pAg = 10490
#Masse der Probe
mProbe = pAg*VAg
print("Die Probe wiegt: ")
print(mProbe)
#Atomgewicht von Silber
u = 1.661*(10**(-27))
mAg = 107.8682*u
print("Das Atomgewicht von Silber beträgt: ")
print(mAg)
#Anzahl Silberatome in der Probe
atomeProbe = mProbe/mAg
print("Die Probe enthält dann folgende Atomzahl: ")
print(atomeProbe)
z1 = n1/atomeProbe
z2 = n2/atomeProbe
print("Die Anzahl von Ladungsträgern pro Atom beträgt: ")
print(z1,z2)
#Berechnung der mittleren Flugzeit tau
#Ruhemasse in Kilogramm
m0elektron = (5.486*(10**(-4)))*u
print("Die Ruhemasse des Elektrons in kg beträgt: ")
print(m0elektron)
#Länge in Meter
laengeProbe = 25.164*10**(-3)
#Widerstand in Ohm
RProbe = 0.6
#Querschnitt der Probe in m^2
QProbe = (14.844*10**(-3))*(0.022*10**(-3))
print("Der Qerschnitt der Probe beträgt: ")
print(QProbe)
#Berechne Tau
def tau(m,L,R,n,Q):
    t = (2*m*L*R)/(n*Q*const.e*const.e)
    return(t)
t1 = tau(m0elektron,laengeProbe,RProbe,n1,QProbe)
t2 = tau(m0elektron,laengeProbe,RProbe,n2,QProbe)
print("Die mittlere Flugzeit tau beträgt: ")
print(t1,t2)
#Berechnung der mittleren Driftgeschwindigkeit vd für j=1A/mm^2
def driftgeschw(n):
    vd = -(1)/(n*const.e)
    return(vd)
vd1 = driftgeschw(n1)
vd2 = driftgeschw(n2)
print("Die mittlere Driftgeschwindigkeit beträgt: ")
print(vd1,vd2)
#Berechnung der Beweglichkeit Mü
def mu(t):
    mu = -(const.e*t)/(2*m0elektron)
    return(mu)
mu1 = mu(t1)
mu2 = mu(t2)
print("Die mittlere Beweglichkeit Mü beträgt: ")
print(mu1,mu2)
#Berechnung der Fermi-Energie um die Totalgeschwindigkeit berechnen zu können
def fermiE(n):
    E = ((const.Planck*const.Planck)/(2*m0elektron)) * (((3*n)/(8*const.pi))**2)**(1./3)
    return(E)
E1 = fermiE(n1)
E2 = fermiE(n2)
print("Die Fermieenergie beträgt: ")
print(E1,E2)
#Berechnung der Totalgeschwindigkeit v
def totv(E):
    tv = ((2*E)/m0elektron)**(1./2)
    return(tv)
tv1 = totv(E1)
tv2 = totv(E2)
print("Die Totalgeschwindigkeit beträgt: ")
print(tv1,tv2)
#Berechnung der mittleren freien Weglänge
def wegl(t,tv):
    l = t*tv
    return(l)
l1 = wegl(t1,tv1)
l2 = wegl(t2,tv2)
print("Die mittlere freie Weglänge beträgt: ")
print(l1,l2)
#Magnetische Flussdichte und Feldstrom plotten
stromstärkemagnet1, flussdichte1 = np.genfromtxt("Magnetfeldstärke1.txt", unpack=True)
stromstärkemagnet2, flussdichte2 = np.genfromtxt("Magnetfeldstärke2.txt", unpack=True)
plt.plot(stromstärkemagnet1,flussdichte1, "k.", label="Nicht Umgepolt")
plt.plot(stromstärkemagnet2,flussdichte2, "r.", label="Umgepolt")
plt.xlabel("I/A")
plt.ylabel("B/mT")
plt.legend()
plt.show()
plt.savefig("magnetplot1.pdf")
