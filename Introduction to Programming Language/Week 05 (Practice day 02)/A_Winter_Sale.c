#include <stdio.h>
int main()
{
    int X, P;
    scanf("%d %d", &X, &P);

    float output = (-P * 100.00) / (X - 100.00);
    printf("%0.2f\n", output);
    return 0;
}