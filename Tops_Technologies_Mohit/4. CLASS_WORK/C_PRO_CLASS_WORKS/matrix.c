#include<stdio.h>

void main()
{
	int matrix1[3][3],matrix2[3][3];
	int i,j;
	
	printf("\n\n\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 Accept Matrix 1 \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("Enter Matrix1 [%d][%d] :",i,j);
			scanf("%d",&matrix1[i][j]);			
		}		
	}
	
	printf("\n\n\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 Accept Matrix 2 \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("Enter Matrix2 [%d][%d] :",i,j);
			scanf("%d",&matrix2[i][j]);			
		}		
	}
	
	
	printf("\n\n\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 Matrix 1 \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("%d\t",matrix1[i][j]);
		}
		printf("\n");
	}
	

	
	
	printf("\n\n\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 Matrix 2 \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("%d\t",matrix2[i][j]);
		}
		printf("\n");
	}
	
	
		printf("\n\n\xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2 Subtraction of Matrix 1 and MAtrix 2 \xB2\xB2\xB2\xB2\xB2\xB2\xB2\xB2\n\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("%d\t",(matrix1[i][j]-matrix2[i][j]));
		}
		printf("\n");
	}
	
	
	
	
	
	
	
}
