#include <bits/stdc++.h>
using namespace std;

// complexity: O(2^n)
bool subset_sum(int n, int arr[], int sum)
{
    if (n == 0)
    {
        if (sum == 0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    if (arr[n - 1] <= sum)
    {
        bool opt1 = subset_sum(n - 1, arr, sum - arr[n - 1]);
        bool opt2 = subset_sum(n - 1, arr, sum);

        return opt1 || opt2;
    }
    else
    {
        return subset_sum(n - 1, arr, sum);
    }
    
}

int main()
{
    int n;
    cin >> n;

    int array[n];

    for (int i = 0; i < n; i++)
    {
        cin >> array[i];
    }

    int sum;
    cin >> sum;

    if (subset_sum(n, array, sum))
    {
        cout << "YES" << endl;
    }
    else
    {
        cout << "NO" << endl;
    }

    return 0;
}