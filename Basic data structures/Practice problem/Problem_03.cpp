#include <bits/stdc++.h>
using namespace std;

int main()
{
    int q;
    cin >> q;

    vector<int> v;
    for (int i = 0; i < q; i++)
    {
        int x, value;
        cin >> x;

        if (x == 1)
        {
            cin >> value;
            if (!v.size())
            {
                v.push_back(value);
            }
            else
            {
                v.insert(v.begin() + 1, value);
            }
        }
        else if (x == 2)
        {
            cin >> value;
            if (!v.size())
            {
                v.push_back(value);
            }
            else
            {
                v.insert(v.end() - 1, value);
            }
        }
    }

    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }

    return 0;
}