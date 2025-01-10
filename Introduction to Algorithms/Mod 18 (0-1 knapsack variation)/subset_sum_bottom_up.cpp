#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int array[n];
    for (int i = 0; i < n; i++)
    {
        cin >> array[i];
    }

    int sum;
    cin >> sum;

    bool dp[n + 1][sum + 1];

    dp[0][0] = true;

    for (int i = 1; i <= sum; i++)
    {
        dp[0][i] = false;
    }

    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j <= sum; j++)
        {
            if (array[i - 1] <= j)
            {
                bool opt1 = dp[i - 1][j - array[i - 1]];
                bool opt2 = dp[i - 1][j];

                dp[i][j] = opt1 || opt2;
            }
            else
            {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= sum; j++)
        {
            if (dp[i][j])
            {
                cout << "T ";
            }
            else
            {
                cout << "F ";
            }
        }
        cout << endl;
    }

    if (dp[n][sum])
    {
        cout << "YES" << endl;
    }
    else
    {
        cout << "NO" << endl;
    }

    return 0;
}