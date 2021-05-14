# pragma once
# include <string>
# include <vector>

template<typename T>
class Vect2D {
    public:
        T x, y;
        
        Vect2D() {};

        Vect2D(T x, T y) {
            this->x = x;
            this->y = y;
        }

        Vect2D(std::vector<T> &vect) {
            this->x = vect[0];
            this->y = vect[1];
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

template<typename T>
int sign(const T &x) {
    return (x > 0) - (x < 0);
}