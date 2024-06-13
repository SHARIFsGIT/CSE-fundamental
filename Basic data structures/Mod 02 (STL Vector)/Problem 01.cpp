#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<int> v;
    for (int i = 0; i < n; i++)
    {
        v.push_back(i + 1);
    }

    for (int value : v)
    {
        cout << value << " ";
    }

    return 0;
}