import numpy as np
import scipy
import uncertainties as un

print("Aufgabe1")

#Aufgabe 1: Bestimmen sie die Schwingungsdauer T1 und T2 der beiden frei schwingenden Pendel
#Pendellänge a
T15a, T25a = np.genfromtxt("freieSchwingungsdauernA.txt", unpack = True)
T1a = T15a /5
T2a = T25a /5
#Standardabweichung
deltaT1a = np.std(T1a)
deltaT2a = np.std(T2a)
#Fehler und Mittelwert zusammen speichern
T1aMean = un.ufloat(np.mean(T1a), deltaT1a)
T2aMean = un.ufloat(np.mean(T2a), deltaT2a)
#Ausgabe für Übertrag in tex Dokument
print("Pendellänge 0.993m:")
print("Pendel1: ",T1aMean)
print("Pendel2: ",T2aMean)
#Pendellänge b
T15b, T25b = np.genfromtxt("freieSchwingungsdauernB.txt", unpack = True)
T1b = T15b /5
T2b = T25b /5
#Standardabweichung
deltaT1b = np.std(T1b)
deltaT2b = np.std(T2b)
#Fehler und Mittelwert zusammen speichern
T1bMean = un.ufloat(np.mean(T1b), deltaT1b)
T2bMean = un.ufloat(np.mean(T2b), deltaT2b)
#Ausgabe für Übertrag in tex Dokument
print("Pendellänge 0.325m:")
print("Pendel1: ",T1bMean)
print("Pendel2: ",T2bMean)

#Aufgabe 2: Bestimmen sie die Schwingunsdauer T+ für eine gleichsinnige Schwingung für mindestens zwei Pendellängen
#Aufgabe 3: Bestimmen sie die Schwingungsdauer T- für eine gegensinige Schwingung für mindestens zwei Pendellängen
print("Aufgabe23")
#Pendellänge a
Tplus5a , Tminus5aVersuch1 = np.genfromtxt("gleichGegensinnigeSchwingungsdauernA.txt", unpack = True)
Tminus5aVersuch2 = np.genfromtxt("gegensinnigeSchwingungsdauer2A.txt", unpack = True)
Tplusa = Tplus5a /5
TminusaVersuch1 = Tminus5aVersuch1 /5
TminusaVersuch2 = Tminus5aVersuch2 /5
#Standardabweichung
deltaTplusa = np.std(Tplusa)
deltaTminusaVersuch1 = np.std(TminusaVersuch1)
deltaTminusaVersuch2 = np.std(TminusaVersuch2)
#Fehler und Mittelwert zusammen speichern
TplusaMean = un.ufloat(np.mean(Tplusa), deltaTplusa)
TminusaV1Mean = un.ufloat(np.mean(TminusaVersuch1), deltaTminusaVersuch1)
TminusaV2Mean = un.ufloat(np.mean(TminusaVersuch2), deltaTminusaVersuch2)
#Ausgabe für Übertrag in tex Dokument
print("Pendellänge 0.993m:")
print("T+ a: ", TplusaMean)
print("T- a V1: ", TminusaV1Mean)
print("T- a V2: ", TminusaV2Mean)

#Pendellänge b
Tplus5b, Tminus5b = np.genfromtxt("gleichGegensinnigeSchwingungsdauernB.txt", unpack = True)
Tplusb = Tplus5b /5
Tminusb = Tminus5b /5
#Standardabweichung
deltaTplusb = np.std(Tplusb)
deltaTminusb = np.std(Tminusb)
#Fehler und Mittelwert zusammen speichern
TplusbMean = un.ufloat(np.mean(Tplusb), deltaTplusb)
TminusbMean = un.ufloat(np.mean(Tminusb), deltaTminusb)
#Ausgabe für Übertrag in tex Dokument
print("Pendellänge 0.325m:")
print("T+ b: ", TplusbMean)
print("T- b: ", TminusbMean)

#Aufgabe 4: Bestimmen sie mindestens 10mal die Schwingungsdauer T sowie die Schwebungsdauer Ts für eine gekoppelte Schwingung mit mindestens zwei Pendellängen
print("Aufgabe4")
#Pendellänge A
Tkopa, Tschweba = np.genfromtxt("gekoppeltesPendelA.txt", unpack = True)
Tkopa = Tkopa /5
#Ausgabe
print("Pendellänge 0.993m:")
print("T gekoppelt: ", Tkopa)
print("T Schwebung: ", Tschweba)

#Pendellänge B
Tkopb, Tschwebb = np.genfromtxt("gekoppeltesPendelB.txt", unpack = True)
Tkopb = Tkopb /5
#Ausgabe
print("Pendellänge 0.325m:")
print("T gekoppelt: ", Tkopb)
print("T Schwebung: ", Tschwebb)
#Speichere in txt für leichten Übertrag
np.savetxt("aufgabe4.txt", np.column_stack([Tkopa, Tschweba, Tkopb, Tschwebb]), fmt = "%10.4f", delimiter = " & ", newline = " \\\ ", header = " Tka Tsa Tkb Tsb ")

#Aufgabe 5: Berechnen sie aus den Schwingungsdauern den Kopplungsgrad K
print("Aufgabe5")
Kopplungsgrada = ((TplusaMean)**2 - (TminusaV1Mean)**2)/((TplusaMean)**2 + (TminusaV1Mean)**2)
KopplungsgradaVersuch2 = ((TplusaMean)**2 - (TminusaV2Mean)**2)/((TplusaMean)**2 + (TminusaV2Mean)**2)
Kopplungsgradb = ((TplusbMean)**2 - (TminusbMean)**2)/((TplusbMean)**2 + (TminusbMean)**2)
#Ausgabe
print("K a V1: ",Kopplungsgrada)
print("K a V2: ", KopplungsgradaVersuch2)
print("K b: ", Kopplungsgradb)

#Aufgabe 6: Vergleichen sie die gemessene Schwebungsdauer Ts mit der aus den Schwingungsdauern T+ und T- berechneten Schwebungsdauer Ts
print("Aufgabe6")
Schwebungsdauera = (TplusaMean * TminusaV1Mean)/(TplusaMean - TminusaV1Mean)
SchwebungsdaueraVersuch2 = (TplusaMean * TminusaV2Mean)/(TplusaMean - TminusaV2Mean)
Schwebungsdauerb = (TplusbMean * TminusbMean)/(TplusbMean - TminusbMean)
#Standardfehler der Messung der Schwebungsdauer berechnen
deltaTschweba = np.std(Tschweba)
deltaTschwebb = np.std(Tschwebb)
#Fehler und Mittelwert zusammen speichern
Schwebungsdaueragemessen = un.ufloat(np.mean(Tschweba), deltaTschweba)
Schwebungsdauerbgemessen = un.ufloat(np.mean(Tschwebb), deltaTschwebb)
#Ausgabe
print("Ts a V1: ", Schwebungsdauera)
print("Ts a V2: ", SchwebungsdaueraVersuch2)
print("Ts b: ", Schwebungsdauerb)
print("Ts a gemessen: ", Schwebungsdaueragemessen)
print("Ts b gemessen: ", Schwebungsdauerbgemessen)
print("Wert von Ts a V1: ", Schwebungsdauera.n)
print("Unsicherheit von Ts a V1: ", Schwebungsdauera.s)
#Bestimmung der Schwingungsfrequenzen aus den Messwerten für T
print("w ")
wplusgemessen = 2 * np.pi / TplusaMean
wminusgemessen = 2 * np.pi / TminusaV2Mean
wschwebgemessen = 2 * np.pi / Schwebungsdaueragemessen
#Ausgabe
print("w+ gemessen: ", wplusgemessen)
print("w- gemessen: ", wminusgemessen)
print("ws gemessen: ", wschwebgemessen)
