#include <stdio.h>
int main()
{
    int N = 3;

    int array[N];
    int old[N];

    for (int i = 0; i < N; i++)
    {
        scanf("%d", &array[i]);
    }

    for (int j = 0; j < N; j++)
    {
        old[j] = array[j];
    }

    for (int i = 0; i < N - 1; i++)
    {
        for (int j = i + 1; j < N; j++)
        {
            if (array[i] > array[j])
            {
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
    }

    for (int i = 0; i < N; i++)
    {
        printf("%d\n", array[i]);
    }

    printf("\n");

    for (int j = 0; j < N; j++)
    {
        printf("%d\n", old[j]);
    }

    return 0;
}

/*
#include <stdio.h>
int main()
{
    int A, B, C;
    scanf("%d %d %d", &A, &B, &C);

    int array[3] = {A, B, C};

    for (int i = 0; i < 2; i++)
    {
        for (int j = i + 1; j < 3; j++)
        {
            if (array[i] > array[j])
            {
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
    }
    for (int i = 0; i < 3; i++)
    {
        printf("%d\n", array[i]);
    }
    printf("\n");
    printf("%d\n%d\n%d\n", A, B, C);
    return 0;
}
*/