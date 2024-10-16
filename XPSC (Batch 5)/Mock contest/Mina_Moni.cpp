#include <bits/stdc++.h>
using namespace std;

void divideCoins()
{
    int n;
    cin >> n;
    vector<int> coins(n);

    for (int i = 0; i < n; i++)
    {
        cin >> coins[i];
    }

    int totalSum = accumulate(coins.begin(), coins.end(), 0);
    int minDiff = 1e9;

    for (int mask = 0; mask < (1 << n); mask++)
    {
        int subsetSum = 0;
        int count = 0;

        for (int j = 0; j < n; j++)
        {
            if (mask & (1 << j))
            {
                subsetSum += coins[j];
                count++;
            }
        }

        if (count == n / 2)
        {
            int remainingSum = totalSum - subsetSum;
            minDiff = min(minDiff, abs(subsetSum - remainingSum));
        }
    }

    cout << minDiff << endl;
}

int main()
{
    int testCases;
    cin >> testCases;
    while (testCases--)
    {
        divideCoins();
    }
    return 0;
}
