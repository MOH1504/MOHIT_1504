#include<stdio.h>

void main()
{
	int i,j,t;
	
	for(i=2;i<=7;i++)
	{
		printf("\n Table of %d\n",i);
		for(j=1;j<=10;j++)
		{
			t = i*j;
			printf("%d * %d = %d\n",i,j,t);
		}
        printf("\n");
	}
	
}