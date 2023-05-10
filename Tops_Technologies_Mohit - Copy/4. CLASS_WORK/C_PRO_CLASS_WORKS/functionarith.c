#include<stdio.h>
void add()
{
	int a = 5,b =8;
	printf("\nAddition : %d",(a+b));	
}


void sub()
{
	int a = 5,b =8;
	printf("\nSubtraction : %d",(a-b));	
}


void mul()
{
	int a = 5,b =8;
	printf("\nMultiplication : %d",(a*b));	
}



void div()
{
	int a = 5,b =8;
	printf("\nDivision : %.2f",((float)a/b));	
}

void main()
{	
	add();
	sub();
	mul();
	div();	
}








