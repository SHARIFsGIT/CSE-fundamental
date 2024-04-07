#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int x;
    scanf("%d", &x);

    if (x%3 == 0)
    {
        printf("%d", x/3);
    }
    else
    {
        printf("%d", x/3 + 1);
    }
    return 0;
}
