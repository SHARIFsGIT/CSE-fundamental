#include <stdio.h>
int main()
{
    int t;
    scanf("%d", &t);

    while (t--)
    {
        int n, x;
        scanf("%d %d", &n, &x);

        int unrated = 2 * n - x;

        if (unrated >= x)
        {
            printf("0\n");
        }
        else
        {
            printf("%d\n", x - unrated);
        }
    }

    return 0;
}