#include<stdio.h>
void  func1();
void func2();


void main()
{
	func2();
	func1();
}

void  func1()
{
	printf("\n Function1 Called");
    func2();
}

void func2()
{
	printf("\n Function2 Called");
	func1();
}