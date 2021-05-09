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

        std::vector<float> getListPos() const { return {pos.x, pos.y}; }
        std::vector<float> getListV() const { return {v.x, v.y}; }
        std::vector<float> getListA() const { return {a.x, a.y}; }
        void setListPos(std::vector<float> list) { pos = Vect2D<float>(list); }
        void setListV(std::vector<float> list) { v = Vect2D<float>(list); }
        void setListA(std::vector<float> list) { a = Vect2D<float>(list); }

        void applyForce(Vect2D<float> force);
        void updateState(float dt);

        void print();
};