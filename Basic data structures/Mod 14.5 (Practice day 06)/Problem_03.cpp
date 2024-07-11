#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    stack<int> st, copySt;
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        st.push(x);
    }

    while (!st.empty())
    {
        copySt.push(st.top());
        st.pop();
    }

    while (!copySt.empty())
    {
        cout << copySt.top() << " ";
        copySt.pop();
    }

    return 0;
}