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

    int X;
    scanf("%d", &X);

    int flag = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (array[i][j] == X)
            {
                flag = 1;
                break;
            }
        }
    }

    if (flag)
    {
        printf("will not take number\n");
    }
    else
    {
        printf("will take number\n");
    }

    return 0;
}