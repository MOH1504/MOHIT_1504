#include<stdio.h>

int main()

{
	int choice=0;
	int pizza_price =180;
	int burger_price = 100;
	int dosa_price =120;
	int idli_price =50;
	printf("MENU\n");
	printf("1. PIZZA   price=180/pcs\n"); 
		printf("2. BURGER   price=100/pcs\n"); 
			printf("3. DOSA   price=120/pcs\n"); 
				printf("4. IDLI   price=50/pcs\n\n"); 
				printf("Please enter yourchoice:\n");
				scanf("%d",&choice);
				while(1)
				if(choice==1)
				{
					printf("You have selected pizza:\n");
					int quality=0;
					printf("Please enter quality:");
					scanf("%d",&quality);
					int amount=quality * pizza_price;
					printf("Total amount:\n");
					 printf("\n\nDo You want to place more order ? y/n : ");
				}
				else if(choice==2)
				{
					printf("You have selected burger\n:");
					int quality=0;
					printf("Please enter quality:");
					scanf("%d",&quality);
					int amount=quality * burger_price;
						printf("Total amount:%d\n",amount);
						 printf("\n\nDo You want to place more order ? y/n : ");
				}
				else if(choice==3)
				{
					printf("You have selected dosa:\n");
					int quality=0;
					printf("Please enter quality:\n");
					scanf("%d",&quality);
					int amount=quality * dosa_price;
						printf("Total amount:%d\n",amount);
						 printf("\n\nDo You want to place more order ? y/n : ");
				}
				else if(choice==4)
				{
					printf("You have selected idli:");
					int quality=0;
					printf("Please enter quality:\n");
					scanf("%d",&quality);
					int amount=quality * idli_price;
						printf("Total amount:%d\n",amount);
						 printf("\n\nDo You want to place more order ? y/n : ");
				}
				
				return 0;
}
