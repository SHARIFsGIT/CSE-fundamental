#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

ll input;
bool recursion(ll n)
{
    if (n > input)
    {
        return false;
    }

    if (n == input)
    {
        return true;
    }

    return recursion(n * 10) || recursion(n * 20);
}

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        cin >> input;

        bool flag = recursion(1);

        if (flag)
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }

    return 0;
}