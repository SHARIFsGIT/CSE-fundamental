#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int N;
    scanf("%d", &N);
    printf("%d%d%d%d", N%10, (N/10)%10, (N/100)%10, (N/1000)%10);

    return 0;
}

