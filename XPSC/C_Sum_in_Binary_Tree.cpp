#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        long long int n;
        cin >> n;
        long long int sum = 0;

        while (n > 1)
        {
            sum += n;
            n /= 2;
        }
        cout << sum + 1 << endl;
    }

    return 0;
}