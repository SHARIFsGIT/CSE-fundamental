#include <bits/stdc++.h>
using namespace std;

int main()
{
    // Type : 01
    vector<int> v;

    // Type : 02
    vector<int> v(5);
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }
    cout << endl;

    // Type : 03
    vector<int> v(5, 10);
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }
    cout << endl;

    // Type : 04
    vector<int> v2(5, 100);
    vector<int> v(v2);
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }
    cout << endl;

    // Type : 05
    int array[6] = {0, 1, 2, 3, 4, 5};
    vector<int> v(array, array + 6);
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }
    cout << endl;

    // Type : 06
    vector<int> v = {0, 1, 2, 3, 4};
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }
    cout << endl;

    cout << v.size() << endl;

    return 0;
}