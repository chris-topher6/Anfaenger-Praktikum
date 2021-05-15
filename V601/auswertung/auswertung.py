import matplotlib.pyplot as plt
import numpy as np

t = np.genfromtxt("Temps.dat", unpack=True)#In Grad
#In Kelvin umrechnen
t =  t+273.15

#Funktion für Sättigungsdampfdruck für p in mbar
def psst(T):
    return(5.5 * 10**7*np.exp(-6876/T))

#Funktion für Weglänge
def www(psaett):
    return(0.0029/psaett)

#Abstand Beschleunigerelektrode und Affängerelektrode in m
a = 1*10**-2

print("Temperaturen: ", t, "[K]")
print("Sättigungsdampfdruck: ", psst(t), "[mbar]")
print("mittlere freie Weglänge: ", www(psst(t)), "[cm]")
print("Verhältnis a/w: ", a/www(psst(t)))
