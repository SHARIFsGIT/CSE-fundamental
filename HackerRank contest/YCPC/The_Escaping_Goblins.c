#include <stdio.h>
int main()
{
    int A, B, K;
    scanf("%d %d", &A, &B);
    scanf("%d", &K);

    if (abs(A - B) > K)
    {
        printf("YES\n");
    }
    else
    {
        printf("NO\n");
    }

    return 0;
}