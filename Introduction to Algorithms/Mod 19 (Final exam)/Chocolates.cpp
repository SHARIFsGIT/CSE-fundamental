#include <bits/stdc++.h>
using namespace std;

void checkPartition()
{
    int n;
    cin >> n;

    vector<int> a(n);
    int totalSum = 0;

    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        totalSum += a[i];
    }

    if (totalSum % 2 != 0)
    {
        cout << "NO" << endl;
        return;
    }

    int targetSum = totalSum / 2;

    vector<vector<bool>> dp(n + 1, vector<bool>(targetSum + 1, false));

    for (int i = 0; i <= n; i++)
    {
        dp[i][0] = true;
    }

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= targetSum; j++)
        {
            if (a[i - 1] <= j)
            {
                dp[i][j] = dp[i - 1][j - a[i - 1]] || dp[i - 1][j];
            }
            else
            {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    cout << (dp[n][targetSum] ? "YES" : "NO") << endl;
}

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        checkPartition();
    }

    return 0;
}
