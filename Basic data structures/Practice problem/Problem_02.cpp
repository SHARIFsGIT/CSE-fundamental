#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<int> v(n);
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
    }

    // for (int i = 0; i < v.size(); i++)
    // {
    //     int sum = 0;
    //     for (int j = i + 1; j < v.size(); j++)
    //     {
    //         sum += v[j];
    //     }
    //     cout << sum << " ";
    // }

    vector<int> find_sum(n, 0);
    int sum = 0;
    for (int i = n - 2; i >= 0; i--)
    {
        sum += v[i + 1];
        find_sum[i] = sum;
    }
    for (int i = 0; i < n; i++)
    {
        cout << find_sum[i] << " ";
    }

    return 0;
}