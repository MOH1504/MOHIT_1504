#include<stdio.h>

void main()
{
	int n,i,t;
	
	printf("\n Enter Number : ");
	scanf("%d",&n);
	
	for(i=1;i<=10;i++)
	{
		t = n * i;
		printf("%d * %d = %d\n",n,i,t);
		
	}

}
