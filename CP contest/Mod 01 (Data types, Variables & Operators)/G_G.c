#include <stdio.h>
int main()
{
    int abc;
    scanf("%d", &abc);

    int c = abc - ((abc / 10) * 10);
    int b = (abc / 10) - ((abc / 100) * 10);
    int a = abc / 100;

    int bca = b * 100 + c * 10 + a;
    int cab = c * 100 + a * 10 + b;

    printf("%d", abc + bca + cab);

    return 0;
}