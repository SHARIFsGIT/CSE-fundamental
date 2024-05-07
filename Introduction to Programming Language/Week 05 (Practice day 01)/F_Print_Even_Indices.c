#include <stdio.h>
void recursive(int array[], int i, int n)
{  
    if (i == n)
    {
        return;
    }

    recursive(array, i + 1, n);
    
    if (i % 2 == 0)
    {
        printf("%d ", array[i]);
    }
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

    recursive(array, 0, N);

    return 0;
}