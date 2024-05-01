#include <stdio.h>
void func(int array[], int n)
{
    // int size = sizeof(array) / sizeof(int);
    // printf("Array size in func: %d\n", size);

    for (int i = 0; i < n; i++)
    {
        printf("%d ", array[i]);
    }
    
}
int main()
{
    int array[5] = {1, 2, 3, 4, 5};
    int size = sizeof(array) / sizeof(int);
    printf("Array size in main: %d\n", size);
    func(array, 5);
    return 0;
}