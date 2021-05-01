import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat

#Daten der Geräte
L = ufloat(16.78, 0.09) #in mH
C = ufloat(2.066, 0.006) #in nF
R1 = ufloat(67.2, 0.2) #in Ohm
R2 = ufloat(682, 1) #in Ohm

#Aufgabe 5 a)
#Einhüllende der Schwingungskurve plotten
#Ausgleichsgerade der Kurve, Exponent der e-Funktion bestimmen
#effektiven Dämpfungswiderstand berechnen
#Abklingdauer berechnen
#Vergleich R_eff mit R

#Daten aus den zwei Messreihen zu Teil a)
t1, Uc1 = np.genfromtxt("datena1.txt", unpack = True)
t2, Uc2 = np.genfromtxt("datena2.txt", unpack = True)

#Plot des Spannungsverlaufs

#Plot der Einhüllenden der ersten Messreihe
plt.plot(t1, Uc1, label="Einhüllende")
plt.plot(t1, Uc1, "r.", label="Peaks")
plt.legend()
plt.xlabel(r"$t[\mu s]$")
plt.ylabel(r"$U_c [V]$")
plt.savefig("plot1.pdf")
plt.close()

#Plot der Einhüllenden der zweiten Messreihe
plt.plot(t2, Uc2, label="Einhüllende")
plt.plot(t2, Uc2, "r.", label="Peaks")
plt.legend()
plt.xlabel(r"$t[\mu s]$")
plt.ylabel(r"$U_c [V]$")
plt.savefig("plot2.pdf")
plt.close()
