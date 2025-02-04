#include <stdio.h>
int main()
{
    double max_w, min_h;
    scanf("%lf %lf", &max_w, &min_h);

    int chef_w = 60;
    int chef_h = 130;

    if (max_w >= chef_w && min_h <= chef_h)
    {
        printf("YES\n");
    }
    else
    {
        printf("NO\n");
    }

    return 0;
}