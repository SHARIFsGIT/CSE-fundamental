#include <stdio.h>
int main()
{
    int N;
    scanf("%d", &N);

    int A[N];
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &A[i]);
    }

    int divBy2 = 0;
    int divBy3 = 0;
    for (int i = 0; i < N; i++)
    {
        if (A[i] % 2 == 0 && A[i] % 3 == 0) 
        {
            divBy2++;
        }
        else if (A[i] % 2 == 0)
        {
            divBy2++;
        }
        else if (A[i] % 3 == 0)
        {
            divBy3++;
        }
    }
    printf("%d %d", divBy2, divBy3);
    
    
    return 0;
}