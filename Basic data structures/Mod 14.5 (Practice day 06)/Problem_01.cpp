#include <bits/stdc++.h>
using namespace std;

bool compare(stack<int> st1, stack<int> st2, int n, int m)
{
    if (n != m)
    {
        return false;
    }
    else
    {
        while (!st1.empty())
        {
            if (st1.top() != st2.top())
            {
                return false;
            }
            st1.pop();
            st2.pop();
        }
    }
    return true;
}

int main()
{
    int n;
    cin >> n;

    stack<int> st1;
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        st1.push(x);
    }

    int m;
    cin >> m;

    stack<int> st2;
    for (int i = 0; i < m; i++)
    {
        int x;
        cin >> x;
        st2.push(x);
    }

    bool answer = compare(st1, st2, n, m);
    cout << (answer ? "YES" : "NO") << endl;

    return 0;
}