#include <iostream>
#include <random>
#include "discos.hpp"

int main() {
    //Numero random para la velocidad
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(-3.0, 3.0); // rango para la velocidad

    // Crear los discos
    Disco d1(0.0, 0.0, 10.0, "red", dis(gen), dis(gen)); 
    Disco d2(15.0, 15.0, 10.0, "blue", dis(gen), dis(gen)); 

    // movimiento y colision
    double dt = 0.1;
    double width = 200.0;
    double height = 200.0;

    for (int i = 0; i < 100; ++i) {
        d1.move(dt);
        d2.move(dt);
        d1.check_wall_collision(width, height);
        d2.check_wall_collision(width, height);
        d1.check_disk_collision(d2);
    }

    // posiciones finales despues de 100 iteraciones
    std::cout << "Disk 1 final position: (" << d1.get_x_position() << ", " << d1.get_y_position() << ")\n";
    std::cout << "Disk 2 final position: (" << d2.get_x_position() << ", " << d2.get_y_position() << ")\n";

    return 0;
}
