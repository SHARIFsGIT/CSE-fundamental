#include <stdio.h>
void function(int *pointer)
{
    printf("Value of function x: %d\n", *pointer);
    printf("Address of function x: %p\n", pointer);
    *pointer = 100;
}
int main()
{
    int x = 10;
    printf("Value of main x: %d\n", x);
    printf("Address of main x: %p\n", &x);
    function(&x);
    printf("New value of main x: %d\n", x);
    return 0;
}