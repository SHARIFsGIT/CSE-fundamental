#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int sum = 0;
    int array[n];

    for (int i = 0; i < n; i++)
    {
        cin >> array[i];
        sum += array[i];
    }

    if (sum % 2 == 0)
    {
        int find = sum / 2;

        bool dp[n + 1][find + 1];
        memset(dp, false, sizeof(dp));

        dp[0][0] = true;

        for (int i = 1; i <= find; i++)
        {
            dp[0][i] = false;
        }

        for (int i = 1; i <= n; i++)
        {
            for (int j = 0; j <= find; j++)
            {
                if (j >= array[i - 1])
                {
                    dp[i][j] = dp[i - 1][j] || dp[i - 1][j - array[i - 1]];
                }
                else
                {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }

        if (dp[n][find])
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }
    else
    {
        cout << "NO" << endl;
    }

    return 0;
}
