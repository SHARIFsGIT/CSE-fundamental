#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int charDifference(char a, char b)
{
    return abs(a - b);
}

int main()
{
    int Q;
    scanf("%d", &Q);

    while (Q--)
    {
        char S[100001];
        int K;
        scanf("%s %d", S, &K);

        int n = strlen(S);
        int totalCost = 0;

        for (int i = 0; i < n / 2; i++)
        {
            totalCost += charDifference(S[i], S[n - 1 - i]);
        }

        (totalCost <= K) ? printf("YES\n") : printf("NO\n");
    }

    return 0;
}
