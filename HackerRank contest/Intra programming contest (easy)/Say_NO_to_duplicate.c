#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
}

int main()
{
    int T;
    scanf("%d", &T);

    while (T--)
    {
        int N;
        scanf("%d", &N);

        int arr[N];
        for (int i = 0; i < N; i++)
        {
            scanf("%d", &arr[i]);
        }

        qsort(arr, N, sizeof(int), compare);

        printf("%d", arr[0]);
        for (int i = 1; i < N; i++)
        {
            if (arr[i] != arr[i - 1])
            {
                printf(" %d", arr[i]);
            }
        }
        printf("\n");
    }
    return 0;
}
