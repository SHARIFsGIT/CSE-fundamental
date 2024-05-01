#include <stdio.h>
#include <string.h>
void func(char *array)
{
    // int size = sizeof(array) / sizeof(char);
    // printf("Inside func: %d\n", size);
    printf("Length of array: %d\n", strlen(array));
}
int main()
{
    char array[60] = "Hello";
    int size = sizeof(array) / sizeof(char);
    printf("Inside main: %d\n", size);
    func(array);
    return 0;
}