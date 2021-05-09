# include <iostream>
# include "partcule.hpp"
# include "physic.hpp"

Particule::Particule(Vect2D<float> &pos, float q, float m) {
    this->pos = pos;
    this->q = q;
    this->m = m;
    this->v = Vect2D<float>(0,0);
    this->a = Vect2D<float>(0,0);
}

Particule::Particule(float x, float y, float q, float m) {
    this->pos = Vect2D<float>(x, y);
    this->q = q;
    this->m = m;
    this->v = Vect2D<float>(0,0);
    this->a = Vect2D<float>(0,0);
}

void Particule::applyForce(Vect2D<float> force) {
    this->a = this->a + force / m;
}

void Particule::updateState(float dt) {
    this->v = this->v + this->a * dt;
    this->pos = this->pos + this->v * dt;

    // reset acceleration
    this->a.x = 0;
    this->a.y = 0;
}

void Particule::print(){
    std::cout << "Particule (" << this->pos.x << ", " << this->pos.y << ") q: " << this->q << std::endl;
}