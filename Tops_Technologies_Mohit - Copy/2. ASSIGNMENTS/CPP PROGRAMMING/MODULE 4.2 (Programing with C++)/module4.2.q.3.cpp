#include<iostream>
using namespace std;

//Inline Function
inline int mul(int x, int y)
{
    return x*y;
}

inline int cube(int x)
{
    return x*x*x;
}

int main()
{
    int a, b;
    cout<<"Enter two numbers : ";
    cin>>a>>b;
    cout<<"Multiplication : "<<mul(a,b)<<endl;
    cout<<"Cube of "<<a<<" : "<<cube(a)<<endl;
    return 0;
}