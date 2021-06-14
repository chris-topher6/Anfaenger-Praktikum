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

#Erzeugung der Latex-Tabellen
#Tabelle a
tablea = np.transpose(np.array([R3a, R4a, Rxa, R2a]))
headersa = ["{R_3}", "{R_4}", "{R_x}", "{R_2}"]
print("Tabelle a: ")
print("--------------------------------------------------------")
print(tabulate(tablea,  headers= headersa, tablefmt="latex_raw"))
print("--------------------------------------------------------")
#Tabelle b
tableb = np.transpose(np.array([R3b, R4b, R2b, C2b, Rxb, Cxb]))
headersb = ["{R_3}", "{R_4}", "{R_2}", "{C_2}", "{R_x}", "{C_x}"]
print("Tabelle b: ")
print("--------------------------------------------------------")
print(tabulate(tableb,  headers= headersb, tablefmt="latex_raw"))
print("--------------------------------------------------------")
#Tabelle c
tablec = np.transpose(np.array([R3c, R4c, R2c, L2c, Rxc, Lxc]))
headersc = ["{R_3}", "{R_4}", "{R_2}", "{L_2}", "{R_x}", "{L_x}"]
print("Tabelle c: ")
print("--------------------------------------------------------")
print(tabulate(tablec,  headers= headersc, tablefmt="latex_raw"))
print("--------------------------------------------------------")
#Tabelle d
tabled = np.transpose(np.array([R3d, R4d, R2d, Cd, Rx, Lx]))
headersd = ["{R_3}", "{R_4}", "{R_2}", "{C_d}", "{R_x}", "{L_x}"]
print("Tabelle d: ")
print("--------------------------------------------------------")
print(tabulate(tabled,  headers= headersd, tablefmt="latex_raw"))
print("--------------------------------------------------------")
#Tabelle e
tablee = np.transpose(np.array([Fe, Ue]))
headerse = ["{f [Hz]}", "{U [V]}"]
print("Tabelle e: ")
print("--------------------------------------------------------")
print(tabulate(tablee,  headers= headerse, tablefmt="latex_raw"))
print("--------------------------------------------------------")

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
print("Damit weicht der Wert um ", abweichung(489.9, wheatstone(R2a[0], R3R4a0)),"% ab")
print("Messung 2")
print("Der Widerstand von Wert 11 beträgt: ", wheatstone(R2a[1], R3R4a1) , " [Ohm]")
print("Damit weicht der Wert um ", abweichung(489.9, wheatstone(R2a[1], R3R4a1)),"% ab")
print("--------------------------------------------------------")

#Aufgabenteil b)
print("Aufgabenteil b)")
Rxb0, Cxb0 = kapazbrücke(C2b[0], R2b[0], R3b[0], R4b[0])
Rxb1, Cxb1 = kapazbrücke(C2b[1], R2b[1], R3b[1], R4b[1])
print("Messung 1")
print("Der Widerstand von Wert 15 beträgt: ", Rxb0, "[Ohm]")
print("Damit weicht der Wert um ", abweichung(473, Rxb0), "% ab")
print("Die Kapazität beträgt ", Cxb0, "[nF]")
print("Damit weicht der Wert um ", abweichung(652, Cxb0), "% ab")
print("Messung 2")
print("Der Widerstand von Wert 15 beträgt: ", Rxb0, "[Ohm]")
print("Damit weicht der Wert um ", abweichung(473, Rxb0), "% ab")
print("Die Kapazität beträgt ", Cxb0, "[nF]")
print("Damit weicht der Wert um ", abweichung(652, Cxb0), "% ab")
print("--------------------------------------------------------")
