# include <iostream>
# include "system.hpp"
# include "physic.hpp"
# include "partcule.hpp"

System::System(std::vector<Particule> &particules, float dt) {
    this->physic = Physics();
    this->particules = particules;

    if (dt == -1) {
        dt = this->physic.constants.defaultDt;
    }
    this->dt = dt;
}

void System::updateState(float dt) {

    if (dt == -1) {
        dt = this->dt;
    }

    // perform all interactions
    for (int i=0; i<particules.size()-1; i++) {
        for (int j=i+1; j<particules.size(); j++) {
            physic.handelnParticulesInteraction(
                particules[i],
                particules[j]
            );
        }
    }

    // update state
    for (int i=0; i<particules.size(); i++){
        particules[i].updateState(dt);
    }
}

void System::print() {
    std::cout << "System : " << particules.size() << " particules." << std::endl;
    for (int i=0; i<particules.size(); i++) {
        particules[i].print();
    }
}