#include<stdio.h>

void main()
{
	int arr[5];
	int i;
	printf("\n\xB2\xB2\xB2\xB2\xB2\xB2 ENTER ARRAY1 \xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	
	for(i=0;i<5;i++)
	{
		printf("Enter Element[%d] : ",i+1);
		scanf("%d",&arr[i]);
	}
	
	for(i=0;i<5;i++)
	{
		printf("\nElement [%d] = %d",i+1,arr[i]);
	}
	
	
	
	
}