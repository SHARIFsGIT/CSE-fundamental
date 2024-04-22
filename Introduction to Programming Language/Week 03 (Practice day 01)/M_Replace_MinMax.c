#include <stdio.h>
#include <limits.h>
int main()
{
    int N;
    scanf("%d", &N);

    int array[N];
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &array[i]);
    }

    int min = INT_MAX;
    int max = INT_MIN;
    int positionMin;
    int positionMax;
    for (int i = 0; i < N; i++)
    {
        if (array[i] < min)
        {
            min = array[i];
            positionMin = i;
        }
        if (array[i] > max)
        {
            max = array[i];
            positionMax = i;
        }
    }
    array[positionMin] = max;
    array[positionMax] = min;

    for (int i = 0; i < N; i++)
    {
        printf("%d ", array[i]);
    }

    return 0;
}