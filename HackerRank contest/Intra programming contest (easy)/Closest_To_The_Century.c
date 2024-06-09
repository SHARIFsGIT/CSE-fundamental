#include <stdio.h>
#include <stdlib.h>

int main()
{
    int T;
    scanf("%d", &T);

    while (T--)
    {
        int N;
        scanf("%d", &N);

        int scores[N];
        for (int i = 0; i < N; ++i)
        {
            scanf("%d", &scores[i]);
        }

        int closest = -1;
        for (int i = 0; i < N; ++i)
        {
            if (scores[i] < 100)
            {
                if (closest == -1 || abs(100 - scores[i]) < abs(100 - closest))
                {
                    closest = scores[i];
                }
            }
        }
        printf("%d\n", closest);
    }

    return 0;
}
