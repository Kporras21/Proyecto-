#ifndef DISCO_HPP
#define DISCO_HPP

#include <vector>
#include <string>

class Disco {
private:
    double x_position;
    double y_position;
    double radio;
    std::string color;
    double Vx;
    double Vy;
    std::vector<double> x_positions;  // position x over time
    std::vector<double> y_positions;  // position y over time
    //Default Constructor
    Disco();

public:
    // Custom Constructor
    Disco(double x_position, double y_position, double radio, const std::string& color, double Vx, double Vy);

    // metodos
    void move(double dt);
    void check_wall_collision(double width, double height);
    void check_disk_collision(Disco& other_disk);

    // acceso variables privadas
    double get_x_position() const;
    double get_y_position() const;
    double get_radio() const;
    const std::string& get_color() const;
    double get_Vx() const;
    double get_Vy() const;
    const std::vector<double>& get_x_positions() const;
    const std::vector<double>& get_y_positions() const;
};

#endif // DISCO_HPP



