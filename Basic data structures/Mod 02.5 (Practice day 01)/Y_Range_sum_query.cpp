#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long int n, q;
    cin >> n >> q;

    long long int array[n];
    for (int i = 0; i < n; i++)
    {
        cin >> array[i];
    }

    long long int prefix[n];
    prefix[0] = array[0];
    for (int i = 1; i < n; i++)
    {
        prefix[i] = array[i] + prefix[i - 1];
    }

    while (q--)
    {
        int l, r;
        cin >> l >> r;
        l--;
        r--;

        // int sum = 0;
        // for (int i = l; i <= r; i++)
        // {
        //     sum += array[i];
        // }

        // cout << sum << endl;

        long long int sum;
        if (l == 0)
        {
            sum = prefix[r];
        }
        else
        {
            sum = prefix[r] - prefix[l - 1];
        }
        
        cout << sum << endl;
    }

    return 0;
}