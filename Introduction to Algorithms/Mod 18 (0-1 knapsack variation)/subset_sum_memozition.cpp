#include <bits/stdc++.h>
using namespace std;

int dp[1005][1005];

// complexity: O(n*sum)
bool subset_sum(int n, int arr[], int sum)
{
    if (n == 0)
    {
        if (sum == 0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    if (dp[n][sum] != -1)
    {
        return dp[n][sum];
    }

    if (arr[n - 1] <= sum)
    {
        bool opt1 = subset_sum(n - 1, arr, sum - arr[n - 1]);
        bool opt2 = subset_sum(n - 1, arr, sum);

        return dp[n][sum] = opt1 || opt2;
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

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            dp[i][j] = -1;
        }
    }

    if (subset_sum(n, array, sum))
    {
        cout << "YES" << endl;
    }
    else
    {
        cout << "NO" << endl;
    }

    return 0;
}