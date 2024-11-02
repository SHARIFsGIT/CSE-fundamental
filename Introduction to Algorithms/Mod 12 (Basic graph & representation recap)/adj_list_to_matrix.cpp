#include <bits/stdc++.h>
using namespace std;

void convert(int node, vector<int> adj[])
{
    int matrix[node][node];

    for (int i = 0; i < node; i++)
    {
        for (int j = 0; j < node; j++)
        {
            matrix[i][j] = 0;
            if (i == j)
            {
                matrix[i][j] = 1;
            }
        }
    }

    for (int i = 0; i < node; i++)
    {
        for (int child : adj[i])
        {
            matrix[i][child] = 1;
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

    vector<int> v[node];

    while (edge--)
    {
        int a, b;
        cin >> a >> b;

        // Undirect list:
        v[a].push_back(b);
        v[b].push_back(a);

        // Directed list:
        // v[a].push_back(b);
    }

    convert(node, v);

    return 0;
}