#include <stdio.h>
int main()
{
    int t;
    scanf("%d", &t);

    while (t--)
    {
        int x, y;
        scanf("%d %d", &x, &y);

        int requiredPlates = 20 * y;

        if (requiredPlates <= x)
        {
            printf("20\n");
        }
        else
        {
            printf("%d\n", x / y);
        }
    }

    return 0;
}