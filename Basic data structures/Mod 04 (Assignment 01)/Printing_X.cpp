#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int center = n / 2;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << ((i == center && i == j) ? 'X' : 
                    (i == j) ? '\\' : 
                    (i + j == n - 1) ? '/' : ' ');
        }
        cout << endl;
    }

    return 0;
}