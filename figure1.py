# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 09:05:06 2017

@author: carreau
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

def fonction(x, tau, omega):
    """La fonction à tracer"""
    return np.exp(-x / tau) * np.sin(omega * x)

x = np.linspace(0., 10., 1000)
y1 = fonction(x, 10., 2. * np.pi)
y2 = fonction(x, 3., 4. * np.pi)

plt.rc('text', usetex=True)
plt.rc('font', family='serif', weight='normal', style='normal')
#rcParams['font.serif'] = ['Palatino'] #choix de fonte
plt.rc('text.latex', preamble =
       """\usepackage[T1]{fontenc}
       \usepackage[bitstream-charter]{mathdesign}
       """)
rcParams["xtick.labelsize"] = 16.
rcParams["ytick.labelsize"] = 9.
rcParams['axes.labelsize'] = 10.
rcParams['axes.titlesize'] = 12.
rcParams['legend.fontsize'] = 10.
width = 6.69 # largeur en pouces
height = width /2. #hauteur

fig = plt.figure(figsize = (width,height))
plt.plot(x, y1, label = r"$\tau = 10, \ \omega = 2 \pi$")
plt.plot(x, y2, label = r"$\tau = 3, \ \omega = 4 \pi$")
plt.grid()
plt.legend(loc = "best")
plt.xlabel("Temps $t$")
plt.ylabel("Amplitude $y(t)$")
plt.title(r"Oscillateur amorti : $y(t) = \exp(-t/\tau)\sin(\omega t)$")
#plt.show()
plt.tight_layout()
plt.savefig("Oscillateur.pdf")
