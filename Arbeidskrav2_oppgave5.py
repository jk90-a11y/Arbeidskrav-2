# -*- coding: utf-8 -*-
"""
Dette programmet regner ut areal og omrkrets av en gitt figur med mål A og B
"""

import numpy as np

def areal_omkrets(a, b):
    r=a/2
    
    areal_trekant = a*b/2
    areal_halvsirkel = np.pi*r*r/2
    areal = areal_trekant + areal_halvsirkel
    
    omkrets_hyp=np.sqrt(a*a + b*b)
    omkrets_halvsirkel=np.pi*r
    omkrets = b+omkrets_hyp+omkrets_halvsirkel
    
    return areal, omkrets

a = float(input('Skriv inn a: '))
b = float(input('Skriv inn b: ')) 

areal, omkrets = areal_omkrets(a, b)

print(f'Arealet av figuren er {areal:.2f}')
print(f'Omkretsen av figuren er {omkrets:.2f}')