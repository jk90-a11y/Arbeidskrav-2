# -*- coding: utf-8 -*-
"""
Dette programmet plotter funksjonen f(x) = -x^2 -5 på intervallet [-10, 10]
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
y = -x**2 -5

plt.plot(x, y,label='f(x) = -x² - 5') # plotter graf
plt.xlabel('x') # label på x-akse
plt.ylabel('f(x)') # label på y-akse
plt.title('Kurveplot av f(x) = -x² - 5') # overskrift
plt.grid(True) # rutenett
plt.legend() # plotter forklaring av grafen
plt.show()