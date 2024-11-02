#include <bits/stdc++.h>
using namespace std;

int main()
{
    int node, edge;
    cin >> node >> edge;

    vector<pair<int, int>> v[node];
    while (edge--)
    {
        int a, b, cost;
        cin >> a >> b >> cost;

        // Undirected:
        // v[a].push_back({b, cost});
        // v[b].push_back({a, cost});

        // Directed:
        v[a].push_back({b, cost});
    }

    for (int i = 0; i < node; i++)
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