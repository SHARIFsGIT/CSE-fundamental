#include <bits/stdc++.h>
using namespace std;

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

    vector<pair<int, int>> v[node];
    while (edge--)
    {
        int a, b, cost;
        cin >> a >> b >> cost;

        v[a].push_back({b, cost});
    }

    vector<Edge> edge_list;
    for (int i = 0; i < node; i++)
    {
        for (pair<int, int> child : v[i])
        {
            int childNode = child.first;
            int childCost = child.second;

            edge_list.push_back(Edge(i, childNode, childCost));
        }
    }

    for (Edge edge : edge_list)
    {
        cout << edge.u << " " << edge.v << " " << edge.cost << endl;
    }

    return 0;
}