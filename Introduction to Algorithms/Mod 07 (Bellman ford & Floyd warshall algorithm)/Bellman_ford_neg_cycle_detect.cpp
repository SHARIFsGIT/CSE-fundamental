#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;
int distances[N];

class Edge
{
public:
    int u, v, cost;
    Edge(int u, int v, int cost)
    {
        this->u = u;
        this->v = v;
        this->cost = cost;
    }
};

int main()
{
    int node, edge;
    cin >> node >> edge;

    vector<Edge> EdgeList;

    while (edge--)
    {
        int u, v, cost;
        cin >> u >> v >> cost;

        EdgeList.push_back(Edge(u, v, cost));
    }

    for (int i = 0; i < node; i++)
    {
        distances[i] = INT_MAX;
    }

    distances[0] = 0;

    for (int i = 1; i <= node - 1; i++)
    {
        for (Edge edgeElement : EdgeList)
        {
            int u, v, cost;

            u = edgeElement.u;
            v = edgeElement.v;
            cost = edgeElement.cost;

            if (distances[u] < INT_MAX && distances[u] + cost < distances[v])
            {
                distances[v] = distances[u] + cost;
            }
        }
    }

    bool cycle = false;

    for (Edge edgeElement : EdgeList)
    {
        int u, v, cost;

        u = edgeElement.u;
        v = edgeElement.v;
        cost = edgeElement.cost;

        if (distances[u] < INT_MAX && distances[u] + cost < distances[v])
        {
            cycle = true;
            break;
        }
    }

    if (cycle)
    {
        cout << "Cycle detected" << endl;
    }
    else
    {
        for (int i = 0; i < node; i++)
        {
            cout << i << " --> " << distances[i] << endl;
        }
    }

    return 0;
}