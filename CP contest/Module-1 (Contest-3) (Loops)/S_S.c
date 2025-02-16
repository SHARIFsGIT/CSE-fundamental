#include <stdio.h>
int main()
{
    int t;
    scanf("%d", &t);

    while (t--)
    {
        int n;
        scanf("%d", &n);

        int count = 0;

        int m = n;
        while (m > 0)
        {
            int lastDigit = m % 10;
            m /= 10;

            if (lastDigit > 0)
            {
                count++;
            }
        }
        printf("%d\n", count);

        int power = 1;
        while (n > 0)
        {
            int lastDigit = n % 10;
            n /= 10;

            if (lastDigit != 0)
            {
                printf("%d ", lastDigit * power);
            }
            power *= 10;
        }
        printf("\n");
    }

    return 0;
}