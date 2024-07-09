#include <bits/stdc++.h>
using namespace std;

int main()
{
    stack<int> st;

    st.push(10);
    st.push(20);

    cout << st.top() << endl;
    st.pop();

    cout << st.top() << endl;
    st.pop();

    cout << st.top() << endl;

    if (!st.empty())
    {
        cout << st.top() << endl;
        st.pop();
    }
    

    return 0;
}