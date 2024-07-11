import csv

import matplotlib.pyplot as plt

import numpy as np



fig, ax = plt.subplots()

Divisions = 50

N = 4

file = 'positions.csv'

all_positions_str = []

with open(file, 'r') as file:
    lector_csv = csv.reader(file)
    
    for row in lector_csv:
        all_positions_str.extend(row)



all_positions = [float(i) for i in all_positions_str]

plt.rcParams.update({'figure.figsize':(7,5), 'figure.dpi':100})

weights = np.ones_like(all_positions) / (len(all_positions)/N)
plt.hist(all_positions, bins=Divisions, weights=weights)
plt.gca().set(title='Histograma de probabilidad para 4 discos', ylabel='Probabilidad')
plt.xlim(-2.5, 2.5)
plt.xlabel("Posición x")
plt.show()
