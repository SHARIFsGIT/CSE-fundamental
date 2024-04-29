#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int main()
{
    double x;
    scanf("%lf", &x);

    int ceil_ans = ceil(x);
    printf("%d\n", ceil_ans);

    int floor_ans = floor(x);
    printf("%d\n", floor_ans);

    int round_ans = round(x);
    printf("%d\n", round_ans);

    double sqrt_ans = sqrt(x);
    printf("%0.3lf\n", sqrt_ans);

    double pow_ans = pow(x, x);
    printf("%0.2lf\n", pow_ans);

    int abs_ans = abs(x);
    printf("%d\n", abs_ans);
    return 0;
}