#include <stdio.h>
void function(int x)
{
    printf("Address of function x: %p\n", &x);
    printf("Value of function x: %d\n", x);
    x = 100;
    printf("New value of function x: %d\n", x);
}
int main()
{
    int x = 10;
    printf("Address of main x: %p\n", &x);
    printf("Value of main x: %d\n", x);
    function(x); // vlaue goes only not the variable
    printf("New value of main x: %d\n", x);
    return 0;
}