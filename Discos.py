import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.animation as animation


class Disco:
    # Inicializamos la construcción del disco.
    def __init__(self, x_position, y_position, radio, color, Vx, Vy):
        self.x_position = x_position
        self.y_position = y_position
        self.radio = radio
        self.color = color
        self.Vx = Vx
        self.Vy = Vy

    def mover(self, x_0, y_0, t_max, N, width, height):
        """
        Método de la clase discos, la cual toma la posición inicial en ambas coordenadas, la velocidad, el tiempo máximo
        y la cantidad de particiones.

        Parameters:
        x_0 (float): Posición inicial del disco en x.
        y_0 (float): Posición inicial del disco en y.
        t_max (float): Tiempo total de muestreo.
        N (int): Cantidad de particiones del tiempo.

        Returns:
        tuple: (time, x_positions, y_positions) Devuelve el arreglo de tiempo y los arreglos de las posiciones individualmente.
        """
        time = np.linspace(0, t_max, N)
        x_positions = np.zeros(np.size(time))
        y_positions = np.zeros(np.size(time))

        for i in range(np.size(time)-1):
            self.x_position = x_0 + self.Vx * time[i]
            self.y_position = y_0 + self.Vy * time[i]
            self.collision_wall(width, height)



            x_positions[i] = x_0 + self.Vx * time[i]
            y_positions[i] = y_0 + self.Vy * time[i]

            

        return time, x_positions, y_positions

    def collision_wall(self, width, height):
        """
        Método para manejar la colisión del disco con las paredes.

        Parameters:
        width (float): Ancho del área donde se mueve el disco.
        height (float): Altura del área donde se mueve el disco.

        Modifica las velocidades `Vx` y `Vy` si el disco colisiona con las paredes.
        """
        if self.x_position - self.radio < 0 or self.x_position + self.radio > width:
            self.Vx = -self.Vx
        if self.y_position - self.radio < 0 or self.y_position + self.radio > height:
            self.Vy = -self.Vy
        





def collision_wall(self):
        for i in range():
            pass
         
        


    #Posiblemente hagan falta más



"""

Una función para animar los discos por medio de matplotlib, utilizando funcAnimation de matplotlib.
"""
def animation():
        pass