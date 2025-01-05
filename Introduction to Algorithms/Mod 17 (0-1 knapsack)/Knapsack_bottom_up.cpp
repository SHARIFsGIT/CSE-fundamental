#include <bits/stdc++.h>
using namespace std;

// bottom-up approch
// complexity: O(n*W)
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

    int dp[n + 1][W + 1];

    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= W; j++)
        {
            if (i == 0 || j == 0)
            {
                dp[i][j] = 0;
            }
        }
    }

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= W; j++)
        {
            if (weight[i - 1] <= j)
            {
                int option1 = dp[i - 1][j - weight[i - 1]] + value[i - 1];
                int option2 = dp[i - 1][j];

                dp[i][j] = max(option1, option2);
            }
            else
            {
                int option2 = dp[i - 1][j];
                dp[i][j] = option2;
            }
        }
    }

    cout << dp[n][W] << endl;

    return 0;
}