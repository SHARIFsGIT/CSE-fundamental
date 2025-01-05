#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N, W;
    cin >> N >> W;

    vector<int> weight(N);
    vector<int> value(N);

    for (int i = 0; i < N; i++)
    {
        cin >> weight[i] >> value[i];
    }

    vector<vector<int>> dp(N + 1, vector<int>(W + 1, 0));

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= W; j++)
        {
            if (weight[i - 1] <= j)
            {
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i - 1]] + value[i - 1]);
            }
            else
            {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    cout << dp[N][W] << endl;

    return 0;
}
