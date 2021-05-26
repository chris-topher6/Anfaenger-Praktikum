import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
import scipy.constants as const
from uncertainties import ufloat


print("Aufgabenteil a)")
t = np.genfromtxt("temps.dat", unpack=True)#In Grad
#In Kelvin umrechnen
t =  t+273.15

#Funktion für Sättigungsdampfdruck für p in mbar
def psst(T):
    return(5.5 * 10**7*np.exp(-6876/T))

#Funktion für Weglänge
def www(psaett):
    return(0.0029/psaett)

#Abstand Beschleunigerelektrode und Auffängerelektrode in cm umgerechnet
a = 1*10**-2

print("Temperaturen: ", t, "[K]")
print("Sättigungsdampfdruck: ", psst(t), "[mbar]")
print("mittlere freie Weglänge: ", www(psst(t)), "[cm]")
print("Verhältnis a/w: ", a/www(psst(t)))

#Daten für die Breite [mm] eines Volts auf dem Graphen aus den beiden Messreihen
intv1, intbr1 = np.genfromtxt("skalierung1.dat", unpack=True)
intv2, intbr2 = np.genfromtxt("skalierung2.dat", unpack=True)
#Mittelwert berechnen
meanbreite1 = np.mean(intbr1)
meanbreite2 = np.mean(intbr2)
#Fehler des Mittelwertes/Standardfehler
stdbreite1 = np.std(intbr1, ddof=1)/np.sqrt(len(intbr1))
stdbreite2 = np.std(intbr2, ddof=1)/np.sqrt(len(intbr2))

print("Die mittlere Breite für 1V aus Messreihe 1 beträgt: ", meanbreite1,"+-", stdbreite1)
print("Die mittlere Breite für 1V der Messreihe 2 beträgt: ", meanbreite2,"+-", stdbreite2)
#Daten der differentiellen Energieverteilung einlesen
diffpos11, diffsteig11, diffpos12, diffsteig12 = np.genfromtxt("diffenergie1.dat", unpack=True)
diffpos21, diffsteig21, diffpos22, diffsteig22 = np.genfromtxt("diffenergie2.dat", unpack=True)
#Umrechnung der Position in die Bremsspannung U_A
#Umrechnung in mm
diffpos11 = diffpos11*10
diffpos12 = diffpos12*10
diffpos21 = diffpos21*10
diffpos22 = diffpos22*10
#Umrechnung in V (für Messreihe 1: 1V = 23.3mm, für Messreihe 2: 1V = 23.7mm)
diffpos11 = diffpos11/23.3
diffpos12 = diffpos12/23.3
diffpos21 = diffpos21/23.7
diffpos22 = diffpos22/23.7

#Plot der ersten differentiellen Energieverteilung
plt.plot(diffpos11, diffsteig11, "g-o", label="Messreihe 24°C")
plt.plot(diffpos12, diffsteig12, "r-o", label="Messreihe 143.9°C")
plt.axvline(x=9.012, color="k", linestyle="dashed")
plt.grid()
plt.legend()
plt.xlabel(r"$U_A$ [V]")
plt.ylabel("Steigung")
plt.savefig("differentielleEnergie1.pdf")
plt.close()
#PLot der zweiten differentiellen Energieverteilung
plt.plot(diffpos21, diffsteig21, "g-o", label="Messreihe 24°C")
plt.plot(diffpos22, diffsteig22, "r-o", label="Messreihe 143.9°C")
plt.axvline(x=8.860, color="k", linestyle="dashed")
plt.grid()
plt.legend()
plt.xlabel(r"$U_A$ [V]")
plt.ylabel("Steigung")
plt.savefig("differentielleEnergie2.pdf")
plt.close()

print("Aufgabenteil b)")
#Skalierung der beiden Messreihen der Franck-Hertz Kurve
intv3, intbr31, intbr32 = np.genfromtxt("skalierung3.dat", unpack=True)
#Mittelwert der Breite bestimmen
meanbreite31 = np.mean(intbr31)
meanbreite32 = np.mean(intbr32)
#Fehler des Mittelwertes
stdbreite31 = np.std(intbr31, ddof=1)/np.sqrt(len(intbr31))
stdbreite32 = np.std(intbr32, ddof=1)/np.sqrt(len(intbr32))

print("Die mittlere Breite für 5V aus Messreihe 1 beträgt: ", meanbreite31, "+-", stdbreite31)
print("Die mittlere Breite für 5V aus Messreihe 2 beträgt: ", meanbreite32, "+-", stdbreite32)

#Mittelwert der Maxima der Franck-Hertz Kurven
max, abst1, abst2 = np.genfromtxt("abstmaxima.dat", unpack=True)
#Umrechnung von mm auf Volt (Skalierung: 5V = 20,818mm (Messreihe 1), 5V = 19,909mm (Messreihe 2))
abst1 = abst1*5/20.818
abst2 = abst2*5/19.909
#Mittelwert berechnen
meanabst1 = np.mean(abst1)
meanabst2 = np.mean(abst2)
#Fehler des Mittelwertes
stdabst1 = np.std(abst1, ddof=1)/np.sqrt(len(abst1))
stdabst2 = np.std(abst2, ddof=1)/np.sqrt(len(abst2))

print("Der mittlere Abstand zwischen zwei Maxima in Kurve 1 beträgt: ", meanabst1, "+-", stdabst1)
print("Der mittlere Abstand zwischen zwei Maxima in Kurve 2 beträgt: ", meanabst2, "+-", stdabst2)
#Definiere Energiedifferenz E_1-E_0
energiediff1 = ufloat(meanabst1, stdabst1)
energiediff2 = ufloat(meanabst2, stdabst2)
#Wandle Volt in eVolt um durch Multiplikation mit Elementarladung
energiediff1 = energiediff1*const.e
energiediff2 = energiediff2*const.e
#Teile durch Plancksches Wirkunsgquantum
energiediff1 = energiediff1/const.Planck
energiediff2 = energiediff2/const.Planck
#Berechnung der Wellenlänge
lambda1 = const.speed_of_light/energiediff1
lambda2 = const.speed_of_light/energiediff2

print("Die Wellenlänge des emittierten Photons beträgt nach der ersten Messreihe: ", lambda1, "[m]")
print("Die Wellenlänge des emittierten Photons beträgt nach der zweiten Messreihe: ", lambda2, "[m]")
