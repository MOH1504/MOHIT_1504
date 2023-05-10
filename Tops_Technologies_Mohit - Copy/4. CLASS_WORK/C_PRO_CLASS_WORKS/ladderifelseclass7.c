#include<stdio.h>

void main()
{
	int roll_no,s1,s2,s3,total;
	char name[10];
	float per;
	char c='%';
	
	printf("\n***********Student Information*************\n");
	printf("\nEnter Roll No : ");
	scanf("%d",&roll_no);
	printf("Enter Name : ");
	scanf("%s",&name);
	printf("Enter Physics Marks : ");
	scanf("%d",&s1);
	printf("Enter Chemistry Marks : ");
	scanf("%d",&s2);
	printf("Enter Maths Marks : ");
	scanf("%d",&s3);
	total = s1+s2+s3;
	per = (float)total/3;
	printf("\nTotal Marks : %d",total);
	printf("\nPercentage : %.2f%c",per,c);
	
	if(per>=75)
	{
		printf("\nDistinction");
	}
	else if(per>=60)
	{
		printf("\nFirst Class");
	}
	else if(per>=50)
	{
		printf("\nSecond Class");		
	}
	else if(per>=40)
	{
		printf("\nPass Class");
	}
	else
	{
		printf("\nFail");
	}
	
}








