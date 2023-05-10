#include<stdio.h>

void main()
{
	int a,b,c;
	printf("\n Enter 3 Values : ");
	scanf("%d%d%d" ,&a,&b,&c);
	printf("\nA= %d, B=%d, C=%d",a,b,c);
	
	
if(a>b)
{
		if(a>c)
		
		{
		printf("\n%d is Greater",a);
	    }
	    
	    else
        {
		printf("\n is Greater",c);
        }
}

else
{
	    if(b>c)
	    {
	    	printf("\n%d is Greater",b);
	    }
	    
	    else
	    {
	    	printf("\n%d is Greater",c);
	   	}
}
    
}