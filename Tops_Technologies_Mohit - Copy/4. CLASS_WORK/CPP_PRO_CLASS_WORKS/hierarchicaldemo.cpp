#include<iostream>
using namespace std;

class Side{
    protected: 
	int l;
	
    public:
	void getSide(int s)
	{
		l = s;
	}
};

class Square:public Side{ 
    public:
    int sq()
	{
		return l*l;
	}	
};

class Cube:public Side{
    public:
	int cu()
	{
		return l*l*l;
    } 	
};

int main()
{   
    Square obj1;
    obj1.getSide(5);
    cout<<"\n Square Of 5 is : "<<obj1.sq();
    
    Cube obj2;
    obj2.getSide(5);
    cout<<"\n Cube Of 5 is : "<<obj2.cu();
    
	return 0;
}