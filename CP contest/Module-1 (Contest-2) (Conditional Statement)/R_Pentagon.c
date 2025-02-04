#include <stdio.h>
#include <math.h>

int main()
{
    char s1, s2, t1, t2;
    scanf("%c%c %c%c", &s1, &s2, &t1, &t2);

    int d1 = abs(s1 - s2);
    if (d1 > 2)
    {
        d1 = 5 - d1;
    }

    int d2 = abs(t1 - t2);
    if (d2 > 2)
    {
        d2 = 5 - d2;
    }

    if (d1 == d2)
    {
        printf("Yes\n");
    }
    else
    {
        printf("No\n");
    }

    return 0;
}