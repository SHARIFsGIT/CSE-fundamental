#include <stdio.h>
int main()
{
    int N, K;
    scanf("%d %d", &N, &K);

    int array[N];
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &array[i]);
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 1; j < N; j++)
        {
            if (array[i] < array[j])
            {
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
        printf("%d ", array[i]);
    }

    return 0;
}