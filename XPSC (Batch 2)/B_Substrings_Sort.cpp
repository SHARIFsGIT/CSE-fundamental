#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<string> a(n);
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    sort(a.begin(), a.end(), [&](string a, string b)
         { return a.size() < b.size(); });

    bool flag = true;
    for (int i = 0; i < n - 1; i++)
    {
        string s = a[i + 1];
        int position = s.find(a[i]);
        if (position == -1)
        {
            flag = false;
            break;
        }
    }
    
    if (flag)
    {
        cout << "YES" << endl;
        for (auto c : a)
        {
            cout << c << endl;
        }
    }
    else
    {
        cout << "NO" << endl;
    }

    return 0;
}