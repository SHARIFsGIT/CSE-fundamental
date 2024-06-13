#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> v = {10, 11, 12, 13, 14};
    vector<int> v2 = {100, 110, 120, 130, 140};
    v.insert(v.begin() + 3, 30);
    for (int value : v)
    {
        cout << value << " ";
    }
    cout << endl;

    v.insert(v.begin() + 3, 3, 30);
    for (int value : v)
    {
        cout << value << " ";
    }
    cout << endl;

    v.insert(v.begin() + 3, v2.begin(), v2.end());
    for (int value : v)
    {
        cout << value << " ";
    }
    cout << endl;

    v.insert(v.begin(), v2.begin() + 2, v2.end() - 1);
    for (int value : v)
    {
        cout << value << " ";
    }

    return 0;
}