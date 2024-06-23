#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long int a, b, c, d;
    cin >> a >> b >> c >> d;

    long double lhs = b * log(a);
    long double rhs = d * log(c);

    cout << ((lhs > rhs) ? "YES" : "NO") << endl;

    return 0;
}