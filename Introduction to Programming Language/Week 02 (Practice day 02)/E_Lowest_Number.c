#include <stdio.h>
#include <limits.h>

int main()
{
    int N;
    scanf("%d", &N);

    int arr[N];

    for (int i = 0; i < N; i++)
    {
        scanf("%d", &arr[i]);
    }

    int min = INT_MAX;
    int position;

    for (int i = 0; i < N; i++)
    {
        if (arr[i] < min)
        {
            min = arr[i];
            position = i+1;
        }
    }
    printf("%d %d", min, position);
    
    return 0;
}