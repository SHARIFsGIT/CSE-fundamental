#include <bits/stdc++.h>
using namespace std;

const int N = 1e3 + 7;

int graph[N][N];

int main()
{
    int node, edge;
    cin >> node >> edge;

    memset(graph, 0, sizeof(graph));

    while (edge--)
    {
        int x, y;
        cin >> x >> y;

        graph[x][y] = 1;
    }

    int q;
    cin >> q;

    while (q--)
    {
        int a, b;
        cin >> a >> b;

        cout << ((a == b || graph[a][b]) ? "YES" : "NO") << endl;
    }

    return 0;
}