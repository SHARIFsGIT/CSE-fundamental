#include <stdio.h>
int main()
{
    int x, y;
    scanf("%d %d", &x, &y);

    int normal_day = x * 6;
    int special_day = y;

    printf("%d", normal_day + special_day);

    return 0;
}