#include <bits/stdc++.h>
using namespace std;

void convert(int node, vector<pair<int, int>> adj[])
{
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

    for (int i = 0; i < node; i++)
    {
        for (pair<int, int> child : adj[i])
        {
            int childNode = child.first;
            int weight = child.second;

            matrix[i][childNode] = weight;
        }
    }

    for (int i = 0; i < node; i++)
    {
        for (int j = 0; j < node; j++)
        {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}

int main()
{
    int node, edge;
    cin >> node >> edge;

    vector<pair<int, int>> v[node];

    while (edge--)
    {
        int a, b, cost;
        cin >> a >> b >> cost;

        // Directed list:
        v[a].push_back({b, cost});
    }

    convert(node, v);

    return 0;
}