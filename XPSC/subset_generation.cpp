/*
Subset of {1, 5, 3} is 2^3 = 8

{}, {1}, {5}, {3}, {1, 5}, {1, 3}, {5, 3}, {1, 5, 3}

*/

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

    // 2D array:
    vector<vector<int>> subsets;
    for (int i = 0; i < (1 << n); i++)
    {
        vector<int> subset;
        for (int j = 0; j < n; j++)
        {
            if ((i & (1 << j)) != 0)
            {
                subset.push_back(array[j]);
            }
        }
        subsets.push_back(subset);
    }

    for (int i = 0; i < subsets.size(); i++)
    {
        for (auto value : subsets[i])
        {
            cout << value << " ";
        }
        cout << endl;
    }

    return 0;
}