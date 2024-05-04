#include <stdio.h>
void swap_it(int *A, int *B)
{
    int temp = *A;
    *A = *B;
    *B = temp;
}
int main()
{
    int A, B;
    scanf("%d %d", &A, &B);

    swap_it(&A, &B);
    printf("%d %d", A, B);

    return 0;
}