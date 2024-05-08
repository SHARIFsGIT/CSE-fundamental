#include <stdio.h>
long long int recursive(int N)
{
    if (N == 0)
    {
        return 1;
    }

    long long int ans = recursive(N - 1);
    return N * ans;
}
int main()
{
    int N;
    scanf("%d", &N);

    long long int result = recursive(N);
    printf("%lld\n", result);
    return 0;
}