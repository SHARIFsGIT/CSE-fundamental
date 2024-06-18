#include <bits/stdc++.h>
using namespace std;

int main()
{
    int x, y, t;
    cin >> x >> y >> t;

    for (int i = 0; i * x <= t; i++)
    {
        int remaining = t - (i * x);

        if (remaining % y == 0)
        {
            cout << "YES" << endl;
            return 0;
        }
    }
    
    cout << "NO" << endl;
    return 0;

    return 0;
}