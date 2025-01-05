#include <bits/stdc++.h>
using namespace std;

// complexity: O(2^n)
int knapsack(int n, int weight[], int value[], int W)
{
    if (n < 0 || W == 0)
    {
        // invalid index
        return 0;
    }

    if (weight[n] <= W)
    {
        // two options: 1. take 2. don't
        int option1 = knapsack(n - 1, weight, value, W - weight[n]) + value[n];
        int option2 = knapsack(n - 1, weight, value, W);

        return max(option1, option2);
    }
    else
    {
        // one option: 1. don't
        int option2 = knapsack(n - 1, weight, value, W);

        return option2;
    }
}

int main()
{
    int n;
    cin >> n;

    int weight[n];
    int value[n];

    for (int i = 0; i < n; i++)
    {
        cin >> weight[i];
    }

    for (int i = 0; i < n; i++)
    {
        cin >> value[i];
    }

    int W;
    cin >> W;

    cout << knapsack(n - 1, weight, value, W) << endl;

    return 0;
}