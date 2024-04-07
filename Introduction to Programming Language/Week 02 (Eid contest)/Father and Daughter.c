#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int X;
    scanf("%d", &X);

    int daughter = X / 5;
    int father = daughter * 4;

    printf("%d %d", father, daughter);

    return 0;
}
