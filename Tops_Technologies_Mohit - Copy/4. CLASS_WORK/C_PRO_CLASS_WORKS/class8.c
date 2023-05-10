#include<stdio.h>

void main()
{
	int a,b;
	printf("\nEnter A: ");
	scanf("%d",&a);
	printf("\nEnter B: ");
	scanf("%d",&b);
	printf("\nA = %d, B = %d",a,b);
	
	if(a > b)
	{
		printf("\n%d is Greater",a);
	}
	else
	{
		printf("\n%d is Greater",b);
	}
	
}