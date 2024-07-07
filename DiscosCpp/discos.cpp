#include "discos.hpp"
#include <cmath>
#include <algorithm>

// Constructor
Disco::Disco(double x_position, double y_position, double radio, const std::string& color, double Vx, double Vy)
    : x_position(x_position), y_position(y_position), radio(radio), color(color), Vx(Vx), Vy(Vy) {
    x_positions.push_back(x_position);
    y_positions.push_back(y_position);
}

// Metodos
void Disco::move(double dt) {
    x_position += Vx * dt;
    y_position += Vy * dt;
    x_positions.push_back(x_position);
    y_positions.push_back(y_position);
}

//Colision pared
void Disco::check_wall_collision(double width, double height) {
    if (x_position - radio <= -width / 2) {
        Vx *= -1.0;
        x_position = (-width / 2) + radio;
    }
    else if (x_position + radio >= width / 2) {
        Vx *= -1.0;
        x_position = (width / 2) - radio;
    }
    else if (y_position - radio <= -height / 2) {
        Vy *= -1.0;
        y_position = (-height / 2) + radio;
    }
    else if (y_position + radio >= height / 2) {
        Vy *= -1.0;
        y_position = (height / 2) - radio;
    }
}

//Colision discos
void Disco::check_disk_collision(Disco& other_disk) {
    double dx = x_position - other_disk.x_position;
    double dy = y_position - other_disk.y_position;
    double distance = std::sqrt(dx * dx + dy * dy);

    if (distance < radio + other_disk.radio) {
        std::vector<double> collision_normal = { dx / distance, dy / distance };
        std::vector<double> relative_velocity = { Vx - other_disk.Vx, Vy - other_disk.Vy };
        double relative_speed = relative_velocity[0] * collision_normal[0] + relative_velocity[1] * collision_normal[1];

        if (relative_speed < 0) {
            Vx -= relative_speed * collision_normal[0];
            Vy -= relative_speed * collision_normal[1];
            other_disk.Vx += relative_speed * collision_normal[0];
            other_disk.Vy += relative_speed * collision_normal[1];
        }

        // Posicion despues de la colision
        x_positions.back() = x_position;
        y_positions.back() = y_position;
        other_disk.x_positions.back() = other_disk.x_position;
        other_disk.y_positions.back() = other_disk.y_position;
    }
}

// Accesos a las variables privadas
double Disco::get_x_position() const { return x_position; }
double Disco::get_y_position() const { return y_position; }
double Disco::get_radio() const { return radio; }
const std::string& Disco::get_color() const { return color; }
double Disco::get_Vx() const { return Vx; }
double Disco::get_Vy() const { return Vy; }
const std::vector<double>& Disco::get_x_positions() const { return x_positions; }
const std::vector<double>& Disco::get_y_positions() const { return y_positions; }



