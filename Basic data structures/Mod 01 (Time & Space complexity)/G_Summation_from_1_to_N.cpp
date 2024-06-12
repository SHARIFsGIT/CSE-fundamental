#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long int n;
    cin >> n;

    long long int sum = 0;

    // Time limit exceeded:
    // for (int i = 1; i <= n; i++)
    // {
    //     sum += i;
    // }

    // New time in O(N):
    sum = (n * (n + 1) / 2);

    cout << sum << endl;

    return 0;
}