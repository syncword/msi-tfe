import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

x = np.linspace(0.0, 2*np.pi, 1000)

y1 = np.sin(20*x)

y2 = 1.5 + np.sin(2*x)
y3 = 1.5 + signal.square(np.pi * x)
y4 = (y2 * y1)
y5 = (y3 * y1)

plots = []
p1 = plt.subplot(5, 1, 1)
plt.plot(x, y1, color='steelblue')
plt.ylabel('Portadora')
plots.append(p1)

p2 = plt.subplot(5, 1, 2)
plt.plot(x, y2,color='red')
plt.ylabel('Analogica')
plots.append(p2)

p3 = plt.subplot(5, 1, 3)
plt.plot(x, y4, color='green')
plt.plot(x, y2, linestyle='dashed', color='steelblue')
plt.plot(x, -y2, linestyle='dashed', color='steelblue')
plt.ylabel('AM')
plots.append(p3)

p4 = plt.subplot(5, 1, 4)
plt.plot(x, y3,color='red')
plt.ylabel('Digital')
plots.append(p4)

p5 = plt.subplot(5, 1, 5)
plt.plot(x, y5, color='green')
plt.plot(x, y3, linestyle='dashed', color='steelblue')
plt.plot(x, -y3, linestyle='dashed', color='steelblue')
plt.ylabel('ASK')
plots.append(p5)


for plot in plots:
    plot.axes.get_xaxis().set_ticks([])
    plot.axes.get_yaxis().set_ticks([])

plt.show()