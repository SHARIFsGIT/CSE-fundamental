#include <stdio.h>
int main()
{
    int rows, cols;
    printf("Number of rows & columns: ");
    scanf("%d %d", &rows, &cols);

    int array[rows][cols];
    printf("Value of each rows & columns:\n");
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            scanf("%d", &array[i][j]);
        }
    }

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            printf("array[%d][%d]: %d \t", i, j, array[i][j]);
        }
        printf("\n");
    }

    int exact_row;
    printf("Exact number of row: ");
    scanf("%d", &exact_row);

    for (int i = 0; i < cols; i++)
    {
        printf("a[%d][%d]->%d \t", exact_row, i, array[exact_row][i]);
    }
    printf("\n");

    int exact_column;
    printf("Exact number of column: ");
    scanf("%d", &exact_column);

    for (int i = 0; i < rows; i++)
    {
        printf("a[%d][%d]->%d \n", i, exact_column, array[i][exact_column]);
    }

    return 0;
}