#include <stdio.h>
int main()
{
    int N;
    scanf("%d", &N);

    int star = N;
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= star; j++)
        {
            printf("*");
        }
        star--;
        printf("\n");
    }

    return 0;
}