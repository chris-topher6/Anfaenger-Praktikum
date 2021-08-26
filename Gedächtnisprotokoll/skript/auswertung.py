import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp
import scipy.constants as const
from scipy.optimize import curve_fit

x=np.linspace(0,8)
plt.plot(x,np.e**(-x))
plt.ylabel("N")
plt.xlabel("t")
ax = plt.gca()
ax.axes.xaxis.set_ticks([])
ax.axes.yaxis.set_ticks([])
plt.savefig("pictures/Zerfallsgesetz.pdf")