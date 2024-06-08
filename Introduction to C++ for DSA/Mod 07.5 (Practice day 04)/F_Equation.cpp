#include <bits/stdc++.h>
using namespace std;

int main()
{
    int x, n;
    cin >> x >> n;

    double sum = 0;
    for (int i = 2; i <= n; i += 2)
    {
        sum += pow(x, i);
    }
    cout << (long long int)sum << endl;

    return 0;
}