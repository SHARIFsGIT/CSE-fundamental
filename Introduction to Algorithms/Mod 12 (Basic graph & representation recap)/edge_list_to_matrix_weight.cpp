#include <bits/stdc++.h>
using namespace std;

int main()
{
    int node, edge;
    cin >> node >> edge;

    int matrix[node][node];
    for (int i = 0; i < node; i++)
    {
        for (int j = 0; j < node; j++)
        {
            matrix[i][j] = -1;
            if (i == j)
            {
                matrix[i][j] = 0;
            }
        }
    }

    while (edge--)
    {
        int u, v, cost;
        cin >> u >> v >> cost;

        // Undirect list:
        matrix[u][v] = cost;
        matrix[v][u] = cost;

        // Directed list:
        // matrix[u][v] = 1;
    }

    for (int i = 0; i < node; i++)
    {
        for (int j = 0; j < node; j++)
        {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}