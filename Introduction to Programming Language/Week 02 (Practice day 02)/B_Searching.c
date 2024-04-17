#include <stdio.h>
int main()
{
    int N;
    scanf("%d", &N);

    int arr[N];
    for (int i = 0; i < N; i++)
    {
        scanf("%d ", &arr[i]);
    }
    int X;
    scanf("%d", &X);
    int ans = -1;
    for (int i = 0; i < N; i++)
    {
        if (arr[i] == X)
        {
            ans = i;
            break;
        }
    }
    printf("%d", ans);
    
    return 0;
}