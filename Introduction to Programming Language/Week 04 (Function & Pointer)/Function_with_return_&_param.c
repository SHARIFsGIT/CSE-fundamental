#include <stdio.h>

// int sum(int x, int y)
// {
//     int result = x + y;
//     return result;
// }

// OR

int sum(int x, int y);

int main()
{
    int display = sum(10, 20);
    printf("%d\n", display);
    return 0;
}

int sum(int x, int y)
{
    int result = x + y;
    return result;
}