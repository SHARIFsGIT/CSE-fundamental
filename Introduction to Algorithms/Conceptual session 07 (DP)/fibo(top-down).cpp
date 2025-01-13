#include <bits/stdc++.h>
#define ll long long
using namespace std;

int ll dp[10005];

// Top down approch:
ll fibo(int n)
{
    if (n < 2)
    {
        return n;
    }

    if (dp[n] != -1)
    {
        return dp[n];
    }

    dp[n] = fibo(n - 1) + fibo(n - 2);

    return dp[n];
}

int main()
{
    int n;
    cin >> n;

    memset(dp, -1, sizeof(dp));

    cout << fibo(n) << endl;

    return 0;
}