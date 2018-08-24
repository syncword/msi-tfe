import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

x = np.linspace(0.0, 2*np.pi, 1000)

y1 = np.sin(20*x)
y2 = 1.5 + np.cos(2*x)
y3 = (y2 * np.cos(20*x))

plots = []
p1 = plt.subplot(3, 1, 1)
plt.plot(x, y2,color='red')
plt.title('Modulación AM')
plt.ylabel('Señal')
plots.append(p1)

p2 = plt.subplot(3, 1, 2)
plt.plot(x, y1, color='steelblue')
plt.ylabel('Onda portadora')
plots.append(p2)

p3 = plt.subplot(3, 1, 3)
plt.plot(x, y3, color='green')
plt.plot(x, y2, linestyle='dashed', color='steelblue')
plt.plot(x, -y2, linestyle='dashed', color='steelblue')
plt.ylabel('Onda modulada')
plots.append(p3)

for plot in plots:
    plot.axes.get_xaxis().set_ticks([])
    plot.axes.get_yaxis().set_ticks([])

plt.show()