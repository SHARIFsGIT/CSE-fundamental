#include <stdio.h>
int main()
{
    int R, C;
    scanf("%d %d", &R, &C);

    int arrayA[R][C];
    int arrayB[R][C];
    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            scanf("%d", &arrayA[i][j]);
        }
    }

    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            scanf("%d", &arrayB[i][j]);
        }
    }

    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            printf("%d ", arrayA[i][j] + arrayB[i][j]);
        }
        printf("\n");
    }

    return 0;
}