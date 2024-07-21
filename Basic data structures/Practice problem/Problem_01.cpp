#include <bits/stdc++.h>
using namespace std;

vector<int> find_minimum(vector<int> &v)
{
    for (int i = 1; i < v.size() - 1; i++)
    {
        if (v[i] < v[i - 1] && v[i] < v[i + 1])
        {
            cout << v[i] << endl;
        }
    }
}

int main()
{
    int n;
    cin >> n;

    vector<int> v(n);
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
    }

    find_minimum(v);

    return 0;
}