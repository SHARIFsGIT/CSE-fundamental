#include <stdio.h>
int main()
{
    int t;
    scanf("%d", &t);

    for (int i = 0; i < t; i++)
    {
        int x;
        scanf("%d", &x);

        printf("%d\n", x - 10);
    }

    return 0;
}