#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        int n;
        cin >> n;

        int array[n];
        for (int i = 0; i < n; i++)
        {
            cin >> array[i];
        }

        if (n % 2 == 0)
        {
            int even = 0, odd = 0;
            for (int i = 0; i < n; i++)
            {
                (array[i] % 2 == 0) ? even++ : odd++;
            }
            if (odd == even)
            {
                cout << 0 << endl;
            }
            else if ((even + odd) % 2 == 0)
            {
                cout << abs(odd - even) / 2 << endl;
            }
        }
        else
        {
            cout << -1 << endl;
        }
    }

    return 0;
}