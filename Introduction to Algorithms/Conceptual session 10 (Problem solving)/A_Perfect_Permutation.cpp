#include <bits/stdc++.h>
using namespace std;

void solve()
{
    int n;
    cin >> n;

    if (n % 2 != 0)
    {
        cout << "-1" << endl;
        return;
    }

    vector<int> P(n + 1);

    for (int i = 1; i <= n; i++)
    {
        P[i] = i;
    }

    for (int i = 1; i < n; i += 2)
    {
        swap(P[i], P[i + 1]);
    }

    for (int i = 1; i <= n; i++)
    {
        cout << P[i] << " ";
    }
    cout << endl;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}