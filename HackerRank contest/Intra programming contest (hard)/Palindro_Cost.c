#include <stdio.h>
#include <string.h>

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
            int cost = S[i] > S[n - 1 - i] ? S[i] - S[n - 1 - i] : S[n - 1 - i] - S[i];
            totalCost += cost;
        }

        (totalCost <= K) ? printf("YES\n") : printf("NO\n");
    }

    return 0;
}
