#include <stdio.h>
int main()
{
    int t;
    scanf("%d", &t);

    while (t--)
    {
        int x, y, z;
        scanf("%d %d %d", &x, &y, &z);

        int totalStudents = x * y;
        double totalPassed = totalStudents * 0.5;

        if (totalPassed < z)
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