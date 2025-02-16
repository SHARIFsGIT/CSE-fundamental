#include <stdio.h>
int main()
{
    int t;
    scanf("%d", &t);

    while (t--)
    {
        int n;
        scanf("%d", &n);

        int index = 1;
        int quality = -1;

        for (int i = 1; i <= n; i++)
        {
            int a, b;
            scanf("%d %d", &a, &b);

            if (a > 10)
            {
                continue;
            }

            if (b > quality)
            {
                quality = b;
                index = i;
            }
        }
        printf("%d\n", index);
    }

    return 0;
}