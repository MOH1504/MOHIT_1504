#include<iostream>
using namespace std;

int Function1(int a, int b)
{
	return a+b;
}

int main()
{
    int n,e;
	cout<<"Enter No.";	
	cin>>n>>e;
	cout<<Function1(n,e);
	
	return 0;
}