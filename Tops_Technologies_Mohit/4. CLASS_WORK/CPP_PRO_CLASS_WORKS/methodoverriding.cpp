#include<iostream>
using namespace std;

class A
{
    public :
    	void show()
    	{
    		cout<<"\nShow from A. ";
		}
};
class B : public A
{
    public :
	    void show()
		{
			A::show();
			cout<<"\nShow from B. ";	
		}
};
		
class C : public B
{
    public :
	    void show()
		{
			B::show();
			cout<<"\nShow from C. ";
		}	
};

int main()
{  
    C obj;
    obj.show();
	return 0;
}