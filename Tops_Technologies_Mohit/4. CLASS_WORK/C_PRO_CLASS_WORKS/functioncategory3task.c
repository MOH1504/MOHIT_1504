#include<stdio.h>

int mul(int n1)
{
	printf("\nA = %d",n1);
	
	return n1*n1*n1;
}

void main()
{
    int a;
    printf("\nEnter A:");
    scanf("%d",&a);

	printf("\nCube of %d = %d",a,mul(a));
}