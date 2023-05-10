#include<stdio.h>

int add()
{
	int n1=32,n2=45;
	return n1+n2;
}

int sub()
{
	int n1=32,n2=45;
	return n1-n2;
}

void main()
{
	printf("\nAddition = %d",add());
	printf("\nSubtraction = %d",sub());
}