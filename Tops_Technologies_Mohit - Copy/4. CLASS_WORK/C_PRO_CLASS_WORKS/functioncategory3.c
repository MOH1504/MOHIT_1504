#include<stdio.h>

int add(int n1,int n2)
{
	printf("\nA = %d",n1);
	printf("\nB = %d",n2);
	return n1+n2;
}

void main()
{
    int a = 23,b = 64;

	printf("\nAddition = %d",add(a,b));
}