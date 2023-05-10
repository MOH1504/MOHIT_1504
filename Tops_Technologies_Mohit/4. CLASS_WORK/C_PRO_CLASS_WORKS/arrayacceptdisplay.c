#include<stdio.h>

void main()
{
	int marks[5];
	int i;
	
	for(i=0;i<5;i++)
	{
		printf("Enter Element %d :",i+1);
		scanf("%d",&marks[i]);
	}
	
	printf("\nDisplay Elements : \n\n");
	for(i=0;i<5;i++)
	{
		printf("%d\t",marks[i]);
	}
	
	
}