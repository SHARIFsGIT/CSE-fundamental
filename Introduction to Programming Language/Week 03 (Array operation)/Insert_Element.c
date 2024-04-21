#include <stdio.h>
int main()
{
    int N;
    scanf("%d", &N);

    int array[N+1];

    for (int i = 0; i < N; i++)
    {
        scanf("%d ", &array[i]);
    }

    int position, value;
    scanf("%d %d", &position, &value);

    for (int i = N; i >= position+1; i--)
    {
        array[i] = array[i-1];
    }

    array[position] = value;

    for (int i = 0; i <= N; i++)
    {
        printf("%d ", array[i]);
    } 
    return 0;
}