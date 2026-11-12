# -*- coding: utf-8 -*-
"""
Dette programmet regner om input i grader til radianer
"""

import numpy as np

v_grad = float(input('Skriv inn gradtallet:'))
 
v_rad = v_grad * np.pi / 180 # omregning fra grader til radianer

print(f'{v_grad} grader = {v_rad:.4f} radianer.')