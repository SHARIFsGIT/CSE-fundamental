#include <stdio.h>
int main()
{
    int t;
    scanf("%d", &t);

    while (t--)
    {
        int n, k;
        scanf("%d %d", &n, &k);

        int oddNumber = n - (k - 1);
        int evenNumber = n - 2 * (k - 1);

        if (oddNumber >= 1 && oddNumber % 2 != 0)
        {
            printf("YES\n");
            for (int i = 0; i < k - 1; i++)
            {
                printf("1 ");
            }
            printf("%d\n", oddNumber);
        }
        else if (evenNumber >= 1 && evenNumber % 2 == 0)
        {
            printf("YES\n");
            for (int i = 0; i < k - 1; i++)
            {
                printf("2 ");
            }
            printf("%d\n", evenNumber);
        }
        else
        {
            printf("NO\n");
        }
    }
    return 0;
}