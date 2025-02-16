#include <stdio.h>
int main()
{
    int t;
    scanf("%d", &t);

    while (t--)
    {
        int s;
        scanf("%d", &s);

        int words = 24 * s * 1000;

        printf("%d\n", words);
    }
    return 0;
}