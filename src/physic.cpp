# include <iostream>
# include "physic.hpp"
# include "partcule.hpp"

Physics::Physics() {
    this->constants = Constants();
}

Vect2D<float> Physics::getParticulesAttraction(const Particule &p1, const Particule &p2) const {
    Vect2D<float> dx = p2.pos - p1.pos;

    float length = dx.length();
    float force = this->constants.getK() * p1.q * p2.q / (length*length);
    force *= -1; // charge +- & -+ are attracted | ++ & -- are repulsed
    return dx.normalize() * force;
}

void Physics::handelnParticulesInteraction(Particule &p1, Particule &p2) const {
    Vect2D<float> force = this->getParticulesAttraction(p1, p2);
    p1.applyForce(force);
    p2.applyForce(force * -1);
}

void Physics::handelnMagneticInteraction(Particule &p, MagneticField &m) const {
    float B = m.getIntensity(p.pos);

    if (B == 0) {
        return;
    }

    // compute Lorentz force F = q * v * B
    Vect2D<float> force = p.v * (p.q * B);

    // compute normal to v
    float inter = force.x;
    force.x = force.y;
    force.y = -inter;
    
    // apply force
    p.applyForce(force);
}

MagneticField::MagneticField(Vect2D<float> origin, float intensity, float dispersion, bool isUniform) {
    this->origin = origin;
    this->intensity = intensity;
    this->isUniform = isUniform;

    if (dispersion == -1) {
        this->dispersion = this->defaultDispersion;
    } else {
        this->dispersion = dispersion;
    }
}

MagneticField::MagneticField(float x, float y, float intensity, float dispersion, bool isUniform) {
    this->origin = (Vect2D<float>(x, y));
    this->intensity = intensity;
    this->isUniform = isUniform;

    if (dispersion == -1) {
        this->dispersion = this->defaultDispersion;
    } else {
        this->dispersion = dispersion;
    }
}

float MagneticField::getIntensity(const Vect2D<float> &coordinate) const {
    float dist = (this->origin - coordinate).length();

    // handle to far coordinates
    if (dist >= this->dispersion) {
        return 0;
    }

    float coefDispersion;
    if (this->isUniform) {
        coefDispersion = 1;
    } else {
        coefDispersion = (this->dispersion - dist) / this->dispersion;
    }

    return coefDispersion * this->intensity;
}