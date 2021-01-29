import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp
import scipy.constants as const
from scipy.optimize import curve_fit

#Rhodiummessung
trhodium, imprhodium = np.genfromtxt("Rhodium.dat", unpack = True)
#Fehler der Messung
imprhodium = unp.uarray(imprhodium, np.sqrt(imprhodium))
trhodium = unp.uarray(trhodium, 10**(-5))
#Vanadiummessung
tvanadium, impvanadium = np.genfromtxt("Vanadium.dat", unpack = True)
#Fehler der Messung
impvanadium = unp.uarray(impvanadium, np.sqrt(impvanadium))
tvanadium = unp.uarray(tvanadium, 10**(-5))
#Messung des Nulleffektes
nulleffekt = [129, 143, 144, 136, 139, 126, 158]
deltatnulleffekt = ufloat(300, 10**(-5))
#Fehler der Messung
nulleffekt = unp.uarray(nulleffekt, np.sqrt(nulleffekt))
#Nulleffekt auf 30s Messintervalle bringen
deltatnulleffekt = deltatnulleffekt/10
nulleffekt = nulleffekt/10

#Berücksichtige Nulleffekt
Nvanadium = impvanadium - np.mean(nulleffekt)

#fitte log(zerfallsgesetz)
params1, covariance_matrix1 = np.polyfit(unp.nominal_values(tvanadium), np.log(unp.nominal_values(Nvanadium)), deg = 1, cov = True)
#linspace über komplette Zeitskala
x_plot1 = np.linspace(0,1320)

#Plotte Nvanadium
plt.errorbar(unp.nominal_values(tvanadium), np.log(unp.nominal_values(Nvanadium)), xerr = unp.std_devs(tvanadium), yerr = np.log(unp.std_devs(Nvanadium)), fmt = "x", ecolor = "black", label="Messung Vanadium")
plt.plot(x_plot1, params1[0]*x_plot1+params1[1], label="Regression" )
plt.ylabel("ln(N)")
plt.xlabel("t [s]")
plt.legend()
plt.savefig("PlotVanadiumLinLog1.pdf")
plt.clf()
#Angabe der Zerfallszeit(reziproke Zerfallskonstante) nach erster Regression
print("Die Zerfallskonstante Lambda der ersten Regression von Vanadium beträgt: ", params1[0])
zerfallszeit1 = 1/(params1[0] * (-1))
print("Die Zerfallszeit der ersten Regression von Vanadium beträgt: ", zerfallszeit1)
#Bestimmung der Halbwertszeit
halbwertszeit1 = np.log(2)/(params1[0] * (-1))
print("Die Halbwertszeit der ersten Regression von Vanadium beträgt: ", halbwertszeit1)
#Literaturangabe Wikipedia: 52 Vanadium 3.743min, ungefähr 220s
#Plotte Nvanadium, beachte nur Werte bis 460s (nächster Messpunkt bei t=450s)
x_plot2 = np.linspace(0, 450)
#tvanadium und Nvanadium verringern auf oben genannte Messwerte
tvanadium2 = tvanadium[:15]
Nvanadium2 = Nvanadium[:15]
#log(zerfallsgesetz) auf alles unter der doppelten Halbwertszeit fitten
params2, covariance_matrix2 = np.polyfit(unp.nominal_values(tvanadium2), np.log(unp.nominal_values(Nvanadium2)), deg = 1, cov = True)
#Plotten
plt.errorbar(unp.nominal_values(tvanadium2), np.log(unp.nominal_values(Nvanadium2)), xerr = unp.std_devs(tvanadium2), yerr = np.log(unp.std_devs(Nvanadium2)), fmt = "x", ecolor = "black", label="Messung Vanadium")
plt.plot(x_plot2, params2[0]*x_plot2+params2[1], label="Regression")
plt.ylabel("ln(N)")
plt.xlabel("t [s]")
plt.legend()
plt.savefig("PlotVanadiumLinLog2.pdf")
plt.clf()
print("Die Zerfallskonstante Lambda der zweiten Regression von Vanadium beträgt: ", params2[0])
zerfallszeit2 = 1/(params2[0]*(-1))
print("Die Zerfallszeit der zweiten Regression von Vanadium beträgt: ",zerfallszeit2)
halbwertszeit2 = np.log(2)/(params2[0]*(-1))
print("Die Halbwertszeit der zweiten Regression von Vanadium beträgt: ", halbwertszeit2)
#Nulleffekt von 30s auf 15s Messintervalle bringen
deltatnulleffekt = deltatnulleffekt/2
nulleffekt = nulleffekt/2
#Nulleffekt berücksichtigen
Nrhodium = imprhodium - np.mean(nulleffekt)
#plotte Rhodium
plt.errorbar(unp.nominal_values(trhodium), np.log(unp.nominal_values(Nrhodium)), xerr = unp.std_devs(trhodium), yerr = np.log(unp.std_devs(Nrhodium)), fmt = "x", ecolor = "black", label = "Messung Rhodium")
#Fitte Funktion an den Langlebigen Teil des Zerfalls
trhodiumlanglebig = trhodium[15:44]
Nrhodiumlanglebig = Nrhodium[15:44]
params3, covariance_matrix3 = np.polyfit(unp.nominal_values(trhodiumlanglebig), np.log(unp.nominal_values(Nrhodiumlanglebig)), deg = 1, cov = True)
x_plot3 = np.linspace(220, 660)
plt.plot(x_plot3, params3[0]*x_plot3+params3[1], label = "Langlebige Regression")
plt.ylabel("log(N)")
plt.xlabel("t [s]")
plt.legend()
plt.savefig("PlotRhodiumLinLog1.pdf")
plt.clf()
#Bestimme Werte
print("Die Zerfallskonstante Lambda der langlebigen Regression von Rhodium beträgt: ", params3[0])
zerfallszeit3 = 1/(params3[0]*(-1))
print("Die Zerfallszeit des langlebigen Zerfalls von Rhodium beträgt: ", zerfallszeit3)
halbwertszeit3 = np.log(2)/(params3[0]*(-1))
print("Die Halbwertszeit des langlebigen Zerfalls von Rhodium beträgt: ", halbwertszeit3)
#Plotte Extrapolierte Regression des Langlebigen Rhodium-Zerfalls
plt.errorbar(unp.nominal_values(trhodium), np.log(unp.nominal_values(Nrhodium)), xerr = unp.std_devs(trhodium), yerr = np.log(unp.std_devs(Nrhodium)), fmt = "x", ecolor = "black", label = "Messung Rhodium")
x_plot4 = np.linspace(0, 660)
plt.plot(x_plot4, params3[0]*x_plot4+params3[1], label = "Extrapolierte langlebige Regression ")
plt.ylabel("log(N)")
plt.xlabel("t [s]")
plt.legend()
plt.savefig("PlotRhodiumLinLogExtr1.pdf")
plt.clf()
#Langlebigen Zerfall vom Kurzlebigen trennen
NominalNrhodiumkurzlebig = np.zeros(43)
DevNrhodiumkurzlebig = np.zeros(43)
for i in range(0,43):
    NominalNrhodiumkurzlebig[i] = unp.nominal_values(Nrhodium[i]) - params3[0]*unp.nominal_values(trhodium[i])+params3[1]
    DevNrhodiumkurzlebig[i] = unp.std_devs(Nrhodium[i]) - params3[0]*unp.std_devs(trhodium[i])+params3[1]

Nrhodiumkurzlebig = unp.uarray(NominalNrhodiumkurzlebig, DevNrhodiumkurzlebig)
