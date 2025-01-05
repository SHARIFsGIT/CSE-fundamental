#include <bits/stdc++.h>
using namespace std;

const int maxN = 1000;
const int maxW = 1000;
int dp[maxN][maxW];

// top-down approch
// complexity: O(n*W)
int knapsack(int n, int weight[], int value[], int W)
{
    if (n < 0 || W == 0)
    {
        // invalid index
        return 0;
    }

    if (dp[n][W] != -1)
    {
        return dp[n][W];
    }

    if (weight[n] <= W)
    {
        // two options: 1. take 2. don't
        int option1 = knapsack(n - 1, weight, value, W - weight[n]) + value[n];
        int option2 = knapsack(n - 1, weight, value, W);

        dp[n][W] = max(option1, option2);

        return dp[n][W];
    }
    else
    {
        // one option: 1. don't
        int option2 = knapsack(n - 1, weight, value, W);

        dp[n][W] = option2;

        return dp[n][W];
    }
}

int main()
{
    int n;
    cin >> n;

    int weight[n];
    int value[n];

    for (int i = 0; i < n; i++)
    {
        cin >> weight[i];
    }

    for (int i = 0; i < n; i++)
    {
        cin >> value[i];
    }

    int W;
    cin >> W;

    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= W; j++)
        {
            dp[i][j] = -1;
        }
    }

    cout << knapsack(n - 1, weight, value, W) << endl;

    return 0;
}