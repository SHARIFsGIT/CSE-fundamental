#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int X, Y;
    scanf("%d %d", &X, &Y);

    int rita = (X - Y) / 2;
    int mina = rita + Y;

    printf("%d %d", mina, rita);

    return 0;
}
