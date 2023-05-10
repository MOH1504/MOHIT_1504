#include<stdio.h>
#include<string.h>

int main()
{
    char str[100],rev_str[100];
    int i,j=0;
    printf("Enter a string : ");
    gets(str);
    i=0;
    while(str[i]!='\0')
    {
        i++;
    }
    i--;
    while(i>=0)
    {
        rev_str[j]=str[i];
        j++;
        i--;
    }
    rev_str[j]='\0';
    if(strcmp(str,rev_str)==0)
    {
        printf("Palindrome");
    }
    else
    {
        printf("Not Palindrome");
    }
    return 0;
}