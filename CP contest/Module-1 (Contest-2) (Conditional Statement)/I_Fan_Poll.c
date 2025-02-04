#include <stdio.h>
int main()
{
    double a, b, c;
    scanf("%lf %lf %lf", &a, &b, &c);

    if (a > b && a > c)
    {
        printf("Yes\n");
    }
    else
    {
        printf("No\n");
    }

    return 0;
}