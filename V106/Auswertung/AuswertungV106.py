import numpy as np
print("Aufgabe1---------------------------------------------------------------------------------------------------------------------")
#Aufgabe 1: Bestimmen sie die Schwingungsdauer T1 und T2 der beiden frei schwingenden Pendel
#Pendellänge a
T15a, T25a = np.genfromtxt("freieSchwingungsdauernA.txt", unpack = True)
T1a = np.mean(T15a) /5
T2a = np.mean(T25a) /5
print("Pendellänge 0.993m:")
print(T1a, T2a)
#Pendellänge b
T15b, T25b = np.genfromtxt("freieSchwingungsdauernB.txt", unpack = True)
T1b = np.mean(T15b) /5
T2b = np.mean(T25b) /5
print("Pendellänge 0.325m:")
print(T1b, T2b)
np.savetxt("aufgabe1.txt", np.column_stack([T1a, T2a, T1b, T2b]),fmt="%10.4f", delimiter = " & ", newline = " \\\ ", header = "T1a T2a T1b T2b")
#Aufgabe 2: Bestimmen sie die Schwingunsdauer T+ für eine gleichsinnige Schwingung für mindestens zwei Pendellängen
#Aufgabe 3: Bestimmen sie die Schwingungsdauer T- für eine gegensinige Schwingung für mindestens zwei Pendellängen
print("Aufgabe23---------------------------------------------------------------------------------------------------------------------")
#Pendellänge a
Tplus5a , Tminus5aVersuch1 = np.genfromtxt("gleichGegensinnigeSchwingungsdauernA.txt", unpack = True)
Tminus5aVersuch2 = np.genfromtxt("gegensinnigeSchwingungsdauer2A.txt", unpack = True)
Tplusa = np.mean(Tplus5a) /5
TminusaVersuch1 = np.mean(Tminus5aVersuch1) /5
TminusaVersuch2 = np.mean(Tminus5aVersuch2) /5
print("Pendellänge 0.993m:")
print(Tplusa, TminusaVersuch1, TminusaVersuch2)
#Pendellänge b
Tplus5b, Tminus5b = np.genfromtxt("gleichGegensinnigeSchwingungsdauernB.txt", unpack = True)
Tplusb = np.mean(Tplus5b) /5
Tminusb = np.mean(Tminus5b) /5
print("Pendellänge 0.325m:")
print(Tplusb, Tminusb)
np.savetxt("aufgabe23.txt", np.column_stack([Tplusa, TminusaVersuch1, TminusaVersuch2, Tplusb, Tminusb]),fmt="%10.4f", delimiter = " & ", newline = " \\\ ", header = "T+ a T- a Versuch 1 T- a Versuch 2 T+ b T- b ")
#Aufgabe 4: Bestimmen sie mindestens 10mal die Schwingungsdauer T sowie die Schwebungsdauer Ts für eine gekoppelte Schwingung mit mindestens zwei Pendellängen
print("Aufgabe4---------------------------------------------------------------------------------------------------------------------")
#Pendellänge A
Tkopa, Tschweba = np.genfromtxt("gekoppeltesPendelA.txt", unpack = True)
Tkopa = Tkopa /5
Tschweba = Tschweba /5
print("Pendellänge 0.993m:")
print(Tkopa, Tschweba)
#Pendellänge B
Tkopb, Tschwebb = np.genfromtxt("gekoppeltesPendelB.txt", unpack = True)
Tkopb = Tkopb /5
Tschwebb = Tschwebb /5
print("Pendellänge 0.325m:")
print(Tkopb, Tschwebb)
np.savetxt("aufgabe4.txt", np.column_stack([Tkopa, Tschweba, Tkopb, Tschwebb]), fmt = "%10.4f", delimiter = " & ", newline = " \\\ ", header = " Tka Tsa Tkb Tsb ")
print("Aufgabe5---------------------------------------------------------------------------------------------------------------------")
#Aufgabe 5: Berechnen sie aus den Schwingungsdauern den Kopplungsgrad K
Kopplungsgrada = ((Tplusa)**2 - (TminusaVersuch1)**2)/((Tplusa)**2 + (TminusaVersuch1)**2)
KopplungsgradaVersuch2 = ((Tplusa)**2 - (TminusaVersuch2)**2)/((Tplusa)**2 + (TminusaVersuch2)**2)
Kopplungsgradb = ((Tplusb)**2 - (Tminusb)**2)/((Tplusb)**2 + (Tminusb)**2)
print(Kopplungsgrada, KopplungsgradaVersuch2, Kopplungsgradb)
np.savetxt("aufgabe5.txt", np.column_stack([Kopplungsgrada, KopplungsgradaVersuch2, Kopplungsgradb]), fmt = "%10.4f", delimiter = " & ", newline = " \\\ ", header = " Kopplungsgrad a Kopplungsgrad a Versuch 2 Kopplungsgrad b ")
#Aufgabe 6: Vergleichen sie die gemessene Schwebungsdauer Ts mit der aus den Schwingungsdauern T+ und T- berechneten Schwebungsdauer Ts
print("Aufgabe6---------------------------------------------------------------------------------------------------------------------")
Schwebungsdauera = (Tplusa * TminusaVersuch1)/(Tplusa - TminusaVersuch1)
SchwebungsdaueraVersuch2 = (Tplusa * TminusaVersuch2)/(Tplusa - TminusaVersuch2)
Schwebungsdauerb = (Tplusb * Tminusb)/(Tplusb - Tminusb)
print(Schwebungsdauera, SchwebungsdaueraVersuch2, Schwebungsdauerb)
np.savetxt("aufgabe6.txt", np.column_stack([Schwebungsdauera, SchwebungsdaueraVersuch2, Schwebungsdauerb]), fmt = "%10.4f", delimiter = " & ", newline = " \\\ ", header = " Schwebungsdauer a, Schwebungsdauer a Versuch2 Schwebungsdauer b ")
print("---------------------------------------------------------------------------------------------------------------------")
