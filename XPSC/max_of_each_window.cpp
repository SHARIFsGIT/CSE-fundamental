#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int array[n];
    for (int i = 0; i < n; i++)
    {
        cin >> array[i];
    }

    int k;
    cin >> k;

    int maximum = INT_MIN;
    int i = 0, j = 0, shift = 0;

    while (j < n)
    {
        maximum = max(maximum, array[j]);
        if (j < k - 1)
        {
            j++;
        }
        else
        {
            maximum = max(maximum, array[j]);
            shift -= array[i];
            i++;
            j++;
            cout << maximum << " ";
        }
    }

    return 0;
}