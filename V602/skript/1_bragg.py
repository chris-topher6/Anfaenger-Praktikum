import numpy as np
import matplotlib.pyplot as plt

theta, N = np.genfromtxt('data/Bragg.dat', unpack=True)

theta_theorie = 28
theta_peak = theta[np.argmax(N)]
print(f"Maximum: {theta_peak}° / {np.max(N)}")
print(f"Abweichung: {abs(theta_peak - theta_theorie):.2f}°")

plt.plot(theta, N, '-')
plt.axvline(theta_peak, linestyle='-', color='red', label=r'$\theta_{B, exp}$')
plt.axvline(theta_theorie, linestyle='--', color='gray', label=r'$\theta_{B, theo}$')

plt.xlabel(r'$θ_{GM} \;/\; °$')
plt.ylabel(r'$N$')
plt.legend()
plt.tight_layout()
plt.savefig('build/plot_bragg.pdf')
#plt.show()