#include <stdio.h>
int main()
{
    int n;
    scanf("%d", &n);

    int last_two = n % 100;
    printf("K%02d", last_two);

    return 0;
}