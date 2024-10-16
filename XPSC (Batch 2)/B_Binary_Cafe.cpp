#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        long long int n, k;
        cin >> n >> k;

        cout << ((log2(n) >= k) ? (int)pow(2, k) : n + 1) << endl;
    }

    return 0;
}