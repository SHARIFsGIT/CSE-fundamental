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

    int left_sum[n], running_sum = 0;
    for (int i = 0; i < n; i++)
    {
        left_sum[i] = running_sum;
        running_sum += array[i];
    }

    for (int i = 0; i < n; i++)
    {
        cout << left_sum[i] << " ";
    }

    return 0;
}