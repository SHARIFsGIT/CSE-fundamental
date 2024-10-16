#include <bits/stdc++.h>
using namespace std;

void solve()
{
    int n;
    cin >> n;

    vector<int> arr(n);

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    int firstMaxIndex = -1, secondMaxIndex = -1;

    int maxVal = INT_MIN;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] > maxVal)
        {
            maxVal = arr[i];
            firstMaxIndex = i;
        }
    }

    arr[firstMaxIndex] = -1;

    maxVal = INT_MIN;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] > maxVal)
        {
            maxVal = arr[i];
            secondMaxIndex = i;
        }
    }

    cout << min(firstMaxIndex, secondMaxIndex) << " "
         << max(firstMaxIndex, secondMaxIndex) << endl;
}

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        solve();
    }

    return 0;
}
