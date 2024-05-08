#include <stdio.h>
void recursive(int N)
{
    if (N == 0)
    {
        return;
    }

    int mod = N % 10;
    recursive(N / 10);
    printf("%d ", mod);
}
int main()
{
    int T;
    scanf("%d", &T);

    int N;
    for (int i = 0; i < T; i++)
    {
        scanf("%d", &N);
        recursive(N);
        if (N == 0)
        {
            printf("0");
        }
        
        printf("\n");
    }

    return 0;
}