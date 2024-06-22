#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    cout << n / 365 << " years" << endl;
    n %= 365;

    cout << n / 30 << " months" << endl;
    cout << n % 30 << " days" << endl;

    return 0;
}