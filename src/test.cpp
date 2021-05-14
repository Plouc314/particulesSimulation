# include <iostream>
# include <vector>
# include "physic.hpp"
# include "partcule.hpp"
# include "system.hpp"

int main() {
    
    Particule p1(0, 0, 1, 1);
    Particule p2(0, 1, -1, 1);
    Particule p3(1, 1, 1, 1);

    std::vector<Particule> particules = {p1, p2, p3};

    System system = System(particules, 1);
    system.physic.constants.setK(1);
    // system.setLimits(0, 10, 0, 10);

    system.print();
    system.updateState();
    system.print();
    system.updateState();
    system.print();
    system.updateState();
    system.print();
    system.updateState();
    system.print();

    Vect2D<float> origin(2,3);
    auto magnetic = MagneticField(origin, 10);

    Vect2D<float> coord(3,3);
    std::cout << magnetic.getIntensity(coord) << std::endl;

    std::cout << "number: " << -23 << " -> " << sign(-23) << std::endl;

    return 0;
}
