#include <stdio.h>
int main()
{
    int N, M;
    scanf("%d %d", &N, &M);

    int array[N][M];
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            scanf("%d", &array[i][j]);
        }
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = M - 1; j >= 0; j--)
        {
            printf("%d ", array[i][j]);
        }
        printf("\n");
    }

    return 0;
}