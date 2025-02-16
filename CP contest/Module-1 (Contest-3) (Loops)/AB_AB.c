#include <stdio.h>
int main()
{
    int n, k, m;
    scanf("%d %d %d", &n, &k, &m);

    int score = 0;

    for (int i = 0; i < n - 1; i++)
    {
        int a;
        scanf("%d", &a);

        score += a;
    }

    int required = (m * n) - score;

    if (required <= 0)
    {
        printf("0\n");
    }
    else if (required > k)
    {
        printf("-1\n");
    }
    else
    {
        printf("%d\n", required);
    }

    return 0;
}