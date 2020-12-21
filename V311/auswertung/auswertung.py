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
mag = 107.8682 * 1.661*10**(-27)#Masse eines Silberatoms in kg
dichteag = 10490 #Dichte von Silber bei 20C in kg*m^-3
#Berechnung der Ladunsträger pro Atom
def ladproat(n,m,p):
    z = (n*m)/p
    return(z)

print("Ladungsträger pro Atom für konstanten Platinenstrom: ")
z1 = ladproat(n1, mag, dichteag)
print(z1)
print("Ladungsträger für konstanten Spulenstrom: ")
z2 = ladproat(n2, mag, dichteag)
print(z2)
