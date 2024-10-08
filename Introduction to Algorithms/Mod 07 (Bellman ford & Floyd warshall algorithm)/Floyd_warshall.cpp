#include <bits/stdc++.h>
#define ll long long int
using namespace std;

int main()
{
    ll node, edge;
    cin >> node >> edge;

    ll adj[node][node];

    for (int i = 0; i < node; i++)
    {
        for (int j = 0; j < node; j++)
        {
            adj[i][j] = INT_MAX;

            if (i == j)
            {
                adj[i][j] = 0;
            }
        }
    }

    while (edge--)
    {
        int a, b, cost;
        cin >> a >> b >> cost;

        adj[a][b] = cost;
    }

    cout << endl;
    cout << "-----BEFORE-----" << endl;

    for (int i = 0; i < node; i++)
    {
        for (int j = 0; j < node; j++)
        {
            if (adj[i][j] == INT_MAX)
            {
                cout << "INF ";
            }
            else
            {
                cout << adj[i][j] << " ";
            }
        }
        cout << endl;
    }

    for (int k = 0; k < node; k++)
    {
        for (int i = 0; i < node; i++)
        {
            for (int j = 0; j < node; j++)
            {
                if (adj[i][k] + adj[k][j] < adj[i][j])
                {
                    adj[i][j] = adj[i][k] + adj[k][j];
                }
            }
        }
    }

    cout << endl;
    cout << "-----AFTER-----" << endl;

    for (int i = 0; i < node; i++)
    {
        for (int j = 0; j < node; j++)
        {
            if (adj[i][j] == INT_MAX)
            {
                cout << "INF ";
            }
            else
            {
                cout << adj[i][j] << " ";
            }
        }
        cout << endl;
    }

    cout << endl;

    for (int i = 0; i < node; i++)
    {
        if (adj[i][i] < 0)
        {
            cout << "Cycle Detected";
            break;
        }
    }

    return 0;
}