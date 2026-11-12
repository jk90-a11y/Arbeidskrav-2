# -*- coding: utf-8 -*-

"""a) Opprett dictionary"""

data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
    }
 

"""b) Slå opp et land og skriv ut setning"""

land = input('Skriv inn et land: ') #input land
 
if land in data:
    hovedstad, innbyggere = data[land]
    print(f'{hovedstad} er hovedstaden i {land} og det er {innbyggere} mill. innbyggere i {hovedstad}')
else:
    print(f'{land} finnes ikke i dictionaryen.')
    
    
"""c) Legg til et nytt land"""

nytt_land = input('Skriv inn et nytt land: ')
 
while nytt_land in data:
    nytt_land = input(f'{nytt_land} finnes allerede. Skriv inn et annet land: ')
 
ny_hovedstad = input(f'Skriv inn hovedstaden i {nytt_land}: ')
nye_innbyggere = float(input(f'Skriv inn antall innbyggere i {ny_hovedstad} (i mill.): '))
 
data[nytt_land] = [ny_hovedstad, nye_innbyggere]
 
print(data)