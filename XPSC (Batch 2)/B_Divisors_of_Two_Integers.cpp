#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    sort(a.begin(), a.end());

    int maxi = a[n - 1];

    vector<int> divisors(maxi + 1, 0);

    for (int i = 1; i * i <= maxi; i++)
    {
        if (maxi % i == 0)
        {
            divisors[i]++;
            if (i != maxi / i)
            {
                divisors[maxi / i]++;
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        if (divisors[a[i]] > 0)
        {
            divisors[a[i]]--;
            a[i] = 0;
        }
    }

    int x = maxi, y = 0;
    for (int i = 0; i < n; i++)
    {
        y = max(y, a[i]);
    }
    cout << x << " " << y << endl;

    return 0;
}
