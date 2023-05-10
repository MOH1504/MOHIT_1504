#include<iostream>
using namespace std;

void add()
{
	int a = 5, b = 10;
	cout<<"\nAddition : "<<(a+b);	
}

void sub()
{
	int a = 5, b = 10;
	cout<<"\nSubtraction : "<<(a-b);	
}

void mul()
{
	int a = 5, b = 10;
	cout<<"\nMultiplication : "<<(a*b);	
}

void div()
{
	int a = 5, b = 10;
	cout<<"\ndivision : "<<((float)a/b);	
}


int main()

{	
    int a,b,choice;
    cout<<"\n\nPress 1.Addition\nPress 2.Subtraction\nPress 3.Multiplication\nPress 4.Division";
	cout<<"\nEnter your choice?";
	cin>>choice;
		
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
	    default:cout<<"\nInvalid Choice.";
			   break;	   
    }
    
    return 0;
		
}


	