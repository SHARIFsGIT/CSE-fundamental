#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    // cin.ignore();
    vector<string> v;
    // vector<string> v(n);

    for (int i = 0; i < n; i++)
    {
        string str;
        cin >> str;
        // getline(cin, v[i]);
        v.push_back(str);
    }

    // for (int i = 0; i < v.size(); i++)
    // {
    //     cout << v[i] << endl;
    // }

    for (string name : v)
    {
        cout << name << endl;
    }
    
    return 0;
}