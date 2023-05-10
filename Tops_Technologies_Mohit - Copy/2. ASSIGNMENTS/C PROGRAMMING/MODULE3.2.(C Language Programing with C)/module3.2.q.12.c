#include <stdio.h>

int main()
{
    int num = 1523;
    int sum = 0;

    while(num > 0)
    {
        sum += num % 10;
        num /= 10;
    }
    
    printf("Sum of given number: %d\n", -sum);
    return 0;
}