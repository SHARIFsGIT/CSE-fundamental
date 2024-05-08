#include <stdio.h>
#include <limits.h>
int recursive(int array[], int N, int i)
{
    if (i == N)
    {
        return INT_MIN;
    }

    int result = recursive(array, N, i + 1);

    if (array[i] > result)
    {
        return array[i];
    }
    else
    {
        return result;
    }
}
int main()
{
    int N;
    scanf("%d", &N);

    int array[N];
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &array[i]);
    }

    int result = recursive(array, N, 0);
    printf("%d", result);
    return 0;
}