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

    int old_value, new_value;
    cin >> old_value >> new_value;

    replace(v.begin(), v.end(), old_value, new_value);

    for (int i = 0; i < n; i++)
    {
        cout << v[i] << " ";
    }
    cout << endl;

    int find_value;
    cin >> find_value;

    auto it = find(v.begin(), v.end(), find_value);
    if (it == v.end())
    {
        cout << -1 << endl;
    }
    else
    {
        cout << it - v.begin() << endl;
    }

    return 0;
}