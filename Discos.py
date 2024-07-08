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

        if self.x_position - self.radio <= -width / 2:

            self.Vx *= -1.0

            self.x_position = (-1.0 * width / 2) + self.radio

        elif self.x_position + self.radio >= width / 2:

            self.Vx *= -1.0

            self.x_position = (width / 2) - self.radio

        elif self.y_position - self.radio <= -height / 2:

            self.Vy *= -1.0

            self.y_position = (-1.0 * height / 2) + self.radio

        elif self.y_position + self.radio >= height / 2:

            self.Vy *= -1.0

            self.y_position = (width / 2) - self.radio



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

        return self.discos

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

def time_to_wall_collision(disk, width, height):
    tx_min = float('inf')
    ty_min = float('inf')

    if disk.Vx > 0:
        tx_min = (width / 2 - disk.radio - disk.x_position) / disk.Vx
    elif disk.Vx < 0:
        tx_min = (-width / 2 + disk.radio - disk.x_position) / disk.Vx

    if disk.Vy > 0:
        ty_min = (height / 2 - disk.radio - disk.y_position) / disk.Vy
    elif disk.Vy < 0:
        ty_min = (-height / 2 + disk.radio - disk.y_position) / disk.Vy

    return min(tx_min, ty_min)

def time_to_disk_collision(disk1, disk2):
    R_rel = np.array([disk1.x_position - disk2.x_position, disk1.y_position - disk2.y_position])
    V_rel = np.array([disk1.Vx - disk2.Vx, disk1.Vy - disk2.Vy])
    R_rel_dot_V_rel = np.dot(R_rel, V_rel)
    V_rel_square = np.dot(V_rel, V_rel)
    R_rel_square = np.dot(R_rel, R_rel)
    sum_radius = disk1.radio + disk2.radio

    if V_rel_square == 0:
        return float('inf')

    a = V_rel_square
    b = 2 * R_rel_dot_V_rel
    c = R_rel_square - sum_radius**2

    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return float('inf')

    t1 = (-b - np.sqrt(discriminant)) / (2 * a)
    t2 = (-b + np.sqrt(discriminant)) / (2 * a)

    if t1 > 0 and t2 > 0:
        return min(t1, t2)
    elif t1 > 0:
        return t1
    elif t2 > 0:
        return t2
    else:
        return float('inf')

def determine_collision_event(disk1, disk2, width, height):
    t_wall_collision1 = time_to_wall_collision(disk1, width, height)
    t_wall_collision2 = time_to_wall_collision(disk2, width, height)
    t_disk_collision = time_to_disk_collision(disk1, disk2)

    min_time = min(t_wall_collision1, t_wall_collision2, t_disk_collision)

    if min_time == t_disk_collision:
        return 'disk_collision', min_time
    elif min_time == t_wall_collision1:
        return 'wall_collision_disk1', min_time
    else:
        return 'wall_collision_disk2', min_time

# Example usage
width = 10
height = 10



sim = DiscoSimulation(2, 5, 5, 0.5)

disks = sim.disk_creation()

disk1, disk2 = disks[0], disks[1]

sim.animate_movement()

event, time = determine_collision_event(disk1, disk2, width, height)
print(f"The first event is a {event} occurring at t = {time:.2f} seconds")

# Obtener posiciones registradas

positions = sim.get_positions()
