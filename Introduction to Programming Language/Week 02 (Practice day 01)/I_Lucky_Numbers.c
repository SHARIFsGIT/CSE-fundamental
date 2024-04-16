#include <stdio.h>
int main()
{
    int N;
    scanf("%d", &N);

    int quotient = N / 10;
    int remainder = N % 10;

    if ((remainder % quotient == 0) || (quotient % remainder == 0))
    {
        printf("YES");
    }
    else{
        printf("NO");
    }
    return 0;
}