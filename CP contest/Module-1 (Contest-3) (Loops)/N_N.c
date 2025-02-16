#include <stdio.h>
int main()
{
    int t;
    scanf("%d", &t);

    while (t--)
    {
        int x, n;
        scanf("%d %d", &x, &n);

        int totalSeat = x * 100;
        int remainingPerson = n - totalSeat;

        if (totalSeat >= n)
        {
            printf("0\n");
        }
        else
        {
            if (remainingPerson % 100 != 0)
            {
                printf("%d\n", (remainingPerson / 100) + 1);
            }
            else
            {
                printf("%d\n", (remainingPerson / 100));
            }
        }
    }

    return 0;
}