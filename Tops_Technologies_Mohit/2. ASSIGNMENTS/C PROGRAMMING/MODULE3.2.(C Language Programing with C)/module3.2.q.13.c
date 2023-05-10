#include <stdio.h>

int main()
{
    int num, firstDigit, lastDigit, sum;
    
    printf("Enter a number: ");
    scanf("%d", &num);
    
    // Find the first digit
    firstDigit = num;
    while(firstDigit >= 10)
    {
        firstDigit = firstDigit / 10;
    }
    
    // Find the last digit
    lastDigit = num % 10;
    
    // Calculate the sum
    sum = firstDigit + lastDigit;
    
    printf("Sum of first and last digit of %d is: %d\n", num, sum);
    
    return 0;
}