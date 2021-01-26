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
#fitte Zerfallsgesetz
def zerfallsgesetz(N0, llambda, t):
    N = N0 * np.exp(-llambda * t)
    return(N)
params, covariance_matrix = curve_fit(zerfallsgesetz, unp.nominal_values(tvanadium), np.log(unp.nominal_values(Nvanadium)))
uncertainties = np.sqrt(np.diag(covariance_matrix))
for name, value, uncertainty in zip('N0 llamba t', params, uncertainties):
    print(f'{name} = {value:8.3f} ± {uncertainty:.3f}')
#Plotte Nvanadium
plt.errorbar(unp.nominal_values(tvanadium), np.log(unp.nominal_values(Nvanadium)), xerr = unp.std_devs(tvanadium), yerr = np.log(unp.std_devs(Nvanadium)), fmt = "x", ecolor = "red")
plt.ylabel("N [Imp/t]")
plt.xlabel("t [s]")
plt.savefig("PlotVanadiumLinLog.pdf")
plt.clf()
