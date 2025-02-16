#include <stdio.h>
int main()
{
    int t;
    scanf("%d", &t);

    while (t--)
    {
        int n, m;
        scanf("%d %d", &n, &m);

        if (m >= n)
        {
            printf("0\n");
        }
        else
        {
            printf("%d\n", n - m);
        }
    }
    return 0;
}