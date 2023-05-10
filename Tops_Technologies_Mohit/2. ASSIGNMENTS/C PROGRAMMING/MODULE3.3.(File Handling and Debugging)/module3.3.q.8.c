#include<stdio.h>

struct employee
{
    int empNo;
    char empName[20];
    char address[50];
    int age;
};

int main()
{
    struct employee emp;
    
    printf("Enter employee number: ");
    scanf("%d", &emp.empNo);
    
    printf("Enter employee name: ");
    scanf("%s", emp.empName);
    
    printf("Enter employee address: ");
    scanf("%s", emp.address);
    
    printf("Enter employee age: ");
    scanf("%d", &emp.age);
    
    printf("\nEmployee No.: %d\nName: %s\nAddress: %s\nAge: %d\n", emp.empNo, emp.empName, emp.address, emp.age);
    
    return 0;
}