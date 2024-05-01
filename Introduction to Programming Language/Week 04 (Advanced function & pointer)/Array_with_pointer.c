#include <stdio.h>
int main()
{
    int array[5] = {10, 20, 30, 40, 50};
    printf("0th index address: %p\n", &array[0]);
    printf("All index address: %p\n", array);

    printf("0th index value: %d\n", array[0]);
    printf("All index value: %d\n", *array);

    printf("1st index value with indexing: %d\n", array[1]);
    printf("1st index value with indexing: %d\n", 1[array]);
    printf("1st index value with dereferencing: %d\n", *(array + 1));
    printf("1st index value with dereferencing: %d\n", *(1 + array));

    /*
        array[1] = *(array + 1)
        *(array + 1) = *(1 + array)
        *(array + 1) = array[1]
        *(array + 1) = 1[array]
    */

    return 0;
}