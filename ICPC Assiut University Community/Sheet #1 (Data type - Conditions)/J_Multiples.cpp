#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;

    cout << ((a % b == 0 || b % a == 0) ? "Multiples" : "No Multiples") << endl;

    return 0;
}