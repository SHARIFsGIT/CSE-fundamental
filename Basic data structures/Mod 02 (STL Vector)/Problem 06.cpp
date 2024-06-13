#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<string> v(n);
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
    }

    for (int i = 0; i < n; i++)
    {
        v[i][0] = v[i][0] - 32;
    }

    for (int i = 0; i < n; i++)
    {
        cout << v[i] << endl;
    }

    return 0;
}