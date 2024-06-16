#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int array[n];
    for (int i = 0; i < n; i++)
    {
        cin >> array[i];
    }

    long long int prefix_sum[n];
    prefix_sum[0] = array[0];

    for (int i = 1; i < n; i++)
    {
        prefix_sum[i] = prefix_sum[i - 1] + array[i];
    }

    for (int i = n - 1; i >= 0; i--)
    {
        cout << prefix_sum[i] << " ";
    }

    return 0;
}