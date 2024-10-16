#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        int n, x;
        cin >> n >> x;

        cout << ((n * x >= 10000 && n * x <= 99999) ? "YES" : "NO") << endl;
    }

    return 0;
}