#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;

        vector<int> v(n);
        for (int i = 0; i < n; i++)
        {
            cin >> v[i];
        }

        bool found = false;
        for (int x = 0; x < (1 << 8); x++)
        {
            vector<int> temp = v;
            for (int i = 0; i < n; i++)
            {
                temp[i] = temp[i] ^ x;
            }

            int ans = 0;
            for (int i = 0; i < n; i++)
            {
                ans = ans ^ temp[i];
            }

            if (ans == 0)
            {
                cout << x << endl;
                found = true;
                break;
            }
        }
        if (!found)
        {
            cout << -1 << endl;
        }
    }

    return 0;
}
