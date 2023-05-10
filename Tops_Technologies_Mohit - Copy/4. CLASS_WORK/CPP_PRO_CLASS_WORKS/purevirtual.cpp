#include<iostream>
using namespace std;


class Sample1{
	public:
		void f1()
		{
			cout<<"\n Non Pure Virtual Function.";
		}
		
		virtual void f2();
};

class Sample2: public Sample1{
	public:
		void f2()
		{
			cout<<"\n Implemented Pure Virtual Function in Sample 2 Class.";
		}
};

int main()
{
	Sample2 s;
	s.f1();
	s.f2();
	return 0;
}