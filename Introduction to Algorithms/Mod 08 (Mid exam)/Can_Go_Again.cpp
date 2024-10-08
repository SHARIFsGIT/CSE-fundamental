#include <bits/stdc++.h>
using namespace std;

const long long N = 1e18;

long long distances[10005];

class Edge
{
public:
    int u, v, c;
    Edge(int u, int v, int c)
    {
        this->u = u;
        this->v = v;
        this->c = c;
    }
};

int main()
{
    int node, edge;
    cin >> node >> edge;

    vector<Edge> EdgeList;

    while (edge--)
    {
        int u, v, c;
        cin >> u >> v >> c;

        EdgeList.push_back(Edge(u, v, c));
    }

    for (int i = 1; i <= node; i++)
    {
        distances[i] = N;
    }

    int source;
    cin >> source;

    distances[source] = 0;

    for (int i = 0; i < node - 1; i++)
    {
        for (Edge ed : EdgeList)
        {
            int u, v, c;
            u = ed.u;
            v = ed.v;
            c = ed.c;

            if (distances[u] < N && distances[u] + c < distances[v])
            {
                distances[v] = distances[u] + c;
            }
        }
    }

    bool cycle = false;

    for (Edge ed : EdgeList)
    {
        int u, v, c;
        u = ed.u;
        v = ed.v;
        c = ed.c;

        if (distances[u] < N && distances[u] + c < distances[v])
        {
            cycle = true;
            break;
        }
    }

    if (cycle)
    {
        cout << "Negative Cycle Detected" << endl;
    }
    else
    {
        int t;
        cin >> t;

        while (t--)
        {
            int x;
            cin >> x;

            if (distances[x] == N)
            {
                cout << "Not Possible\n";
            }
            else
            {
                cout << distances[x] << endl;
            }
        }
    }
    return 0;
}