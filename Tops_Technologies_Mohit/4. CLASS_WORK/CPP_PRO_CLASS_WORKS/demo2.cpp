#include<iostream>
using namespace std;

int main()
{
	int a,b;
	
	cout<<"\n Enter A & B : ";
	cin>>a>>b;
		
	cout<<"\nA = "<<a<<"\tB = "<<b;
	
	cout<<"\nAdd : "<<(a+b);
	cout<<"\nSub : "<<(a-b);
	cout<<"\nMul : "<<(a*b);
	cout<<"\nDiv : "<<((float)a/b);
	
	return 0;
}