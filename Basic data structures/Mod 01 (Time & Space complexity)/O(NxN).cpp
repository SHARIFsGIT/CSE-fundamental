#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) // O(N*N)
    {
        for (int j = 0; j < n; j++)
        {
            cout << i << " " << j << endl;
        }
    }

    for (int i = 0; i < n - 1; i++) // O(N*N)
    {
        for (int j = i + 1; j < n; j++)
        {
            cout << i << " " << j << endl;
        }
    }

    return 0;
}

// Rank : 5 -> 10^3