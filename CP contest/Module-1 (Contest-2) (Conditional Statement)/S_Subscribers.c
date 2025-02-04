#include <stdio.h>
int main()
{
    int n;
    scanf("%d", &n);

    if (n <= 1e3 - 1)
    {
        printf("%d\n", n);
    }
    else if (n <= 1e4 - 1)
    {
        n = (n / 10) * 10;
        printf("%d\n", n);
    }
    else if (n <= 1e5 - 1)
    {
        n = (n / 100) * 100;
        printf("%d\n", n);
    }
    else if (n <= 1e6 - 1)
    {
        n = (n / 1000) * 1000;
        printf("%d\n", n);
    }
    else if (n <= 1e7 - 1)
    {
        n = (n / 10000) * 10000;
        printf("%d\n", n);
    }
    else if (n <= 1e8 - 1)
    {
        n = (n / 100000) * 100000;
        printf("%d\n", n);
    }
    else
    {
        n = (n / 1000000) * 1000000;
        printf("%d\n", n);
    }

    return 0;
}