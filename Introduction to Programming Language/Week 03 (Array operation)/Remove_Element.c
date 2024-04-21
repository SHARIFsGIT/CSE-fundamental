#include <stdio.h>
int main()
{
    int N;
    scanf("%d", &N);

    int array[N];

    for (int i = 0; i < N; i++)
    {
        scanf("%d ", &array[i]);
    }

    int position;
    scanf("%d", &position);

    for (int i = position; i < N - 1; i++)
    {
        array[i] = array[i + 1];
    }

    for (int i = 0; i < N - 1; i++)
    {
        printf("%d ", array[i]);
    }

    return 0;
}