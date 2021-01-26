import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat

trhodium, imprhodium = np.genfromtxt("Rhodium.dat", unpack = True)
tvanadium, impvanadium = np.genfromtxt("Vanadium.dat", unpack = True)

nulleffekt = {129, 143, 144, 136, 139, 126, 158}
deltatnulleffekt = np.ufloat(300, 10**(-5))
print(deltatnulleffekt)
