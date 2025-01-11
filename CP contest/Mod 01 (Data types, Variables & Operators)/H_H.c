#include <stdio.h>
int main()
{
    long long int a, b;
    scanf("%lld %lld", &a, &b);

    long long int ans = (a + b - 1) / b;

    printf("%lld", ans);

    return 0;
}