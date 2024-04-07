#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int N;
    scanf("%d", &N);

    int start = (N / 5) - 4;

    for (int i = 0; i < 5; i++)
        printf("%d ", start + 2 * i);

    return 0;
}

