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

    vector<int> v[n];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (matrix[i][j] == 1)
            {
                v[i].push_back(j);
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        cout << i << " --> ";
        for (int child : v[i])
        {
            cout << child << " ";
        }
        cout << endl;
    }

    return 0;
}