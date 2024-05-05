#include <stdio.h>
void func(int array[], int n, int i)
{
    if (i == n)
    {
        return;
    }

    printf("%d\n", array[i]);
    func(array, 5, i+1);
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

    func(array, N, 0);

    return 0;
}