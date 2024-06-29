import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import random

class Disco:
    def __init__(self, x_position, y_position, radio, color, Vx, Vy):
        self.x_position = x_position
        self.y_position = y_position
        self.radio = radio
        self.color = color
        self.Vx = Vx
        self.Vy = Vy
        self.x_positions = [x_position]  # Lista para almacenar posiciones x a lo largo del tiempo
        self.y_positions = [y_position]  # Lista para almacenar posiciones y a lo largo del tiempo

    def move(self, dt):
        self.x_position += self.Vx * dt
        self.y_position += self.Vy * dt
        self.x_positions.append(self.x_position)  # Registrar nueva posición x
        self.y_positions.append(self.y_position)  # Registrar nueva posición y

    def check_wall_collision(self, width, height):
        if self.x_position - self.radio <= -width / 2 or self.x_position + self.radio >= width / 2:
            self.Vx = -self.Vx
        if self.y_position - self.radio <= -height / 2 or self.y_position + self.radio >= height / 2:
            self.Vy = -self.Vy

    def check_disk_collision(self, other_disk):
        dx = self.x_position - other_disk.x_position
        dy = self.y_position - other_disk.y_position
        distance = np.sqrt(dx**2 + dy**2)

        if distance < self.radio + other_disk.radio:
            collision_normal = np.array([dx, dy]) / distance
            relative_velocity = np.array([self.Vx - other_disk.Vx, self.Vy - other_disk.Vy])
            relative_speed = np.dot(relative_velocity, collision_normal)

            if relative_speed < 0:
                self.Vx -= relative_speed * collision_normal[0]
                self.Vy -= relative_speed * collision_normal[1]
                other_disk.Vx += relative_speed * collision_normal[0]
                other_disk.Vy += relative_speed * collision_normal[1]

            # Registra las posiciones después de la colisión
            self.x_positions[-1] = self.x_position
            self.y_positions[-1] = self.y_position
            other_disk.x_positions[-1] = other_disk.x_position
            other_disk.y_positions[-1] = other_disk.y_position


class DiscoSimulation:
    def __init__(self, N, alto, ancho, radio):
        self.N = N  # Cantidad de discos
        self.altura = alto
        self.ancho = ancho
        self.radio = radio
        self.discos = []

    def disk_creation(self):
        for _ in range(self.N):
            while True:
                x_position = random.uniform(-self.ancho / 2 + self.radio, self.ancho / 2 - self.radio)
                y_position = random.uniform(-self.altura / 2 + self.radio, self.altura / 2 - self.radio)
                color = random.choice(['red', 'blue', 'green', 'yellow'])
                Vx = random.uniform(-3, 3)
                Vy = random.uniform(-3, 3)

                # Ajustar para evitar valores excesivamente pequeños
                while abs(Vx) < 1.0 or abs(Vy) < 1.0:
                    Vx = random.uniform(-3, 3)
                    Vy = random.uniform(-3, 3)

                # Crear disco y añadirlo a la lista
                disco = Disco(x_position, y_position, self.radio, color, Vx, Vy)
                self.discos.append(disco)

                # Comprobar colisiones con otros discos
                colision = False
                for other in self.discos[:-1]:
                    if np.sqrt((disco.x_position - other.x_position)**2 + (disco.y_position - other.y_position)**2) < disco.radio + other.radio:
                        colision = True
                        break

                if not colision:
                    break

    def animate_movement(self):
        fig, ax = plt.subplots()
        ax.set_xlim(-self.ancho / 2, self.ancho / 2)
        ax.set_ylim(-self.altura / 2, self.altura / 2)
        ax.set_aspect('equal')

        patches_list = []
        for disco in self.discos:
            circle = patches.Circle((disco.x_position, disco.y_position), radius=disco.radio, color=disco.color)
            ax.add_patch(circle)
            patches_list.append(circle)

        def init():
            return patches_list

        def animate(i):
            dt = 0.05  # Tiempo discretizado ajustado para coincidir con el intervalo de 50ms

            # Mover discos y verificar colisiones con paredes
            for disco in self.discos:
                disco.move(dt)
                disco.check_wall_collision(self.ancho, self.altura)

            # Verificar colisiones entre discos
            for i in range(len(self.discos)):
                for j in range(i + 1, len(self.discos)):
                    self.discos[i].check_disk_collision(self.discos[j])

            # Actualizar posiciones de los parches
            for index, disco in enumerate(self.discos):
                patches_list[index].center = (disco.x_position, disco.y_position)

            return patches_list

        ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=50, blit=True)
        plt.show()

    def get_positions(self):
        positions = []
        for disco in self.discos:
            positions.append((disco.x_positions, disco.y_positions))
        return positions

sim = DiscoSimulation(1, 5, 5, 0.9)
sim.disk_creation()
sim.animate_movement()

# Obtener posiciones registradas
positions = sim.get_positions()