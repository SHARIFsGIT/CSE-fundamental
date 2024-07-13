#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;

    stack<int> st;
    queue<int> q;

    for (int i = 0; i < N; ++i)
    {
        int value;
        cin >> value;
        st.push(value);
    }

    for (int i = 0; i < M; ++i)
    {
        int value;
        cin >> value;
        q.push(value);
    }

    bool areSame = true;
    if (N != M)
    {
        areSame = false;
    }

    while (!st.empty() && !q.empty())
    {
        if (st.top() != q.front())
        {
            areSame = false;
            break;
        }
        st.pop();
        q.pop();
    }

    cout << (areSame ? "YES" : "NO") << endl;

    return 0;
}
