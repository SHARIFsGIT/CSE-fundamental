#include <stdio.h>
int main()
{
    int x = 10;
    printf("%p\n", &x);

    int *pointer = &x;
    printf("%p\n", pointer);

    // dereference
    printf("%d\n", *pointer);

    // pointer = 500;
    // printf("%d\n", x);

    // dereference
    *pointer = 500;
    printf("%d\n", x);
    printf("%p\n", pointer);
    return 0;
}