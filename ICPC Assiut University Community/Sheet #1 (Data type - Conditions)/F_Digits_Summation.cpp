#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long int n, m;
    cin >> n >> m;

    long long int result = (n % 10) + (m % 10);
    cout << result << endl;

    return 0;
}