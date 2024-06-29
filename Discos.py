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

    def mover(self, x_0, y_0, other_disc=None):
        time = np.linspace(0.0, 10, 1000)
        self.x_position = np.zeros(np.size(time))
        self.y_position = np.zeros(np.size(time))

        self.x_position[0] = x_0
        self.y_position[0] = y_0

        if other_disc:
            other_disc.x_position = np.zeros(np.size(time))
            other_disc.y_position = np.zeros(np.size(time))
            other_disc.x_position[0] = other_disc.x_position_initial
            other_disc.y_position[0] = other_disc.y_position_initial

        h = time[1] - time[0]

        for i in range(len(time) - 1):
            self.x_position[i + 1] = self.x_position[i] + self.Vx * h
            self.y_position[i + 1] = self.y_position[i] + self.Vy * h 

            self.collision_wall(i + 1)
            if other_disc:
                other_disc.x_position[i + 1] = other_disc.x_position[i] + other_disc.Vx * h
                other_disc.y_position[i + 1] = other_disc.y_position[i] + other_disc.Vy * h
                other_disc.collision_wall(i + 1)
                self.collision_disc(other_disc, i + 1)
                
        return time, self.x_position, self.y_position

    def collision_wall(self, i):
        if self.x_position[i] - self.radio <= -0.5 or self.x_position[i] + self.radio >= 0.5:
            self.Vx = -self.Vx
        if self.y_position[i] - self.radio <= -0.5 or self.y_position[i] + self.radio >= 0.5:
            self.Vy = -self.Vy

    def collision_disc(self, other, i):
        dx = self.x_position[i] - other.x_position[i]
        dy = self.y_position[i] - other.y_position[i]
        distance = np.sqrt(dx**2 + dy**2)
        if distance < self.radio + other.radio:
            # Reflect velocities upon collision
            self.Vx, other.Vx = other.Vx, self.Vx
            self.Vy, other.Vy = other.Vy, self.Vy

    def animate_movement(self, x_0, y_0, other_disc=None):
        fig, ax = plt.subplots()
        ax.set_xlim((-0.5, 0.5))
        ax.set_ylim((-0.5, 0.5))
        ax.set_xlabel('Posición en X')
        ax.set_ylabel('Posición en Y')

        self.x_position_initial = x_0
        self.y_position_initial = y_0

        if other_disc:
            other_disc.x_position_initial = other_disc.x_position
            other_disc.y_position_initial = other_disc.y_position

        time, self.x_positions, self.y_positions = self.mover(x_0, y_0, other_disc)
        
        moving_disco = patches.Circle((self.x_position[0], self.y_position[0]), radius=self.radio, color=self.color)
        ax.add_patch(moving_disco)
        
        if other_disc:
            static_disco = patches.Circle((other_disc.x_position[0], other_disc.y_position[0]), radius=other_disc.radio, color=other_disc.color)
            ax.add_patch(static_disco)

        def init():
            moving_disco.center = (self.x_position[0], self.y_position[0])
            if other_disc:
                static_disco.center = (other_disc.x_position[0], other_disc.y_position[0])
            return (moving_disco, static_disco) if other_disc else (moving_disco,)

        def animate(i):
            moving_disco.center = (self.x_position[i], self.y_position[i])
            if other_disc:
                static_disco.center = (other_disc.x_position[i], other_disc.y_position[i])
            return (moving_disco, static_disco) if other_disc else (moving_disco,)

        anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(time), interval=50, blit=True)
        plt.show()


# Ejemplo de uso
disco1 = Disco(0, 0, 0.2, 'green', -1, -0.5)
disco2 = Disco(0.2, 0.2, 0.1, 'red', 0.5, 0.5)

disco1.animate_movement(0, 0, other_disc=disco2)