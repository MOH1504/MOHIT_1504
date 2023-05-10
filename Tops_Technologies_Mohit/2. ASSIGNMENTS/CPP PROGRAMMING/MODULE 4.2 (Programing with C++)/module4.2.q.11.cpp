#include <iostream>
#include <cmath>
using namespace std;
 
double area(double a)
{ 
    return 3.14 * a * a; 
}
 
double area(double a, double b)
{
    return a * b;
}
 
double area(double a, double b, double c)
{
    double s = (a + b + c) / 2;
    return sqrt(s * (s - a) * (s - b) * (s - c));
}
 
int main()
{
    double a, b, c;
    cout << "Enter the parameters of rectangle: ";
    cin >> a >> b;
    cout << "Area of rectangle is: " << area(a, b) << endl;
    cout << "Enter the parameters of triangle: ";
    cin >> a >> b >> c;
    cout << "Area of triangle is: " << area(a, b, c) << endl;
    cout << "Enter the radius of circle: ";
    cin >> a;
    cout << "Area of circle is: " << area(a) << endl;
    return 0;
}