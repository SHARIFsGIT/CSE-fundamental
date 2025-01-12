#include <stdio.h>
int main()
{
    int x, n;
    scanf("%d %d", &x, &n);

    int remaining_money = x - (n * 10);
    int buy = remaining_money / 20;

    printf("%d", buy);

    return 0;
}