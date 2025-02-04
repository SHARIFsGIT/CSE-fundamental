#include <stdio.h>
#include <math.h>

int main()
{
    double r1, r2, d1, d2;
    scanf("%lf %lf", &r1, &r2);
    scanf("%lf %lf", &d1, &d2);

    double dominater = r1 + d1;
    double everule = r2 + d2;

    if (dominater < everule)
    {
        printf("Everule\n");
    }
    else
    {
        printf("Dominater\n");
    }

    return 0;
}