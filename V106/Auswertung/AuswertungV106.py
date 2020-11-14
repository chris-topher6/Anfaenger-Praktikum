import numpy as np
#Aufgabe 1: Bestimmen sie die Schwingungsdauer T1 und T2 der beiden frei schwingenden Pendel
T15, T25 = np.genfromtxt("freieSchwingungsdauern.txt", unpack = True)
T1 = np.mean(T15) /5
T2 = np.mean(T25) /5
print(T1, T2)
#Aufgabe 2: Bestimmen sie die Schwingunsdauer T+ für eine gleichphasige Schwingung für mindestens zwei Pendellängen
#Aufgabe 3: Bestimmen sie die Schwingungsdauer T- für eine gegenphasige Schwingung für mindetsens zwei Pendellängen
#Pendellänge a
Tplus5 , Tminus5Versuch1 = np.genfromtxt("gleichGegenphasigeSchwingungsdauernA.txt", unpack = True)
Tminus5Versuch2 = np.genfromtxt("gegensinnigeSchwingungsdauer2.txt", unpack = True)
Tplus = np.mean(Tplus5) /5
TminusVersuch1 = np.mean(Tminus5Versuch1) /5
TminusVersuch2 = np.mean(Tminus5Versuch2) /5
print("Pendellänge 0.993m:")
print(Tplus, TminusVersuch1, TminusVersuch2)
#Pendellänge b
