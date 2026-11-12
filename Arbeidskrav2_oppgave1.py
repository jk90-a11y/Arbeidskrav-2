"""
Dette programmet beregner alder i 2024 basert på input av fødselsår og printer
utregningen.
"""

alder = int(input('Hvilket år er du født? ')) # input alder som int
 
alder_2024 = 2024 - alder # utregning av alder i 2024
 
print(f'Du blir {alder_2024} år i løpet av 2024.')