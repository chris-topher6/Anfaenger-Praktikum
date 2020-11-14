import numpy as np
#Aufgabe 1: Bestimmen sie die Schwingungsdauer T1 und T2 der beiden frei schwingenden Pendel
T15, T25 = np.genfromtxt("freieSchwingungsdauernA.txt", unpack = True)
T1 = np.mean(T15) /5
T2 = np.mean(T25) /5
print(T1, T2)
#Aufgabe 2: Bestimmen sie die Schwingunsdauer T+ für eine gleichphasige Schwingung für mindestens zwei Pendellängen
#Aufgabe 3: Bestimmen sie die Schwingungsdauer T- für eine gegenphasige Schwingung für mindetsens zwei Pendellängen
#Pendellänge a
Tplus5 , Tminus5Versuch1 = np.genfromtxt("gleichGegensinnigeSchwingungsdauernA.txt", unpack = True)
Tminus5Versuch2 = np.genfromtxt("gegensinnigeSchwingungsdauer2A.txt", unpack = True)
Tplus = np.mean(Tplus5) /5
TminusVersuch1 = np.mean(Tminus5Versuch1) /5
TminusVersuch2 = np.mean(Tminus5Versuch2) /5
print("Pendellänge 0.993m:")
print(Tplus, TminusVersuch1, TminusVersuch2)
#Pendellänge b
Tplus5b, Tminus5b = np.genfromtxt("gleichGegensinnigeSchwingungsdauernB.txt", unpack = True)
Tplusb = np.mean(Tplus5b) /5
Tminusb = np.mean(Tminus5b) /5
print("Pendellänge 0.325m:")
print(Tplusb, Tminusb)
#Aufgabe 4: Bestimmen sie mindestens 10mal die Schwingungsdauer T sowie die Schwebungsdauer Ts für eine gekoppelte Schwingung mit mindestens zwei Pendellängen
Tkopa, Tschweba = np.mean("gekoppeltesPendelA.txt", unpack = True)
#Aufgabe 5: Berechnen sie aus den Schwingungsdauern den Kopplungsgrad K

#Aufgabe 6: Vergleichen sie die gemessene Schwebungsdauer Ts mit der aus den Schwingungsdauern T+ und T- berechneten Schwebungsdauer Ts
