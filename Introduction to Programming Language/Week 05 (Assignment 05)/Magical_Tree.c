#include <stdio.h>
int main()
{
    int N;
    scanf("%d", &N);

    int space = 5;
    int star = 1;

    for (int i = 1; i <= space + N; i++)
    {
        for (int j = 1; j <= space; j++)
        {
            printf(" ");
        }
        for (int k = 1; k <= star; k++)
        {
            printf("*");
        }
        space--;
        star +2;
        printf("\n");
    }

    return 0;
}