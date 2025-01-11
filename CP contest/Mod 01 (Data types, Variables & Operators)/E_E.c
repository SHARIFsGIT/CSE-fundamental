#include <stdio.h>
int main()
{
    int a, b;
    scanf("%d %d", &a, &b);

    int d = a / b;
    int r = a - (d * b);
    double f = (double)a / b;

    printf("%d %d %.5lf", d, r, f);

    return 0;
}