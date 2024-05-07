#include <stdio.h>
void recursive(long long array[], int i, int n, long long sum)
{
    if (i == n)
    {
        printf("%lld", sum);
        return;
    }

    sum = sum + array[i];
    recursive(array, i + 1, n, sum);
}
int main()
{
    int N;
    scanf("%d", &N);

    long long array[N];
    for (int i = 0; i < N; i++)
    {
        scanf("%lld", &array[i]);
    }
    long long sum = 0;

    recursive(array, 0, N, sum);

    return 0;
}