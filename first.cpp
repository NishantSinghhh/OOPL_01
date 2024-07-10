#include <iostream>
#include <cmath> // For std::sqrt, std::atan2

using namespace std;

class Complex {
private:
    double real;
    double img;

public:
    Complex() : real(0.0), img(0.0) {}
    Complex(double r, double i) : real(r), img(i) {}

    Complex operator+(const Complex& other) const {
        return Complex(real + other.real, img + other.img);
    }

    Complex operator-(const Complex& other) const {
        return Complex(real - other.real, img - other.img);
    }

    Complex operator*(const Complex& other) const {
        return Complex(real * other.real - img * other.img,
                       real * other.img + img * other.real);
    }

    Complex operator/(const Complex& other) const {
        double denominator = other.real * other.real + other.img * other.img;
        if (denominator == 0) {
            throw invalid_argument("Division by zero");
        }
        return Complex((real * other.real + img * other.img) / denominator,
                       (img * other.real - real * other.img) / denominator);
    }
    
    // Absolute value (magnitude) of the complex number
    double abs() const {
        return sqrt(real * real + img * img);
    }
    
    // Conjugate of the complex number
    Complex conjugate() const {
        return Complex(real, -img);
    }
    
    // Sin function for complex number
    Complex sin() const {
        return Complex(std::sin(real) * std::cosh(img), std::cos(real) * std::sinh(img));
    }

    // Cos function for complex number
    Complex cos() const {
        return Complex(std::cos(real) * std::cosh(img), -std::sin(real) * std::sinh(img));
    }

    // Tan function for complex number
    Complex tan() const {
        return sin() / cos();
    }

    // Output operator
    friend ostream& operator<<(ostream& out, const Complex& c) {
        out << c.real << " + " << c.img << "i";
        return out;
    }

    // Input operator
    friend istream& operator>>(istream& in, Complex& c) {
        cout << "Enter real part: ";
        in >> c.real;
        cout << "Enter imaginary part: ";
        in >> c.img;
        return in;
    }
};

int main() {
    Complex C1, C2, result;
    int choice;

    do {
        cout << "Enter Real and Imaginary part of Complex Number 1:\n";
        cin >> C1;
        cout << "Enter Real and Imaginary part of Complex Number 2:\n";
        cin >> C2;

        cout << "********** MENU **********" << endl;
        cout << "1. Addition" << endl;
        cout << "2. Subtraction" << endl;
        cout << "3. Multiplication" << endl;
        cout << "4. Division" << endl;
        cout << "5. Absolute Value" << endl;
        cout << "6. Conjugate" << endl;
        cout << "7. Sin" << endl;
        cout << "8. Cos" << endl;
        cout << "9. Tan" << endl;
        cout << "10. Exit" << endl;

        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                result = C1 + C2;
                cout << "Result of Addition: " << result << endl;
                break;
            case 2:
                result = C1 - C2;
                cout << "Result of Subtraction: " << result << endl;
                break;
            case 3:
                result = C1 * C2;
                cout << "Result of Multiplication: " << result << endl;
                break;
            case 4:
                try {
                    result = C1 / C2;
                    cout << "Result of Division: " << result << endl;
                } catch (const std::invalid_argument& e) {
                    cout << "Error: " << e.what() << endl;
                }
                break;
            case 5:
                cout << "Absolute Value of Complex Number 1: " << C1.abs() << endl;
                cout << "Absolute Value of Complex Number 2: " << C2.abs() << endl;
                break;
            case 6:
                cout << "Conjugate of Complex Number 1: " << C1.conjugate() << endl;
                cout << "Conjugate of Complex Number 2: " << C2.conjugate() << endl;
                break;
            case 7:
                cout << "Sine of Complex Number 1: " << C1.sin() << endl;
                cout << "Sine of Complex Number 2: " << C2.sin() << endl;
                break;
            case 8:
                cout << "Cosine of Complex Number 1: " << C1.cos() << endl;
                cout << "Cosine of Complex Number 2: " << C2.cos() << endl;
                break;
            case 9:
                cout << "Tangent of Complex Number 1: " << C1.tan() << endl;
                cout << "Tangent of Complex Number 2: " << C2.tan() << endl;
                break;
            case 10:
                cout << "Exiting the program. Thank you!\n";
                break;
            default:
                cout << "Invalid choice! Please enter a number between 1 and 10.\n";
        }

        cout << "------------------------\n";
    } while (choice != 10);

    return 0;
}
