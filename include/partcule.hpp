# pragma once
# include <string>
# include <vector>
# include "physic.hpp"
# include "math.hpp"


class Particule {
    public:
        Vect2D<float> pos, v, a;
        float q, m;
        
        Particule(Vect2D<float> &pos, float q, float m);
        Particule(float x, float y, float q, float m);
        
        float getX() const { return pos.x; }
        void setX(float x) { pos.x = x; }

        float getY() const { return pos.y; }
        void setY(float y) { pos.y = y; }

        std::vector<float> getListPos() const { return {pos.x, pos.y}; }
        std::vector<float> getListV() const { return {v.x, v.y}; }
        std::vector<float> getListA() const { return {a.x, a.y}; }

        void applyForce(Vect2D<float> force);
        void updateState(float dt);

        void print();
};