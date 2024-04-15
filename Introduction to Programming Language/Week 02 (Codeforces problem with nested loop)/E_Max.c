#include <stdio.h>
#include <limits.h>
int main()
{
    int N;
    scanf("%d", &N);

    int numbers;
    int max = INT_MIN, min = INT_MAX;
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &numbers);
        if (numbers > max)
        {
            max = numbers;
        }
        if (numbers < min)
        {
            min = numbers;
        }
        
    }
    printf("Max: %d Min: %d", max, min);

    return 0;
}