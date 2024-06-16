#include <bits/stdc++.h>
using namespace std;

int main()
{
    // 01 : O(log(n))
    int k = 1;
    while (k <= n)
    {
        cout << k << endl;
        k = k * 2;
    }

    // 02 : O(n*n)
    for (int i = 0; i < n; i++)
        for (int j = i; j > 0; j--)
            cout << i << j;

    // 03 : O(n*n*n)
    for (int i = 0; i < n; i++)
        for (int j = i; j > 0; j--)
            for (int k = j; k > 0; k--)
                cout << i << j << k;

    // 04 : O(n*log(n))
    for (int i = n / 2; i <= n; i++)
    {
        for (int j = 1; j <= n; j = j * 2)
        {
            cout << i << j << endl;
        }
    }

    // 05 : O(n*log(n))
    for (int i = n / 2; i <= n; i++)
    {
        for (int j = 1; j <= n; j = j + i)
        {
            cout << i << j << endl;
        }
    }

    return 0;
}