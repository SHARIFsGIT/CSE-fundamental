#include <stdio.h>
int main()
{
    int N;
    scanf("%d", &N);

    int arrayA[N];

    for (int i = 0; i < N; i++)
    {
        scanf("%d", &arrayA[i]);
    }

    int M;
    scanf("%d", &M);

    int arrayB[N];

    for (int i = 0; i < M; i++)
    {
        scanf("%d", &arrayB[i]);
    }

    int ansArray[N + M];

    for (int i = 0; i < N; i++)
    {
        ansArray[i] = arrayA[i];
    }

    int i = N;

    for (int j = 0; j < M; j++)
    {
        ansArray[i] = arrayB[j];
        i++;
    }

    for (int i = 0; i < N + M; i++)
    {
        printf("%d ", ansArray[i]);
    }

    return 0;
}