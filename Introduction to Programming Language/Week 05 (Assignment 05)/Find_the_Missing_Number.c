#include <stdio.h>
int main()
{
    int test;
    scanf("%d", &test);

    for (int i = 0; i < test; i++)
    {
        long long int M, A, B, C;

        scanf("%lld %lld %lld %lld", &M, &A, &B, &C);

        long long int product = A * B * C;

        if (A == 0 || B == 0 || C == 0 || M % product != 0)
        {
            printf("-1\n");
        }
        else
        {
            printf("%lld\n", M / product);
        }
    }

    return 0;
}