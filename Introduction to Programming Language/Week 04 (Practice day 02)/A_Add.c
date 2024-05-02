#include <stdio.h>
int summation(int x, int y)
{
    int sum = x + y;
    return sum;
}
int main()
{
    int a, b;
    scanf("%d %d", &a, &b);

    int result = summation(a, b);
    printf("%d\n", result); 
    return 0;
}