#include <stdio.h>
int main()
{
    int N;
    scanf("%d", &N);

    char A[N];
    for (int i = 0; i < N; i++)
    {
        scanf("%s", A);
    }

    int sum = 0;
    for (int i = 0; A[i] != '\0'; i++)
    {
        sum += (A[i] - 48);
    }
    printf("%d\n", sum);

    return 0;
}