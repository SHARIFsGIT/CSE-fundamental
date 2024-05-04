#include <stdio.h>
int function(int array[], int N)
{
    int max = array[0];
    int min = array[0];
    for (int i = 0; i < N; i++)
    {
        if (array[i] > max)
        {
            max = array[i];
        }
        if (array[i] < min)
        {
            min = array[i];
        }
    }
    printf("%d %d\n", min, max);

    return 0;
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

    function(array, N);
    return 0;
}