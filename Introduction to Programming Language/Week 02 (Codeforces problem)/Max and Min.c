#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int A, B, C;
    scanf("%d %d %d", &A, &B, &C);

    int minimum = A;
    int maximum = A;

    if (B < minimum)
        minimum = B;
    else if (B > maximum)
        maximum = B;

    if (C < minimum)
        minimum = C;
    else if (C > maximum)
        maximum = C;

    printf("%d %d\n", minimum, maximum);

    return 0;
}

