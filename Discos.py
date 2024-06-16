import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.animation as animation

"""
Creo que lo mejor va a ser trabajar con objetos, quizá el proceso sea menos engorroso, de momento solo voy a declarar la clase 
para los discos. Voy dejando comentarios.

"""
class Disco:
    #Inicializamos la construcción del disco.
    def __init__(self, x_position, y_position, radio, Vx_velocity, Vy_velocy):
        self.x_position = x_position
        self.y_position = y_position
        self.radio = radio
        self.Vx_velocity = Vx_velocity
        self.Vy_velocity = Vy_velocy
    #Voy a incluir algunos métodos que considero apropiados.
    def mover():
        pass

    def collision_disk():
        pass

    def collision_wall():
        pass

    #Posiblemente hagan falta más



"""
Una función para animar los discos por medio de matplotlib, utilizando funcAnimation de matplotlib.
"""
def animation():
        pass