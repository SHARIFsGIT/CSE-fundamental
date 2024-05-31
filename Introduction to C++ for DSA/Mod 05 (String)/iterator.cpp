#include <bits/stdc++.h>
using namespace std;

int main()
{
    string str;
    cin >> str;

    cout << *str.begin() << endl;
    cout << *(str.end() - 1) << endl;

    string str2;
    string::iterator it;
    cin >> str2;

    for (it = str2.begin(); it < str2.end(); it++)
    {
        cout << *it << endl;
    }

    // for (string::iterator it = str2.begin(); it < str2.end(); it++)
    // {
    //     cout << *it << endl;
    // }

    for (auto it = str2.begin(); it < str2.end(); it++)
    {
        cout << *it << endl;
    }

    return 0;
}