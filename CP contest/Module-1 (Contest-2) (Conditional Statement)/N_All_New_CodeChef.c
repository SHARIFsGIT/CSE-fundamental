#include <stdio.h>
int main()
{
    int x, y;
    scanf("%d %d", &x, &y);

    if (x < y)
    {
        printf("OLD\n");
    }
    else if (x > y)
    {
        printf("NEW\n");
    }
    else
    {
        printf("SAME\n");
    }

    return 0;
}