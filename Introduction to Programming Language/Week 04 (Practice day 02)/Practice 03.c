#include <stdio.h>
int count_odd(int *array, int N)
{
    int count_odd = 0;
    for (int i = 0; i < N; i++)
    {
        if (array[i] % 2 == 1)
        {
            count_odd++;
        }
    }
    return count_odd;
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

    int count = count_odd(array, N);
    printf("%d\n", count);

    return 0;
}