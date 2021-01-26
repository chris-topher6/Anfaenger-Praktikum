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
Nrhodium = imprhodium - np.mean(nulleffekt)

#fitte log(zerfallsgesetz)
params1, covariance_matrix1 = np.polyfit(unp.nominal_values(tvanadium), np.log(unp.nominal_values(Nvanadium)), deg = 1, cov = True)
#linspace über komplette Zeitskala
x_plot1 = np.linspace(0,1320)

#Plotte Nvanadium
plt.errorbar(unp.nominal_values(tvanadium), np.log(unp.nominal_values(Nvanadium)), xerr = unp.std_devs(tvanadium), yerr = np.log(unp.std_devs(Nvanadium)), fmt = "x", ecolor = "black", label="Messung")
plt.plot(x_plot1, params1[0]*x_plot1+params1[1], label="Regression" )
plt.ylabel("ln(N)")
plt.xlabel("t [s]")
plt.legend()
plt.savefig("PlotVanadiumLinLog1.pdf")
plt.clf()
#Angabe der Zerfallszeit(reziproke Zerfallskonstante) nach erster Regression
zerfallszeit1 = 1/(params1[0] * (-1))
print("Die Zerfallszeit beträgt: ", zerfallszeit1)
#Bestimmung der Halbwertszeit
halbwertszeit = np.log(2/(params1[0] * (-1)))
print("Die Halbwertszeit beträgt: ", halbwertszeit)
#Literaturangabe Wikipedia: 52 Vanadium 3.743min, ungefähr 220s
#Plotte Nvanadium, beachte nur Werte bis 440s (zwischen Messpunkt t=420s und t= 450s)
x_plot2 = np.linspace(0, 420)
#tvanadium und Nvanadium verringern auf oben genannte Messwerte
tvanadium2 = tvanadium[:14]
Nvanadium2 = Nvanadium[:14]
#params2, covariance_matrix2 = np.polyfit()
#params2, covariance_matrix2 = np.polyfit(unp.nominal_values)
