#include <stdio.h>
int count_before_one(int array[], int value)
{
    int count = 0;
    for (int i = 0; i < value; i++)
    {
        if (array[i] == 1)
        {
            break;
        }
        if (array[i] != 1)
        {
            count++;
        }
    }
    return count;
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

    int result = count_before_one(array, N);
    printf("%d\n", result);

    return 0;
}