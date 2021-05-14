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
        std::vector<MagneticField> magneticFields;
        int FLAG_SUM = 0;
        int FLAG_SUM_ONESIDE = 1;

        System(std::vector<Particule> &particules, float dt=-1, int flag = 0);

        void setLimits(float minX, float maxX, float minY, float maxY);
        const Constants& constants() const { return physic.constants; }
        int getNumberParticules() const { return particules.size(); };

        void updateState(float dt=-1);

        void clearElements();
        void addParticule(Particule &particule);
        void addMagneticField(MagneticField &magneticField);

        void print();
        
        private:
            bool isLimits = false;
            int mergingFlag;
            float dt, minX, maxX, minY, maxY;

            bool isInLimits(Particule &particule) const;
            bool willBeValidMerge(Particule &p1, Particule &p2);
            Particule mergeParticules(Particule &p1, Particule &p2);
};