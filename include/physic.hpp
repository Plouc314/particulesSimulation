# pragma once
# include <iostream>
# include <math.h>
# include "partcule.hpp"
# include "math.hpp"

class Particule;

class Constants {
    public:
        double pi = 3.14159265358;
        double masseProton = 1.6726e-27;
        double masseNeutron = 1.6749e-27;
        double masseElectron = 9.1094e-31;
        double chargeProton = 1.602e-19;
        double chargeElectron = -1.602e-19;
        float defaultDt = 0.1;

        Constants() {};

        double getK() const { return this->_k; };
        void setK(double k) {
            this->_k = k;
            this->_e = 1/(4 * this->pi * this->_k);
        };

        double getE() const { return this->_e; };
        void setE(double e) {this->_e = e; };

    private:
        double _e = 8.85e-12;
        double _k = 1/(4 * this->pi * this->_e);
};

class MagneticField{
    public:
        Vect2D<float> origin;
        float intensity, dispersion;
        bool isUniform;

        MagneticField(float x, float y, float intensity, float dispersion = -1, bool isUniform = true);
        MagneticField(Vect2D<float> origin, float intensity, float dispersion = -1, bool isUniform = true);

        std::vector<float> getListOrigin() const { return {origin.x, origin.y}; }

        float getIntensity(const Vect2D<float> &coordinate) const;
    private:
        float defaultDispersion = 20;
};

class Physics {
    public:
        Constants constants;

        Physics();

        Vect2D<float> getParticulesAttraction(const Particule &p1, const Particule &p2) const;
        void handelnParticulesInteraction(Particule &p1, Particule &p2) const;
        void handelnMagneticInteraction(Particule &p, MagneticField &m) const;
};


