#include <stdio.h>
void recursion(int i, int N)
{
    if (i == N + 1)
    {
        return;
    }

    printf("I love Recursion\n");
    recursion(i + 1, N);
}
int main()
{
    int N;
    scanf("%d", &N);

    recursion(1, N);
    return 0;
}