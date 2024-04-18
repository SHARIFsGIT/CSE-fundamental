#include <stdio.h>
int main()
{
    int N;
    scanf("%d", &N);

    int array[N];

    for (int i = 0; i < N; i++)
    {
        scanf("%d", &array[i]);
    }

    int posSum = 0;
    int negSum = 0;

    for (int i = 0; i < N; i++)
    {
        if (array[i] > 0)
        {
            posSum += array[i];
        }
        else
            negSum += array[i];
    }
    printf("%d %d", posSum, negSum);

    return 0;
}