#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<int> v(n);
    stack<int> st;
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
        st.push(v[i]);
    }

    int k;
    cin >> k;

    for (int i = 0; i < n - k; i++)
    {
        st.pop();
    }
    cout << st.top() << endl;

    return 0;
}