#include <bits/stdc++.h>
using namespace std;

const int maxN = 100000 + 5;

int dp[maxN];

bool canReach(int n, int current)
{
    if (current == n)
    {
        return true;
    }

    if (current > n)
    {
        return false;
    }

    if (dp[current] != -1)
    {
        return dp[current];
    }

    bool option1 = false, option2 = false, option3 = false;

    if (current + 3 <= n)
    {
        option1 = canReach(n, current + 3);
    }

    if (current * 2 <= n)
    {
        option2 = canReach(n, current * 2);
    }

    if (current * 2 + 3 <= n)
    {
        option3 = canReach(n, current * 2 + 3);
    }

    return dp[current] = (option1 || option2 || option3);
}

void solve()
{
    int n;
    cin >> n;

    memset(dp, -1, sizeof(dp));

    if (canReach(n, 1))
    {
        cout << "YES" << endl;
    }
    else
    {
        cout << "NO" << endl;
    }
}

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        solve();
    }

    return 0;
}
