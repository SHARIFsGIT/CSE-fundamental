#include <stdio.h>
void sum(int x, int y)
{
    int result = x + y;
    printf("%d", result);
}
int main()
{
    sum(10, 20);
    return 0;
}