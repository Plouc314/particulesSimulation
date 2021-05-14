# include <iostream>
# include "system.hpp"
# include "physic.hpp"
# include "partcule.hpp"

# define LOG(x) std::cout << x << std::endl;

System::System(std::vector<Particule> &particules, float dt, int flag) {
    this->physic = Physics();
    this->particules = particules;

    if (dt == -1) {
        dt = this->physic.constants.defaultDt;
    }
    this->dt = dt;

    this->mergingFlag = flag;
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

    std::vector<int> toRemove;
    std::vector<Particule> newParticules;
    newParticules.reserve(getNumberParticules());
    Particule *ptrP1, *ptrP2;

    // perform all particules interactions
    // merge close particules
    if (particules.size() > 1) {

        for (int i=0; i<particules.size()-1; i++) {
            ptrP1 = &particules[i];

            for (int j=i+1; j<particules.size(); j++) {
                ptrP2 = &particules[j];

                if ((ptrP1->isDead) | (ptrP2->isDead)) {
                    continue;
                }

                if (physic.areNearby(*ptrP1, *ptrP2)) {
                    
                    // set particule to be dead
                    ptrP1->isDead = true;
                    ptrP2->isDead = true;

                    // remove non-charged particules
                    if (willBeValidMerge(*ptrP1, *ptrP2)) {
                        newParticules.push_back(mergeParticules(*ptrP1, *ptrP2));
                    }
                    continue;
                }

                physic.handelnParticulesInteraction(
                    *ptrP1,
                    *ptrP2
                );
            }
        }
    }

    // perfom all magnetics interactions
    for (int i=0; i<magneticFields.size(); i++) {
        for (int j=0; j<particules.size(); j++) {
            
            if (particules[j].isDead) {
                continue;
            }

            physic.handelnMagneticInteraction(
                particules[j],
                magneticFields[i]
            );
        }
    }

    // update state
    // reconstruct particules
    for (int i=particules.size()-1; i>-1; i--){
        
        if (particules[i].isDead) {
            continue;
        }
        
        if (!isInLimits(particules[i])) {
            continue;
        }

        particules[i].updateState(dt);

        newParticules.push_back(particules[i]);
    }

    particules.swap(newParticules);
}

bool System::isInLimits(Particule &p) const {
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

bool System::willBeValidMerge(Particule &p1, Particule &p2) {
    if (mergingFlag == FLAG_SUM_ONESIDE) {
        return true;
    }
    // in case of sum merge -> check that the sum is not 0
    return (p1.q + p2.q != 0);
}

Particule System::mergeParticules(Particule &p1, Particule &p2) {
    
    int q = 0;
    if (mergingFlag == FLAG_SUM) {
        q = p1.q + p2.q;
    } else if (mergingFlag == FLAG_SUM_ONESIDE) {
        if (sign(p1.q) != sign(p2.q)) {
            p2.q *= -1;
        }
        q = p1.q + p2.q;
    }
    
    return Particule(
        p1.pos,
        q,
        p1.m + p2.m
    );
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