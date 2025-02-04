#include <stdio.h>
int main()
{
    int a, b;
    scanf("%d %d", &a, &b);

    int answer = a + b + (a * b);

    if (answer == 111)
    {
        printf("Yes\n");
    }
    else
    {
        printf("No\n");
    }

    return 0;
}