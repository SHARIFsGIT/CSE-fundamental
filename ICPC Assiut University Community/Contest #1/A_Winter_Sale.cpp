#include <bits/stdc++.h>
using namespace std;

int main()
{
    int x, p;
    cin >> x >> p;

    float result = (p * 100.00) / (100.00 - x);
    cout << fixed << setprecision(2) << result << endl;

    return 0;
}