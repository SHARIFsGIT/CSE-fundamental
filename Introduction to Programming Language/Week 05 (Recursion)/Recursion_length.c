#include <stdio.h>
int func(char array[], int i)
{
    if (array[i] == '\0')
    {
        return 0;
    }
    
    int length = func(array, i + 1);
    return length + 1;
}
int main()
{
    char array[100] = "programming";
    int length = func(array, 0);
    printf("%d\n", length);
    return 0;
}