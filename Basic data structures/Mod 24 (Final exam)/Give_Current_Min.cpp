#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    priority_queue<int, vector<int>, greater<int>> p;

    while (n--)
    {
        int x;
        cin >> x;
        p.push(x);
    }

    int q;
    cin >> q;
    while (q--)
    {
        int a, b;
        cin >> a;

        if (a == 1)
        {
            if (p.empty())
            {
                cout << "Empty" << endl;
            }
            else
            {
                cout << p.top() << endl;
            }
        }
        else if (a == 2)
        {
            if (!p.empty())
            {
                p.pop();
            }
            if (p.empty())
            {
                cout << "Empty" << endl;
            }
            else
            {
                cout << p.top() << endl;
            }
        }
        else
        {
            cin >> b;
            p.push(b);
            cout << p.top() << endl;
        }
    }
    return 0;
}