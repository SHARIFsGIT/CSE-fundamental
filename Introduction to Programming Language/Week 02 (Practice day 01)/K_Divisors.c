#include <stdio.h>
int main()
{
    int N;
    scanf("%d", &N);

    for (int j = 1; j <= N; j++)
    {
        if (N % j == 0)
        {
            printf("%d\n", j);
        }
    }
    return 0;
}