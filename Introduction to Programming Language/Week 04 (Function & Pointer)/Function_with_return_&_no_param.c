#include <stdio.h>
int sum()
{
    int x = 10;
    int y = 20;
    int result = x + y;
    return result;
}
int main()
{
    int display = sum();
    printf("%d", display);
    return 0;
}