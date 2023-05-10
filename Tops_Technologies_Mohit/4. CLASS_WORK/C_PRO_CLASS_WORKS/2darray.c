#include<stdio.h>

void main()
{
	
	int arr1[3][3],arr2[3][3];
	int i,j;
	
	printf("\n\n -----Array 1 : -----\n\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("Enter Index[%d][%d] : ",i,j);
			scanf("%d",&arr1[i][j]);
		}
		
	}
	 
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\nValue at Index[%d][%d] : %d",i,j,arr1[i][j]);			
		}
		
	}
	
	printf("\n\n -----Array 2 : -----\n\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("Enter Index[%d][%d] : ",i,j);
			scanf("%d",&arr2[i][j]);
		}
		
	}
	 
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\nValue at Index[%d][%d] : %d",i,j,arr2[i][j]);			
		}
		
	}
	
	
	printf("\n\n-------Addition of 2 Arrays --------------\n\n");
	
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("\nAddition [%d][%d] = %d",i,j,(arr1[i][j]+arr2[i][j]));
		}
	}
	
	
	
}






