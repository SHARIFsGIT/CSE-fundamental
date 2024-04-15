#include <stdio.h>
int main()
{
    int N;
    scanf("%d", &N);

    int even = 0, odd = 0, positive = 0, negative = 0;

    int numbers;
    for (int i = 0; i < N; i++)
    {
        scanf("%d ", &numbers);

        if(numbers % 2 == 0)
            even++;
        else
            odd++;

        if (numbers > 0)
            positive++;
        else if(numbers < 0)
            negative++;
    }
    printf("Even: %d\nOdd: %d\nPositive: %d\nNegative: %d", even, odd, positive, negative);

    return 0;
}