#include <bits/stdc++.h>
using namespace std;

const int maxN = 1000;
const int maxW = 1000;

int dp[maxN + 1][maxW + 1];

int knapsack(int n, int weight[], int value[], int W)
{
    if (n == 0 || W == 0)
    {
        return 0;
    }

    if (dp[n][W] != -1)
    {
        return dp[n][W];
    }

    if (weight[n - 1] <= W)
    {
        int includeItem = knapsack(n - 1, weight, value, W - weight[n - 1]) + value[n - 1];

        int skipItem = knapsack(n - 1, weight, value, W);

        return dp[n][W] = max(includeItem, skipItem);
    }
    else
    {
        return dp[n][W] = knapsack(n - 1, weight, value, W);
    }
}

void solveTestCase()
{
    int n, W;
    cin >> n >> W;

    int weight[n], value[n];

    for (int i = 0; i < n; i++)
    {
        cin >> weight[i];
    }

    for (int i = 0; i < n; i++)
    {
        cin >> value[i];
    }

    memset(dp, -1, sizeof(dp));

    cout << knapsack(n, weight, value, W) << endl;
}

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        solveTestCase();
    }

    return 0;
}
