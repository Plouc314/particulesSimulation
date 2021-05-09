# include <iostream>
# include "physic.hpp"
# include "partcule.hpp"

Physics::Physics() {
    this->constants = Constants();
}

Vect2D<float> Physics::getParticulesAttraction(const Particule &p1, const Particule &p2) {
    Vect2D<float> dx = p2.pos - p1.pos;

    float length = dx.length();
    float force = this->constants.getK() * p1.q * p2.q / (length*length);
    force *= -1; // charge +- & -+ are attracted | ++ & -- are repulsed
    return dx.normalize() * force;
}

void Physics::handelnParticulesInteraction(Particule &p1, Particule &p2) {
    Vect2D<float> force = this->getParticulesAttraction(p1, p2);
    p1.applyForce(force);
    p2.applyForce(force * -1);
}