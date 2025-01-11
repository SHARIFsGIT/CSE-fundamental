#include <stdio.h>
int main()
{
    double r;
    scanf("%lf", &r);

    double PI = 3.14159265358979323846;
    double area = PI * r * r;
    double circumference = 2 * PI * r;

    printf("%.6lf %.6lf", area, circumference);

    return 0;
}