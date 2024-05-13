#include <stdio.h>
int main()
{
    int N;
    scanf("%d", &N);

    int array[N];
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &array[i]);
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = i + 1; j < N; j++)
        {
            if (array[j] > array[i])
            {
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
    }

    int count = 0;
    for (int i = 0; i < N; i++)
    {
        if (array[i] == array[N - 1])
        {
            count++;
        }
    }
    
    if (count % 2 == 1)
    {
        printf("Lucky");
    }
    else
    {
        printf("Unlucky");
    }
    

    return 0;
}