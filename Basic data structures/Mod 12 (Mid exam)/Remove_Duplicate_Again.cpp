#include <bits/stdc++.h>
using namespace std;

int main()
{
    int value;
    list<int> data_list;
    while (cin >> value && value != -1)
    {
        data_list.push_back(value);
    }

    data_list.sort();
    data_list.unique();

    for (auto it : data_list)
    {
        cout << it << " ";
    }

    return 0;
}