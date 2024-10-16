#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 1005;

int dp[MAX_N][MAX_N];

bool isSubsetSum(int n, int targetSum, vector<int> &arr)
{
    if (n == 0)
    {
        return targetSum == 0;
    }

    if (dp[n][targetSum] != -1)
    {
        return dp[n][targetSum];
    }

    if (arr[n - 1] <= targetSum)
    {
        bool include = isSubsetSum(n - 1, targetSum - arr[n - 1], arr);

        bool exclude = isSubsetSum(n - 1, targetSum, arr);

        return dp[n][targetSum] = include || exclude;
    }
    else
    {
        return dp[n][targetSum] = isSubsetSum(n - 1, targetSum, arr);
    }
}

void solveTestCase()
{
    int n, s;
    cin >> n >> s;

    vector<int> arr(n);

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    int targetSum = 1000 - s;

    memset(dp, -1, sizeof(dp));

    cout << (isSubsetSum(n, targetSum, arr) ? "YES" : "NO") << endl;
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
