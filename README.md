# Anfänger-Praktikum

## Wichtiger Hinweis zu `make`

Da `make` jetzt funktioniert, ist die Ordnung eine andere:

- Die `.dat`-Dateien sind im Ordner 'data'
- Die `.py`-Dateien  sind im Ordner 'skript'
- Die Plots, so wie auch alles andere werden in 'build' gespeichert


Ein Beispiel für das Erstellen eines Plots wäre demnach in der `.py`-Datei:

```python
a, b = np.genfromtxt('data/mess1.dat', unpack=True)
plt.figure()
plt.plot(a,b)
plt.savefig('build/plot1.pdf')
```
