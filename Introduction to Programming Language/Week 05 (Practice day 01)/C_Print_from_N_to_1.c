#include <stdio.h>
void recursive(int n)
{
    if (n == 1)
    {
        printf("%d", n);
        return;
    }
    printf("%d ", n);
    recursive(n - 1);
}
int main()
{
    int N;
    scanf("%d", &N);

    recursive(N);
    return 0;
}