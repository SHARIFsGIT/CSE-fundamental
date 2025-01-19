#include <bits/stdc++.h>
using namespace std;

void solve()
{
    int n, k;
    cin >> n >> k;

    int answer = 0;

    if (n % 2 == 0)
    {
        answer = k / 2;
    }
    else
    {
        answer = ceil(1.0 * k / 2);
    }

    cout << (answer % 2 == 0 ? "YES" : "NO") << endl;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--)
    {
        solve();
    }

    return 0;
}