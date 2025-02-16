#include <stdio.h>
#include <math.h>
int main()
{
    int t;
    scanf("%d", &t);

    while (t--)
    {
        int x;
        scanf("%d", &x);

        double commission = x * 0.2;

        int minimumInsurance = ceil(100 / commission);

        printf("%d\n", minimumInsurance);
    }

    return 0;
}