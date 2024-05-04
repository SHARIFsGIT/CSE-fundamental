#include <stdio.h>
int my_abs(int N)
{
    if (N > 0)
        return N;
    else
        return N * (-1);
}
int main()
{
    int N;
    scanf("%d", &N);

    int result = my_abs(N);
    printf("%d\n", result);
    return 0;
}