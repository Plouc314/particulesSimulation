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

    system.print();
    system.updateState();
    system.print();

    p1 = system.particules[0];

    std::vector<float> v = p1.getListV();

    std::cout << v[0] << ' ' << v[1] << std::endl;

    return 0;
}
