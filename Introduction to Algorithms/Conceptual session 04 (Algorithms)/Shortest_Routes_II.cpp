#include <bits/stdc++.h>
#define ll long long int

const long long int INF = 1e18 + 5;
using namespace std;

int main()
{
    ll node, edge, query;
    cin >> node >> edge >> query;

    ll adj[node + 1][node + 1];

    for (int i = 1; i <= node; i++)
    {
        for (int j = 1; j <= node; j++)
        {
            adj[i][j] = INF;

            if (i == j)
            {
                adj[i][j] = 0;
            }
        }
    }

    while (edge--)
    {
        ll a, b, cost;
        cin >> a >> b >> cost;

        adj[a][b] = min(adj[a][b], cost);
        adj[b][a] = min(adj[b][a], cost);
    }

    for (int k = 1; k <= node; k++)
    {
        for (int i = 1; i <= node; i++)
        {
            for (int j = 1; j <= node; j++)
            {
                if (adj[i][k] + adj[k][j] < adj[i][j])
                {
                    adj[i][j] = adj[i][k] + adj[k][j];
                }
            }
        }
    }

    while (query--)
    {
        int source, destination;
        cin >> source >> destination;

        if (adj[source][destination] == INF)
        {
            cout << -1 << endl;
        }
        else
        {
            cout << adj[source][destination] << endl;
        }
    }

    return 0;
}