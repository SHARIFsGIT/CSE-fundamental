#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> x = {10, 20, 30};
    vector<int> v1 = {1, 2, 3};

    v1 = x; // O(1)
    for (int i = 0; i < v1.size(); i++)
    {
        cout << v1[i] << " ";
    }

    cout << endl;

    vector<int> y = {10, 20, 30, 40};
    vector<int> v2 = {1, 2, 3};

    v2 = y; // O(N)
    for (int i = 0; i < v2.size(); i++)
    {
        cout << v2[i] << " ";
    }
    cout << endl;

    vector<int> z = {10, 20, 30, 40};
    z.pop_back();
    for (int i = 0; i < z.size(); i++)
    {
        cout << z[i] << " ";
    }

    return 0;
}