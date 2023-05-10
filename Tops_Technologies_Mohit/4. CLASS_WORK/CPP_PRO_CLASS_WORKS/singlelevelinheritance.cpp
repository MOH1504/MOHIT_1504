#include<iostream>
using namespace std;

class A{
	public:
		int a;
		
		void getA(int x)
		{
			a = x;
		}
		
		void putA()
		{
			cout<<"\nA = "<<a;
		}
};

class B : public A{
	public:
		int b;
		
		void getB(int x)
		{
			b = x;
		}
		
		void putB()
		{
			cout<<"\nB = "<<b;
		}
};


int main()
{
	B obj2;
	int a,b;
	cout<<"Enter A & B : ";
	cin>>a>>b;
	obj2.getA(a);
	obj2.putA();
	obj2.getB(b);
	obj2.putB();
}















