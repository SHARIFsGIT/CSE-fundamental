#include <stdio.h>
int main()
{
    int N, K;
    scanf("%d %d", &N, &K);

    long long int array[N];
    for (int i = 0; i < N; i++)
    {
        scanf("%lld", &array[i]);
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = i + 1; j < N; j++)
        {
            if (array[i] < array[j])
            {
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
    }

    long long int sum = 0;
    for (int i = 0; i < K; i++)
    {
        sum += array[i];
    }
    printf("%lld\n", sum);

    return 0;
}