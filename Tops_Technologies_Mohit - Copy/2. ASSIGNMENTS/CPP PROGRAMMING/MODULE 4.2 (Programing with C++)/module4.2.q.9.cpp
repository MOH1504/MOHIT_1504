#include <iostream>

using namespace std;

class Matrix
{
    int m1[3], m2[3], m3[3];
public:
    void getMatrix()
    {
        cout << "Enter elements of 1st Matrix: ";
        for (int i = 0; i < 3; i++)
            cin >> m1[i];
        cout << "Enter elements of 2nd Matrix: ";
        for (int i = 0; i < 3; i++)
            cin >> m2[i];
    }
    void displayMatrix()
    {
        cout << "The Addition of two matrix is : ";
        for (int i = 0; i < 3; i++)
        {
            cout << m3[i] << " ";
        }
        cout << endl;
    }
    Matrix operator+(Matrix m)
    {
        Matrix temp;
        for (int i = 0; i < 3; i++)
        {
            temp.m3[i] = m1[i] + m2[i];
        }
        return temp;
    }
};

int main()
{
    Matrix m1, m2, m3;
    m1.getMatrix();
    m2.getMatrix();
    m3 = m1 + m2;
    m3.displayMatrix();
    return 0;
}