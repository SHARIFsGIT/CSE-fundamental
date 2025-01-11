#include <stdio.h>
int main()
{
    int n;
    scanf("%d", &n);

    int yea = n / 10;
    int r = n - yea * 10;
    int a = yea - ((yea / 10) * 10);

    printf("K%d%d", a, r);

    return 0;
}