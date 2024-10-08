#include <bits/stdc++.h>
using namespace std;

long long int INF = 1e18 + 5;

int main()
{
    int node, edge;
    cin >> node >> edge;

    long long int a[node + 1][node + 1];

    for (int i = 1; i <= node; i++)
    {
        for (int j = 1; j <= node; j++)
        {
            a[i][j] = INF;

            if (i == j)
            {
                a[i][j] = 0;
            }
        }
    }

    while (edge--)
    {
        int u, v;
        long long int c;
        cin >> u >> v >> c;

        a[u][v] = min(a[u][v], c);
    }

    for (int k = 1; k <= node; k++)
    {
        for (int i = 1; i <= node; i++)
        {
            for (int j = 1; j <= node; j++)
            {
                if (a[i][k] == INF || a[k][j] == INF)
                {
                    continue;
                }

                if (a[i][k] + a[k][j] < a[i][j])
                {
                    a[i][j] = a[i][k] + a[k][j];
                }
            }
        }
    }

    int q;
    cin >> q;

    while (q--)
    {
        int u, v;
        cin >> u >> v;

        cout << (a[u][v] != INF ? a[u][v] : -1) << endl;
    }

    return 0;
}