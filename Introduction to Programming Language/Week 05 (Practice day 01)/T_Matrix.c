#include <stdio.h>
#include <stdlib.h>
int main()
{
    int N;
    scanf("%d", &N);

    int array[N][N];
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            scanf("%d", &array[i][j]);
        }
    }

    int sum_primary = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if ((i == j))
            {
                sum_primary += array[i][j];
            }
        }
    }

    int sum_secondary = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (i + j == N - 1)
            {
                sum_secondary += array[i][j];
            }
        }
    }

    int result = sum_primary - sum_secondary;
    printf("%d\n", abs(result));

    return 0;
}