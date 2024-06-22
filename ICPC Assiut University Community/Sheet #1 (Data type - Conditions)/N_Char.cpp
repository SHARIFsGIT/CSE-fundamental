#include <bits/stdc++.h>
using namespace std;

int main()
{
    char x;
    cin >> x;

    cout << ((x >= 'a') ? char(x - 32) : char(x + 32)) << endl;

    return 0;
}