#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int matrix[n][n];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> matrix[i][j];
        }
    }

    vector<pair<int, int>> v[n];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (matrix[i][j] > 0)
            {
                v[i].push_back({j, matrix[i][j]});
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        cout << i << " --> ";
        for (pair<int, int> child : v[i])
        {
            cout << "{" << child.first << ", " << child.second << "} ";
        }
        cout << endl;
    }

    return 0;
}