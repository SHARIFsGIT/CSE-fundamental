#include <stdio.h>
int main()
{
    int ary[4] = {1, 2, 3, 4};
    int *p;

    p = ary + 3;
    printf("Address of ary[3]: %p\n", p);

    *p = 5;
    printf("%d\n", ary[3]);
}