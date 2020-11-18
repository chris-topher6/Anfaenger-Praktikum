import numpy as np
#Aufgabe 1: Bestimmen sie die Schwingungsdauer T1 und T2 der beiden frei schwingenden Pendel
T15, T25 = np.genfromtxt("freieSchwingungsdauernA.txt", unpack = True)
T1 = np.mean(T15) /5
T2 = np.mean(T25) /5
print(T1, T2)
np.savetxt("aufgabe1.txt", np.column_stack([T1, T2]),fmt="%10.4f", delimiter = " & ", newline = " \\\ ", header = "T1 T2")
#Aufgabe 2: Bestimmen sie die Schwingunsdauer T+ für eine gleichsinnige Schwingung für mindestens zwei Pendellängen
#Aufgabe 3: Bestimmen sie die Schwingungsdauer T- für eine gegensinige Schwingung für mindestens zwei Pendellängen
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
#Aufgabe 5: Berechnen sie aus den Schwingungsdauern den Kopplungsgrad K
Kopplungsgrada = ((Tplusa)**2 - (TminusaVersuch1)**2)/((Tplusa)**2 + (TminusaVersuch1)**2)
Kopplungsgradb = ((Tplusb)**2 - (Tminusb)**2)/((Tplusb)**2 + (Tminusb)**2)
print(Kopplungsgrada, Kopplungsgradb)
np.savetxt("aufgabe5.txt", np.column_stack([Kopplungsgrada, Kopplungsgradb]), fmt = "%10.4f", delimiter = " & ", newline = " \\\ ", header = " Kopplungsgrad a Kopplungsgrad b ")
#Aufgabe 6: Vergleichen sie die gemessene Schwebungsdauer Ts mit der aus den Schwingungsdauern T+ und T- berechneten Schwebungsdauer Ts
Schwebungsdauera = (Tplusa * TminusaVersuch1)/(Tplusa - TminusaVersuch1)
Schwebungsdauerb = (Tplusb * Tminusb)/(Tplusb - Tminusb)
print(Schwebungsdauera, Schwebungsdauerb)
np.savetxt("aufgabe6.txt", np.column_stack([Schwebungsdauera, Schwebungsdauerb]), fmt = "%10.4f", delimiter = " & ", newline = " \\\ ", header = " Schwebungsdauer a Schwebungsdauer b ")
