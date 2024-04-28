#include <stdio.h>
int main()
{
    int N;
    scanf("%d", &N);

    int star = 1;
    int space = N - 1;
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
        space--;
        star = star + 2;
        printf("\n");
    }

    return 0;
}