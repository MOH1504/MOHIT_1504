#include <stdio.h>

int main()
{
    int num = -1562;
    int max = num % 10;
    num /= 10;
    
    while (num > 0) {
        int digit = num % 10;
        if (digit > max)
            max = digit;
        num /= 10;
    }
    
    printf("Max number is %d\n", max);
    
    return 0;
}