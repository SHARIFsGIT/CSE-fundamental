#include <stdio.h>
int main()
{
    int T;
    scanf("%d", &T);

    for (int i = 0; i < T; i++)
    {
        long long int M;
        int A, B, C;
        scanf("%lld %d %d %d", &M, &A, &B, &C);

        long long int product = A * B * C;
        if (M % product == 0)
        {
            printf("%d\n", M / product);
        }
        else
        {
            printf("-1\n");
        }
    }

    return 0;
}