#include<stdio.h>
void function1();
void function2();
void function3();
void main()
{
	function1();
	function2();
    function3();
	
}




	void function1()
{
	
	int leanth,width;
	printf("*********area of rectangle**********");
	
	printf("\nenter the leanth =");
	scanf("%d",&leanth);
	printf("\n enter the width=");
	scanf("%d",&width);
	
	printf("area of rectangle is =%d",(leanth*width));	
	
}
    void function2()
    {
    	float base,hight;
    	
    	printf("\n\n********area of triangle********");
    	
    	printf("\nenter the base=");
    	scanf("%f",&base);
    	
    	printf("\nnenter the hight=");
    	scanf("%f",&hight);
    	
    	printf("the area of triangle is =%f",0.5*base*hight);
    	
    }
    
    void function3()
	{
		
		float radius;
		
		printf("\n\n********area of circle*********");
		
		printf("\nenter the radius is =");
		scanf("%f",&radius);
		
		printf("\narea of circle is=%f",3.14*radius*radius);
		}	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
    	
	