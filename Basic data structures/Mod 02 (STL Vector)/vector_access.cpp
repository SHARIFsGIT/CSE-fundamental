#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> v = {0, 1, 2, 3, 4, 5, 6, 7};
    cout << v[v.size() - 1] << endl;
    cout << v.back() << endl;
    cout << v[0] << endl;
    cout << v.front() << endl;

    // Iterator:
    // vector<int>::iterator it;

    for (auto it = v.begin(); it < v.end(); it++)
    {
        cout << *it << " ";
    }

    return 0;
}