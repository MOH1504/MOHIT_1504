#include<stdio.h>

void main()
{
	
	int age;
	char name[10];
	float salary;
	
	printf("\n**** Accepting Employee Details****");
	
	printf("\n Enter Your Name : ");
	scanf("%s",&name);
	printf("\n Enter Age : ");
	scanf("%d",&age);
	printf("\n Enter Your Salary : ");
	scanf("%f",&salary);
	
	
	
    printf("\n****Display Employee Details****");
    printf("\nName : %s",name);
    printf("\nAge : %d",age);
    printf("\nSalary : %f",salary);
    
	
	
}