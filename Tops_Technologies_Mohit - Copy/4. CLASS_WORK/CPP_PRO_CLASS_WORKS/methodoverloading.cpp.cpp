#include<iostream>
using namespace std;

int func1()
{
	return 10;
}

int func1(int a)
{
	if(a%2==0)
	{
		cout<<"\nEven No : ";
		return a;
	}
	else
	{
		cout<<"\nOdd no : ";
		return a;
	}
}

void func1(int n1,int n2)
{
	int add = n1+n2;
	cout<<"\nAddition : "<<add;
}

int main()
{
	cout<<func1();
	cout<<func1(11);
	func1(21,42);
	return 0;
}