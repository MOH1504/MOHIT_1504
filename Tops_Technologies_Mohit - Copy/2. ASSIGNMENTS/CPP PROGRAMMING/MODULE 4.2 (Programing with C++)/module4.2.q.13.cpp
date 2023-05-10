#include <iostream>
using namespace std;

class MaxNumber
{
    int x, y;

public:
    void getNumber(int a, int b)
    {
        x = a;
        y = b;
    }
    friend int compareNumber(MaxNumber);
};

int compareNumber(MaxNumber m)
{
    if (m.x > m.y)
        return m.x;
    else
        return m.y;
}

int main()
{
    MaxNumber m;
    int x, y;
    cout << "Enter two numbers: ";
    cin >> x >> y;
    m.getNumber(x, y);
    int max = compareNumber(m);
    cout << "Maximum number is: " << max;
    return 0;
}