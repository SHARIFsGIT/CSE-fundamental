#include <bits/stdc++.h>
using namespace std;

int dp[1005][1005];

int subset_sum(int n, int arr[], int sum)
{
    if (n == 0)
    {
        if (sum == 0)
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }

    if (dp[n][sum] != -1)
    {
        return dp[n][sum];
    }

    if (arr[n - 1] <= sum)
    {
        int opt1 = subset_sum(n - 1, arr, sum - arr[n - 1]);
        int opt2 = subset_sum(n - 1, arr, sum);

        return dp[n][sum] = opt1 + opt2;
    }
    else
    {
        return dp[n][sum] = subset_sum(n - 1, arr, sum);
    }
}

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

    dp[0][0] = true;

    for (int i = 1; i <= sum; i++)
    {
        dp[0][i] = 0;
    }

    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j <= sum; j++)
        {
            if (array[i - 1] <= j)
            {
                int opt1 = dp[i - 1][j - array[i - 1]];
                int opt2 = dp[i - 1][j];

                dp[i][j] = opt1 + opt2;
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
            cout << dp[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}