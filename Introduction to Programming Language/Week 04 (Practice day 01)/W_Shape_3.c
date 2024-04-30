#include <stdio.h>
int main()
{
    int N;
    scanf("%d", &N);

    int space = N - 1;
    int star = 1;
    for (int i = 1; i <= 2 * N; i++)
    {
        for (int j = 1; j <= space; j++)
        {
            printf(" ");
        }
        for (int j = 1; j <= star; j++)
        {
            printf("*");
        }
        if (i <= N - 1)
        {
            space--;
            star += 2;
        }
        else if (i == N)
        {
            space = 0;
            star = 2 * N - 1;
        }
        else
        {
            space++;
            star -= 2;
        }

        printf("\n");
    }

    return 0;
}