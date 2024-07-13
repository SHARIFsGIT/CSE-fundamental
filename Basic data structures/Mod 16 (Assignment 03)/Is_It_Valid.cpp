#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string str;
        cin >> str;

        stack<char> st;

        for (char c : str)
        {
            if (!st.empty() && ((c == '0' && st.top() == '1') || (c == '1' && st.top() == '0')))
            {
                st.pop();
            }
            else
            {
                st.push(c);
            }
        }

        cout << (st.empty() ? "YES" : "NO") << endl;
    }

    return 0;
}