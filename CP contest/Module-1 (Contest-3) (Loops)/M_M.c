#include <stdio.h>
int main()
{
    int t;
    scanf("%d", &t);

    while (t--)
    {
        char a, b, c, d, e, f;
        scanf(" %c %c %c %c %c %c", &a, &b, &c, &d, &e, &f);

        if ((a == 'W' && b == 'W' && c == 'W') ||
            (b == 'W' && c == 'W' && d == 'W') ||
            (c == 'W' && d == 'W' && e == 'W') ||
            (d == 'W' && e == 'W' && f == 'W'))
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }
    }

    return 0;
}