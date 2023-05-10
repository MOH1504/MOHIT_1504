#include<stdio.h>

void main()
{
	int arr1[5],arr2[5];
	int i;
	printf("\n\xB2\xB2\xB2\xB2\xB2\xB2 ENTER ARRAY1 \xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	
	for(i=0;i<5;i++)
	{
		printf("Enter Element[%d] : ",i+1);
		scanf("%d",&arr1[i]);
	}
	
	for(i=0;i<5;i++)
	{
		printf("\nElement [%d] = %d",i+1,arr1[i]);
	}
	
	printf("\n\n\n\xB2\xB2\xB2\xB2\xB2\xB2 ENTER ARRAY2 \xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	
	for(i=0;i<5;i++)
	{
		printf("Enter Element[%d] : ",i+1);
		scanf("%d",&arr2[i]);
	}
	
	for(i=0;i<5;i++)
	{
		printf("\nElement [%d] = %d",i+1,arr2[i]);
	}
	
	printf("\n\n\n\xB2\xB2\xB2\xB2\xB2\xB2 ARRAY ADDITION \xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	
	for(i=0;i<5;i++)
	{
		printf("\nElement [%d] = %d",i+1,arr1[i]+arr2[i]);
    }
	
}