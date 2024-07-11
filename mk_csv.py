from Discos import DiscoSimulation

from Discos import Disco

import csv

import numpy as np

# Example usage
width = 10
height = 10

N = 4
Radius = np.sqrt(4/N)*0.5
sim = DiscoSimulation(N, 5, 5, Radius)
disks = sim.disk_creation()

sim.animate_movement()

M= 1000

def guardar_lista_en_csv(lista, nombre_archivo):
    with open(nombre_archivo, mode='w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        for fila in lista:
            escritor_csv.writerow(fila)



while True:
    if len(disks[0].x_positions) > M:

        lista = [[sim.get_positions()[j][0][i] for i in range(M)] for j in range(N)]
        """"
        lista = [disks[k].x_positions[:M] for k in range(N)]
"""
        if __name__ == "__main__":
    
        #Guarda la lista en un archivo CSV
            archivo = 'positions.csv'
            guardar_lista_en_csv(lista, archivo)
            print(f"Lista guardada en {archivo}")

        break

print("El tamaño de xpos1 es " + str(len(disks[0].x_positions)))
print("El tamaño del get es " + str(len(sim.get_positions()[2][1])))
print("El tamaño de lista es " + str(len(lista)) + "x" + str(len(lista[0])))

print("Ya el programa corrió")