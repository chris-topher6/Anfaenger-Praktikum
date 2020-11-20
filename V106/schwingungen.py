import matplotlib.pyplot as plt
import numpy as np
import sympy

x=np.linspace(0, 4*np.pi)
#plt.figure("""first figure""")
plt.subplot(2, 1, 1)
plt.plot(x, np.sin(x), color='red', label='Pendel1')
plt.xlabel(r"$t$")
plt.ylabel(r"$x$")
plt.legend(loc="best")

plt.subplot(2, 1, 2)
plt.plot(x, np.sin(x), color='blue', label='Pendel2')
plt.xlabel(r"$t$")
plt.ylabel(r"$x$")
plt.legend(loc="best")

plt.tight_layout()
plt.savefig('gleichsinnig.pdf')

plt.figure("""first figure""")
plt.subplot(2, 1, 1)
plt.plot(x, np.sin(x), color='red', label='Pendel1')
plt.xlabel(r"$t$")
plt.ylabel(r"$x$")
plt.legend(loc="best")

plt.subplot(2, 1, 2)
plt.plot(x, -np.sin(x), color='blue', label='Pendel2')
plt.xlabel(r"$t$")
plt.ylabel(r"$x$")
plt.legend(loc="best")

plt.tight_layout()
plt.savefig('gegensinnig.pdf')

plt.figure("""second figure""")
x=np.linspace(0, 12*np.pi)
plt.subplot(2, 1, 1)
plt.plot(x, np.cos(2*np.pi*x)*np.cos(2*np.pi*x), color='red', label='Pendel1')
plt.xlabel(r"$t$")
plt.ylabel(r"$x$")
plt.legend(loc="best")

plt.subplot(2, 1, 2)
plt.plot(x, -np.sin(2*np.pi*x)*np.cos(2*np.pi*x), color='blue', label='Pendel2')
plt.xlabel(r"$t$")
plt.ylabel(r"$x$")
plt.legend(loc="best")

plt.tight_layout()
plt.savefig('gekoppelt.pdf')