# pragma once
# include <iostream>
# include <vector>
# include "partcule.hpp"
# include "physic.hpp"

class Particule;

class System{
    public:
        Physics physic;
        std::vector<Particule> particules;
        float dt;

        System(std::vector<Particule> &particules, float dt=-1);

        const Constants& constants() { return physic.constants; }
        
        void updateState(float dt=-1);

        void print();
};