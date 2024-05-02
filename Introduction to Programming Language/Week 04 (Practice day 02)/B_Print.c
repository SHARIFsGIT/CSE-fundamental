#include <stdio.h>
void func(int N)
{
    printf("1");
    for (int i = 2; i <= N; i++)
    {
        printf(" %d", i);
    }
    
}
int main()
{
    int N;
    scanf("%d", &N);

    func(N);

    return 0;
}