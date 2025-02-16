#include <stdio.h>
int main()
{
    int t;
    scanf("%d", &t);

    while (t--)
    {
        int n, x, d;
        scanf("%d %d %d", &n, &x, &d);

        int bunsPerDay = x * 5;
        int daysSurvived = n / bunsPerDay;

        int totalSurvived = daysSurvived + d;
        
        printf("%d\n", totalSurvived);
    }

    return 0;
}