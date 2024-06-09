#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int array[n];
    for (int i = 0; i < n; i++) // O(N)
    {
        cin >> array[i];
    }

    int sum = 0;
    for (int i = 0; i < n; i++) // O(N)
    {
        if (i % 2 == 0)
        {
            sum += array[i];
        }
    }

    cout << sum << endl;

    return 0;
}


// Rank : 3 -> 10^7