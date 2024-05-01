#include <stdio.h>
void func(int *array, int size)
{
    // for (int i = 0; i < size; i++)
    // {
    //     printf("%d ", array[i]);
    // }
    // printf("\n");
    array[0] = 50;
    array[1] = 500;
}
int main()
{
    int array[5] = {1, 2, 3, 4, 5};
    func(array, 5);
    for (int i = 0; i < 5; i++)
    {
        printf("%d ", array[i]);
    }

    return 0;
}