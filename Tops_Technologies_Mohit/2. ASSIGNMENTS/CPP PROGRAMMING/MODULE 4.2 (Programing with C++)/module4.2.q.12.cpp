#include <iostream>
using namespace std;

class Swap
{
    int x, y;

public:
    void getData(int a, int b)
    {
        x = a;
        y = b;
    }
    friend void swap(Swap &s);
    void display()
    {
        cout << "x = " << x << endl
             << "y = " << y;
    }
};

void swap(Swap &s)
{
    s.x = s.x + s.y;
    s.y = s.x - s.y;
    s.x = s.x - s.y;
}

int main()
{
    Swap s;
    s.getData(2, 3);
    cout << "Before Swapping: " << endl;
    s.display();
    swap(s);
    cout << "\nAfter Swapping: " << endl;
    s.display();
    return 0;
}