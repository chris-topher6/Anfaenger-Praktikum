#Kleines Beispiel für das Abspeichern
import matplotlib.pyplot as plt
import numpy as np

print('test')
plt.figure()
x = np.linspace(0, 1)
plt.plot(x, x**2)
plt.savefig('build/test.pdf')