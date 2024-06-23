import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches


class Disco:
    def __init__(self, x_position, y_position, radio, color, Vx, Vy):
        self.x_position = x_position
        self.y_position = y_position
        self.radio = radio
        self.color = color
        self.Vx = Vx
        self.Vy = Vy

    def mover(self, x_0, y_0):
        time = np.linspace(0.0, 10, 1000)
        self.x_position = np.zeros(np.size(time))
        self.y_position = np.zeros(np.size(time))

        self.x_position[0] = x_0
        self.y_position[0] = y_0

        h = time[1] - time[0]

        for i in range(len(time) - 1):
            self.x_position[i + 1] = self.x_position[i] + self.Vx * h
            self.y_position[i + 1] = self.y_position[i] + self.Vy * h 

            self.collision_wall(i + 1)
        return time, self.x_position, self.y_position

    def collision_wall(self, i):
        if self.x_position[i] - self.radio <= -0.5 or self.x_position[i] + self.radio >= 0.5:
            self.Vx = -self.Vx
        if self.y_position[i] - self.radio <= -0.5 or self.y_position[i] + self.radio >= 0.5:
            self.Vy = -self.Vy

    def animate_movement(self, x_0, y_0):
        fig, ax = plt.subplots()
        ax.set_xlim((-0.5, 0.5))
        ax.set_ylim((-0.5, 0.5))
        ax.set_xlabel('Posición en X')
        ax.set_ylabel('Posición en Y')

        time, self.x_positions, self.y_positions = self.mover(x_0, y_0)

        disco = patches.Circle((self.x_position[0], self.y_position[0]), radius=self.radio, color=self.color)
        ax.add_patch(disco)

        

        def init():
            disco.center = (self.x_position[0], self.y_position[0])
            return (disco,)

        def animate(i):
            disco.center = (self.x_position[i], self.y_position[i])
            return (disco,)

        anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(time), interval=50, blit=True)
        plt.show()


# Ejemplo de uso
disco = Disco(0, 0, 0.2, 'green', -1, -0.5)
disco.animate_movement(0, 0)




        


    #Posiblemente hagan falta más



