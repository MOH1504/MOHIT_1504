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

class C : public B{
	public:
		int c;
		
		void getC(int x)
		{
			c = x;
		}
		
		void putC()
		{
			cout<<"\nC = "<<c;
		}
};


int main()
{
	C obj2;
	int a,b,c;
	cout<<"Enter A , B , C : ";
	cin>>a>>b>>c;
	obj2.getA(a);
	obj2.getB(b);
	obj2.getC(c);
	
	obj2.putA();
	obj2.putB();
	obj2.putC();
}















