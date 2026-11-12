# -*- coding: utf-8 -*-
"""
Dette programmet beregner antall pizzaer basert på antall personer i input
Hver elev spiser 1/4 pizza. Resultat rundes opp til nærmeste heltall.
"""

import math
 
antall_elever = int(input('Skriv inn antall elever:')) # henter inn antall elever basert på input.
 
antall_pizzaer = math.ceil(antall_elever / 4) # antall pizzaer rundes opp til nærmeste heltall
 
print(f'Det må handles inn {antall_pizzaer} pizzaer til festen.')
