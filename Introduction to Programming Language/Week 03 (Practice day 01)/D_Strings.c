#include <stdio.h>
int main()
{
    char A[11];
    char B[11];
    scanf("%s %s", A, B);

    int lenA = strlen(A);
    int lenB = strlen(B);
    printf("%d %d\n", lenA, lenB);
    printf("%s%s\n", A, B);

    char tempA = A[0];
    char tempB = B[0];
    B[0] = tempA;
    A[0] = tempB;
    printf("%s %s", A, B);
    return 0;
}