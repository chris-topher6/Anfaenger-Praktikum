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
from tabulate import tabulate

#Daten einlesen
R3a, R4a, Rxa, R2a = np.genfromtxt("Data/a.dat", unpack=True)
R3b, R4b, R2b, C2b, Rxb, Cxb = np.genfromtxt("Data/b.dat", unpack=True)
R3c, R4c, R2c, L2c, Rxc, Lxc = np.genfromtxt("Data/c.dat", unpack=True)
R3d, R4d, R2d, Cd, Rx, Lx = np.genfromtxt("Data/d.dat", unpack=True)
Fe, Ue = np.genfromtxt("Data/e.dat", unpack=True)

#Funktionen für die Berechnungen der Widerstände/Kapazitäten/Induktivitäten
def wheatstone(R2, R3R4):
    Rx = R2*R3R4
    return(Rx)

def kapazbrücke(C2, R2, R3, R4):
    Rx = R2*R3/R4
    Cx = C2*R4/R3
    return(Rx, Cx)

def induktbrücke(L2, R2, R3, R4):
    Rx = R2*R3/R4
    Lx = L2*R3/R4
    return(Rx, Lx)

def maxwellbrücke(R2, R3, R4, C4):
    Rx = R2*R3/R4
    Lx = R2*R3*C4
    return(Rx, Lx)

#Funktion für die Abweichungsbestimmung
def abweichung(lit, mess):
    return abs(100*(lit-mess)/lit)

#Relative Fehler in ufloats speichern
#Bei a): "Das Verhältnis R3/R4 zeigt unsystematische Abweichungen bis +/- 0.5%"
R3R4a0 = ufloat(R3a[0]/R4a[0], R3a[0]/R4a[0]*0.5/100)
R3R4a1 = ufloat(R3a[1]/R4a[1], R3a[1]/R4a[1]*0.5/100)
#Bei b): "Hier muss für R2 [...]. Seine Toleranz [...] beträgt [...] nur +/- 3%."
R2b0 = ufloat(R2b[0], R2b[0]*3/100)
R2b1 = ufloat(R2b[1], R2b[1]*3/100)
#Bei d): "Toleranz von R3 und R4: +/- 3%"
R3d0 = ufloat(R3d[0], R3d[0]*3/100)
R3d1 = ufloat(R3d[1], R3d[1]*3/100)

#Aufgabenteil a)
print("Aufgabenteil a)")
print("Messung 1")
print("Der Widerstand von Wert 11 beträgt: ", wheatstone(R2a[0], R3R4a0) , " [Ohm]")
print("Damit weicht der Wert um ", abweichung(489.9, wheatstone(R2a[0], R3R4a0)),"% von 489.9 Ohm ab")
print("Messung 2")
print("Der Widerstand von Wert 11 beträgt: ", wheatstone(R2a[1], R3R4a1) , " [Ohm]")
print("Damit weicht der Wert um ", abweichung(489.9, wheatstone(R2a[1], R3R4a1)),"% von 489.9 Ohm ab")
print("--------------------------------------------------------")

#Aufgabenteil b)
print("Aufgabenteil b)")
Rxb0, Cxb0 = kapazbrücke(C2b[0], R2b0, R3b[0], R4b[0])
Rxb1, Cxb1 = kapazbrücke(C2b[1], R2b1, R3b[1], R4b[1])
print("Messung 1")
print("Der Widerstand von Wert 15 beträgt: ", Rxb0, "[Ohm]")
print("Damit weicht der Wert um ", abweichung(473, Rxb0), "% von 473 Ohm ab")
print("Die Kapazität beträgt ", Cxb0, "[nF]")
print("Damit weicht der Wert um ", abweichung(652, Cxb0), "% von 652 nF ab")
print("Messung 2")
print("Der Widerstand von Wert 15 beträgt: ", Rxb1, "[Ohm]")
print("Damit weicht der Wert um ", abweichung(473, Rxb1), "% von 473 Ohm ab")
print("Die Kapazität beträgt ", Cxb1, "[nF]")
print("Damit weicht der Wert um ", abweichung(652, Cxb1), "% von 652 nF ab")
print("--------------------------------------------------------")

#Aufgabenteil c)
print("Aufgabenteil c)")
Rxc0, Lxc0 = induktbrücke(L2c[0], R2c[0], R3c[0], R4c[0])
Rxc1, Lxc1 = induktbrücke(L2c[1], R2c[1], R3c[1], R4c[1])
print("Messung 1")
print("Der Widerstand von Wert 18 beträgt: ", Rxc0, "[Ohm]")
print("Damit weicht der Wert um ", abweichung(360, Rxc0), "% von 360 Ohm ab")
print("Die Induktivität beträgt: ", Lxc0, "[mH]")
print("Damit weicht der Wert um ", abweichung(49.82, Lxc0), "% von 49.82 mH ab")
print("Messung 2")
print("Der Widerstand von Wert 18 beträgt: ", Rxc1, "[Ohm]")
print("Damit weicht der Wert um ", abweichung(360, Rxc1), "% von 360 Ohm ab")
print("Die Induktivität beträgt: ", Lxc1, "[mH]")
print("Damit weicht der Wert um ", abweichung(49.82, Lxc1), "% von 49.82 mH ab")
print("--------------------------------------------------------")

#Aufgabenteil d)
print("Aufgabenteil d)")
Rxd0, Lxd0 = maxwellbrücke(R2d[0], R3d0, R4d[0], Cd[0])
Rxd1, Lxd1 = maxwellbrücke(R2d[1], R3d1, R4d[1], Cd[1])
#C ist in nF (nano=10^-9) angeben, daher muss die Induktivität um 10^-6 korrigiert werden um auf mH (milli = 10^-3) zu kommen
Lxd0, Lxd1 = Lxd0*10**(-6), Lxd1*10**(-6)
print("Messung 1")
print("Der Widerstand von Wert 18 beträgt: ", Rxd0, "[Ohm]")
print("Damit weicht der Wert um ", abweichung(360, Rxd0), "% von 360 Ohm ab")
print("Die Induktivität beträgt: ", Lxd0, "[mH]")
print("Damit weicht der Wert um ", abweichung(49.82, Lxd0), "% von 49.82 mH ab")
print("Messung 2")
print("Der Widerstand von Wert 18 beträgt: ", Rxd1, "[Ohm]")
print("Damit weicht der Wert um ", abweichung(360, Rxd1), "% von 360 Ohm ab")
print("Die Induktivität beträgt: ", Lxd1, "[mH]")
print("Damit weicht der Wert um ", abweichung(49.82, Lxd1), "% von 49.82 mH ab")
print("--------------------------------------------------------")

#Aufgabenteil e)
#Teile U_B durch U_S=10V
Ue = Ue/10
#Widerstand R2 in Ohm
R2e = 1000
#Kapazität C in Farad
Ce = 992*10**(-9)
#Berechne v0
v01 = 1/(R2e*Ce)
print("Die berechnete Frequenz bei der U_B verschwindet beträgt v_0 = ",v01, "Hz")

#Definiere zu fittende Funktion U_Br/U_S
def brückenspannung(omegae, a):
    UbrUs = np.sqrt((1/9) * (((omegae/a)**2 -1)**2)/((1-(omegae/a)**2)**2 +9*(omegae/a)**2))
    return(UbrUs)

#Fitte Funktion an Messwerte aus e)
v02, cov = curve_fit(brückenspannung, Fe, Ue)
print("Die aus dem Fit ermittelte Frequenz v_0 beträgt: ",v02, "Hz")
print("--------------------------------------------------------")

#Funktion und Messdaten plotten
x=np.linspace(Fe[0], Fe[20], 10000)
y=brückenspannung(x, v02)

plt.figure()
plt.plot(Fe/v02, Ue, 'r+', label='Messdaten')
plt.plot(x/v02, y, 'gray')
plt.xscale('log')
plt.xlabel(r'$v/v_0$')
plt.ylabel(r'$U_{Br}/U_{S}$')
plt.legend(loc='best')
plt.savefig('build/plotE.pdf')

#Berechnung des Klirrfaktors
klirrfaktor = Ue[5]/brückenspannung(2,1)
print("Der Klirrfaktor beträgt: ", klirrfaktor)
print("--------------------------------------------------------")


#Erzeugung der Latex-Tabellen (muss noch überarbeitet werden!!!)
#Tabelle a
#tablea = np.transpose(np.array([R3a, R4a, Rxa, R2a]))
#headersa = ["{R_3}", "{R_4}", "{R_x}", "{R_2}"]
#print("Tabelle a: ")
#print("--------------------------------------------------------")
#print(tabulate(tablea,  headers= headersa, tablefmt="latex_raw"))
#print("--------------------------------------------------------")
#Tabelle b
#tableb = np.transpose(np.array([R3b, R4b, R2b, C2b, Rxb, Cxb]))
#headersb = ["{R_3}", "{R_4}", "{R_2}", "{C_2}", "{R_x}", "{C_x}"]
#print("Tabelle b: ")
#print("--------------------------------------------------------")
#print(tabulate(tableb,  headers= headersb, tablefmt="latex_raw"))
#print("--------------------------------------------------------")
#Tabelle c
#tablec = np.transpose(np.array([R3c, R4c, R2c, L2c, Rxc, Lxc]))
#headersc = ["{R_3}", "{R_4}", "{R_2}", "{L_2}", "{R_x}", "{L_x}"]
#print("Tabelle c: ")
#print("--------------------------------------------------------")
#print(tabulate(tablec,  headers= headersc, tablefmt="latex_raw"))
#print("--------------------------------------------------------")
#Tabelle d
#tabled = np.transpose(np.array([R3d, R4d, R2d, Cd, Rx, Lx]))
#headersd = ["{R_3}", "{R_4}", "{R_2}", "{C_d}", "{R_x}", "{L_x}"]
#print("Tabelle d: ")
#print("--------------------------------------------------------")
#print(tabulate(tabled,  headers= headersd, tablefmt="latex_raw"))
#print("--------------------------------------------------------")
#Tabelle e
#tablee = np.transpose(np.array([Fe, Ue]))
#headerse = ["{f [Hz]}", "{U [V]}"]
#print("Tabelle e: ")
#print("--------------------------------------------------------")
#print(tabulate(tablee,  headers= headerse, tablefmt="latex_raw"))
#print("--------------------------------------------------------")
