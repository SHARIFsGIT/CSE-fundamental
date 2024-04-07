#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int D, Q, R;
    scanf("%d %d %d", &D, &Q, &R);

    int divisor = (D - R) / Q;
    printf("%d", divisor);

    return 0;
}
