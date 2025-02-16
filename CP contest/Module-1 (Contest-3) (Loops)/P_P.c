#include <stdio.h>
int main()
{
    int t;
    scanf("%d", &t);

    while (t--)
    {
        int x, y, z;
        scanf("%d %d %d", &x, &y, &z);

        int z_min = z * 24 * 60;

        if (x * y > z_min)
        {
            printf("NO\n");
        }
        else
        {
            printf("YES\n");
        }
    }

    return 0;
}