import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

#Daten der Geräte
L = ufloat(16.78, 0.09) #in mH
C = ufloat(2.066, 0.006) #in nF
R1 = ufloat(67.2, 0.2) #in Ohm
R2 = ufloat(682, 1) #in Ohm
R_N = ufloat(0, 0) #in Ohm, Innenwiderstand des Netzgerätes (unbekannt)

#Daten der Geräte auf richtige Größenordnungen bringen
L = L*10**(-3) #in H
C = C*10**(-9) #in F

#Zur Überprüfung
print("Gerätedaten")
print("L = ", L, "[H]")
print("C = ", C, "[F]")
print("R1 = ", R1, "[Ohm]")
print("R2 = ", R2, "[Ohm]")

#Aufgabe 5 a)
print(" ")
print("Aufgabenteil 5 a):")
#Einhüllende der Schwingungskurve plotten
#Ausgleichsgerade der Kurve, Exponent der e-Funktion bestimmen
#effektiven Dämpfungswiderstand berechnen
#Abklingdauer berechnen
#Vergleich R_eff mit R

#Daten aus den zwei Messreihen zu Teil a)
t1, Uc1 = np.genfromtxt("datena1.txt", unpack = True)
t2, Uc2 = np.genfromtxt("datena2.txt", unpack = True)
t2h, Uc2h = np.genfromtxt("datena2einh.txt", unpack = True)

#Zeiten richtig machen
#t2 = t2*10**(-6)#in Sekunden
#t2h = t2h*10**(-6)#in Sekunden



#Plot der Einhüllenden der ersten Messreihe
plt.plot(t1, Uc1, label="Einhüllende")
plt.plot(t1, Uc1, "r.", label="Peaks")
plt.legend()
plt.xlabel(r"$t[\mu s]$")
plt.ylabel(r"$U_c [V]$")
plt.savefig("plot1.pdf")
plt.close()

#Plot der Einhüllenden der zweiten Messreihe
plt.plot(t2h, Uc2h, label="Einhüllende")
plt.plot(t2, Uc2, label = "Schwingungskurve")
plt.plot(t2, Uc2, "r.", label="Peaks")
plt.legend()
plt.xlabel(r"$t[\mu s]$")
plt.ylabel(r"$U_c [V]$")
plt.savefig("plot2.pdf")
plt.close()

#Fit mit e-Funktion an Messreihe 2
def e_fit(t, A, B):
    return(A*np.exp(-B*t))

plt.plot(t2h, Uc2h, "k.", label="Peaks")
plt.xlabel(r"$t[\mu s]$")
plt.ylabel(r"$U_c [V]$")

params, cov_matrix = curve_fit(e_fit, t2h, Uc2h, bounds = (-20, 20))#bounds helfen
errors = np.sqrt(np.diag(cov_matrix))
print('A = ', params[0], '+/-', errors[0])
print('B = ', params[1], '+/-', errors[1])

plt.plot(t2h, e_fit(t2h, *params), "r-", label="Ausgleichsrechnung")
plt.legend()
plt.savefig("plot3.pdf")
plt.close()

#mu erhält man aus dem Exponenten des Fits/2pi
mu = ufloat(params[0]/(2*np.pi), errors[0]/(2*np.pi))
print("mu = ", mu)

#effektiver Dämpfungswiderstand
R_eff = 4*np.pi*mu*L

#Vergleich R_eff und R1, R_eff weicht um rabw von R1 ab
rabw = (unp.sqrt((R1 - R_eff)**2)/R1)*100
print("R = ", R1)
print("R_eff = ", R_eff, "[Ohm]")
print("Abweichung R_eff von R1: ", rabw, "%")#Hä

#Abklingdauer
T_ex = 1/(2*np.pi*mu)

print("T_ex = ", T_ex, "[s]")

#Aufgabe 5 b)
print(" ")
print("Aufgabenteil 5 b):")
#gemessenes R_ap mit dem berechneten vergleichen

#gemessener Dämpfungswiderstand R_ap
R_ap = 3.10 #in kOhm bei 1057 Hz

#Daten auf richtige Größenordnungen bringen
R_ap = R_ap*10**3 #in Ohm

#Theoriewert berechnen
R_apTh = unp.sqrt(((4*L)**2)/(L*C))

#Vgl, prozentuale Abweichung des gemessenen Wertes von der Theorie
R_apabw = (unp.sqrt((R_apTh - R_ap)**2)/R_apTh)*100

print("nach der Theorie bestimmter R_ap = ", R_apTh, "[Ohm]")
print("gemessener R_ap = ", R_ap, "[Ohm]")
print("Abweichung R_ap von R_ap Theorie: ", R_apabw, "%" )

#Aufgabe 5 c)
print(" ")
print("Aufgabenteil 5 c):")
#Plot U_c/U gegen v (halb- oder doppellogarithmisch)
#Umgebung der Resonanzfrequenz auch linear plotten
#Breite der Resonanzkurve bestimmen
#Vergleich mit Theoriewert

#Daten aus der Messreihe
f, U, Uc = np.genfromtxt("datenc.txt", unpack=True)

#Quotientenbildung
def quotient(A, B):
    return(np.sqrt((A/B)**2))

#Plot mit halblogarithmischer Skalierung
plt.plot(f, np.log(quotient(Uc, U)), label="Halblogarithmisch")
plt.legend()
plt.xlabel(r"$\nu [kHz]$")
plt.ylabel(r"$log(\frac{U_C}{U})$")
plt.savefig("plot4.pdf")
plt.close()

#halblogarithmischer Plot der Frequenz
plt.plot(np.log(f), quotient(Uc, U), label="Diagramm der Resonanzkurve")
plt.legend()
plt.xlabel(r"$log(\nu) [kHz]$")
plt.ylabel(r"$\frac{U_C}{U}$")
plt.savefig("plot42.pdf")
plt.close()

#linearer Plot um die (vermutete) Resonanzfrequenz w_0 = 100kHz
plt.plot(f[0:5], quotient(Uc[0:5], U[0:5]), label="lineares Diagramm")
plt.legend()
plt.xlabel(r"$\nu [kHz]$")
plt.ylabel(r"$log(\frac{U_C}{U})$")
plt.savefig("plot5.pdf")
plt.close()

#Theoretische Werte für Resonanzfrequenz und Breite der Resonanzkurve
w_0 = (1/(L * C))**(0.5)
wres = unp.sqrt((1/(L*C)) - ((R2**2)/(2*L**2)))
q_rechn = 1 / (w_0 * C * (R2+R_N)) #Resonanzüberhöhung, Güte
q_rechn_neu = (w_0 * L)/(R2 + R_N) #wtf?
nu1 = (-(R2+R_N)/(2*L) + (((R2+R_N)**2/(4 * L**2)) + (1/(L * C)))**(0.5)) / (2 * np.pi)
nu2 = ( (R2+R_N)/(2*L) + ((R2+R_N)**2/(4 * L**2) + 1/(L * C))**(0.5)) / (2 * np.pi)
print("Die theoretisch berechnete Resonanzfrequenz beträgt: ", wres, "[Hz]")
print("Die theoretisch berechnete Eigenfrequenz beträgt: ", w_0, "[Hz]")
print("Die theoretisch berechnete Resonanzüberhöhung beträgt: ", q_rechn, q_rechn_neu)
print("Die theoretisch berechneten Grenzen der Resonanzbreite betragen: ")
print("v1= ", nu1, "[Hz]", "v2= ", nu2, "[Hz]")
