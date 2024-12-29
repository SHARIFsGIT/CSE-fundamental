#include <bits/stdc++.h>
#define ll long long
using namespace std;

const ll N = 1e6 + 5;
ll dp[N];

// O(n) time | O(n) space
ll fib(ll n)
{
    if (n == 0 || n == 1)
    { 
        return n;
    }

    if (dp[n] != -1)
    {
        return dp[n];
    }

    ll fib1 = fib(n - 1);
    ll fib2 = fib(n - 2);

    dp[n] = fib1 + fib2;

    return fib1 + fib2;
}

int main()
{
    ll n;
    cin >> n;

    memset(dp, -1, sizeof(dp));

    cout << fib(n) << endl;

    return 0;
}