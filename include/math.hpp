# pragma once
# include <string>

template<typename T>
class Vect2D {
    public:
        T x, y;
        
        Vect2D() {};

        Vect2D(T x, T y) {
            this->x = x;
            this->y = y;
        }

        double length() const {
            return sqrt(x*x + y*y);
        }

        Vect2D<T> operator+(const Vect2D<T> &vect) const {
            return Vect2D<T>(
                this->x + vect.x,
                this->y + vect.y
            );
        }
        Vect2D<T> operator-(const Vect2D<T> &vect) const {
            return Vect2D<T>(
                this->x - vect.x,
                this->y - vect.y
            );
        }
        Vect2D<T> operator*(T number) const {
            return Vect2D<T>(
                this->x * number,
                this->y * number
            );
        }
        Vect2D<T> operator/(T number) const {
            return Vect2D<T>(
                this->x / number,
                this->y / number
            );
        }

        Vect2D<T> normalize() {
            double length = this->length();
            return Vect2D<T>(
                this->x / length,
                this->y / length
            );
        }
};