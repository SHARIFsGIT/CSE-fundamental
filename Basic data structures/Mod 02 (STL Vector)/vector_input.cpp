#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> v;
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;

        v.push_back(x);
    }

    for (int val : v)
    {
        cout << val << " ";
    }

    // 2nd type:
    int n2;
    cin >> n2;
    vector<int> v2(n2);

    for (int i = 0; i < n2; i++)
    {
        cin >> v2[i];
    }

    for (int val : v2)
    {
        cout << val << " ";
    }

    return 0;
}