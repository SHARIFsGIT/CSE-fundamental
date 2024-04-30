#include <stdio.h>
int main()
{
    int N;
    scanf("%d", &N);

    int star = 2 * N - 1;
    int space = 1;

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= star; j++)
        {
            printf("*");
        }
        printf("\n");
        for (int j = 1; j <= space; j++)
        {
            printf(" ");
        }
        star -= 2;
        space++;
    }

    return 0;
}