#include <stdio.h>
void change_it(int *array, int n)
{
    array[n - 1] = 100;
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

    change_it(array, N);
    for (int i = 0; i < N; i++)
    {
        printf("%d ", array[i]);
    }

    return 0;
}