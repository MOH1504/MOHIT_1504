#include <stdio.h>
#include <string.h>

int main()
{
    int i, length;
    int flag = 0;
    char string[100], reverse[100];

    printf("Enter a string: ");
    scanf("%s", string);

    length = strlen(string);

    for (i = length - 1; i >= 0; i--)
    {
        reverse[length - i - 1] = string[i];
    }
    reverse[length] = '\0';

    printf("Reverse of the string: %s\n", reverse);

    for (i = 0; i < length; i++)
    {
        if (string[i] != reverse[i])
            flag = 1;
    }

    if (flag == 1)
        printf("%s is not a palindrome\n", string);
    else
        printf("%s is a palindrome\n", string);

    return 0;
}