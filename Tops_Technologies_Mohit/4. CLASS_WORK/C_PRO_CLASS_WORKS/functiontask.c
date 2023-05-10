#include<stdio.h>

void add()
{
	int a = 5, b = 10;
	printf("\nAddition : %d",(a+b));	
}

void sub()
{
	int a = 5, b = 10;
	printf("\nSubtraction : %d",(a-b));	
}

void mul()
{
	int a = 5, b = 10;
	printf("\nMultiplication : %d",(a*b));	
}

void div()
{
	int a = 5, b = 10;
	printf("\nDivision : %.2f",((float)a/b));	
}


void main()

{	
    int a,b,choice;
    printf("\n\nPress 1.Addition\nPress 2.Subtraction\nPress 3.Multiplication\nPress 4.Division");
	printf("\nEnter your choice?");
	scanf("%d",&choice);
	
	switch(choice)
    {
    	case 1:add();
               break;
        case 2:sub();
	           break;	
	    case 3:mul();
		       break;
	    case 4:div();
			   break;
	    default:printf("\nInvalid Choice.");
			   break;	   
    }
		
}


	