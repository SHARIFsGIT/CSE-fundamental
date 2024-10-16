#include <bits/stdc++.h>
using namespace std;

int findK(string &s, string &t, int n)
{
    int k = (t[0] - s[0] + 26) % 26;
    return k;
}

string applyROT(string &u, int k)
{
    string result = u;
    for (char &c : result)
    {
        c = (c - 'a' + k) % 26 + 'a';
    }
    return result;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        string s, t, u;
        cin >> s >> t >> u;

        int k = findK(s, t, n);
        string result = applyROT(u, k);

        cout << result << endl;
    }

    return 0;
}