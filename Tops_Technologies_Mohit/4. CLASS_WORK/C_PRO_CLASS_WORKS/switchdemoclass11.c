#include<stdio.h>

void main()
{
	char c;
	printf("\nEnter a Character : ");
	scanf("%c",&c);
	switch(c)
	{
		case 'a':	
		case 'e':	
		case 'i':
		case 'o':
		case 'u':
		case 'A':
		case 'E':
		case 'I':
		case 'O':
		case 'U':printf("%c is vowel",c);
				 break;
		default : printf("%c is Consonant",c);
				 break;		
	}	

}