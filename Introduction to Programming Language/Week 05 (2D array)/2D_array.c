#include <stdio.h>
int main()
{
    int array[4][3];
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            scanf("%d", &array[i][j]);
        }
    }

    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("a[%d][%d]->%d\t", i, j, array[i][j]);
        }
        printf("\n");
    }

    return 0;
}