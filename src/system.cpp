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

void System::setLimits(float minX, float maxX, float minY, float maxY) {
    this->isLimits = true;
    this->minX = minX;
    this->maxX = maxX;
    this->minY = minY;
    this->maxY = maxY;
}

void System::clearElements() {
    this->particules.clear();
    this->magneticFields.clear();
}

void System::updateState(float dt) {

    if (dt == -1) {
        dt = this->dt;
    }

    // perform all particules interactions
    if (particules.size() > 1) {

        for (int i=0; i<particules.size()-1; i++) {
            for (int j=i+1; j<particules.size(); j++) {
                physic.handelnParticulesInteraction(
                    particules[i],
                    particules[j]
                );
            }
        }
    }

    // perfom all magnetics interactions
    for (int i=0; i<magneticFields.size(); i++) {
        for (int j=0; j<particules.size(); j++) {
            physic.handelnMagneticInteraction(
                particules[j],
                magneticFields[i]
            );
        }
    }

    // update state
    // remove particules out of bounds
    for (int i=particules.size()-1; i>-1; i--){
        particules[i].updateState(dt);
        
        if (!isInLimits(particules[i])) {
            particules.erase(particules.begin() + i);
        }
    }

}

bool System::isInLimits(Particule &p) {
    if (!isLimits) {
        return true;
    } else if (
        (p.pos.x > minX) &
        (p.pos.x < maxX) &
        (p.pos.y > minY) &
        (p.pos.y < maxY)
        ) 
    {
        return true;
    }
    return false;
}

void System::addMagneticField(MagneticField &magneticField) {
    magneticFields.push_back(magneticField);
}

void System::addParticule(Particule &particule) {
    particules.push_back(particule);
}

void System::print() {
    std::cout << "System : " << particules.size() << " particules." << std::endl;
    for (int i=0; i<particules.size(); i++) {
        particules[i].print();
    }
}