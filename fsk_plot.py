# -*- coding: utf-8 -*-
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

t = np.linspace(0.0, 2 * np.pi, 1000)

c = np.sin(20 * t) # carrier

m_analog = np.sin(2 * t)
m_digital = 10*signal.square(2 * t)
fm = np.sin(20 * t + ( 5 * m_analog) )
fsk = np.cos(2 * np.pi * (2 * np.pi + m_digital) * t  )

plots = []
plot_carrier = plt.subplot(5, 1, 1)
plt.plot(t, c, color='steelblue')
plt.ylabel('Portadora')
plots.append(plot_carrier)

plot_m_analog = plt.subplot(5, 1, 2)
plt.plot(t, m_analog,color='red')
plt.ylabel('Analogica')
plots.append(plot_m_analog)

plot_fm = plt.subplot(5, 1, 3)
plt.plot(t, fm, color='green')
plt.ylabel('FM')
plots.append(plot_fm)

plot_m_digital = plt.subplot(5, 1, 4)
plt.plot(t, m_digital, color='red')
plt.ylabel('Digital')
plots.append(plot_m_digital)

plot_fsk = plt.subplot(5, 1, 5)
plt.plot(t, fsk, color='green')
plt.ylabel('FSK')
plots.append(plot_fsk)


for plot in plots:
    plot.axes.get_xaxis().set_ticks([])
    plot.axes.get_yaxis().set_ticks([])

plt.show()