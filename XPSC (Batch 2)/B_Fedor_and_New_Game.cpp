#include <bits/stdc++.h>
using namespace std;

/*
int count(int n)
{
    int cnt = 0;
    while (n)
    {
        cnt += (n & 1);
        n >>= 1;
    }
    return cnt;
}
*/

int main()
{
    int n, m, k;
    cin >> n >> m >> k;

    int array[m + 1];
    int ans = 0;
    for (int i = 0; i <= m; i++)
    {
        cin >> array[i];
    }
    /*
        for (int i = 0; i < m; i++)
        {
            if (count(array[i] ^ array[m]) <= k)
            {
                ans++;
            }
        }
    */

    for (int i = 0; i < m; i++)
    {
        if (__builtin_popcount(array[i] ^ array[m]) <= k)
        {
            ans++;
        }
    }
    cout << ans << endl;

    return 0;
}