#include <bits/stdc++.h>
using namespace std;

int main()
{
    // Replace:
    vector<int> v = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 2};
    replace(v.begin(), v.end() - 1, 2, 200);
    for (int value : v)
    {
        cout << value << " ";
    }

    cout << endl;

    // Find:
    vector<int> v2 = {0, 1, 2, 30, 4, 5, 6, 7, 8, 9, 2};
    // vector<int>::iterator it;
    // it = find(v2.begin(), v2.end(), 30);
    // cout << *it;

    // OR:
    auto it = find(v2.begin(), v2.end(), 30);
    cout << *it;
    cout << endl;
    
    if (it == v2.end())
    {
        cout << "Not found";
    }
    else
    {
        cout << "Found";
    }

    return 0;
}