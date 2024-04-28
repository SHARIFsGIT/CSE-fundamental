#include <stdio.h>
int main()
{
    int N;
    scanf("%d", &N);

    int space = 0;
    int star = N + 2;
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= space; j++)
        {
            printf(" ");
        }
        for (int j = 1; j <= star; j++)
        {
            printf("*");
        }
        star = star - 2;
        space = i;
        printf("\n");
    }

    return 0;
}