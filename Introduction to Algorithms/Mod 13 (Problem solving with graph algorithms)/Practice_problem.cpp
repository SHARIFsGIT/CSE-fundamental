/*
Problem Statement:
You live in a city where there are N buildings, and E roads connect those buildings. Each road has a distance, and they are two-way roads. You want to start a business in your city where you will provide ISP service. For that reason, you need to connect all buildings with your central wire cable through the roads. As the price of optical fiber is high, you want to reduce the cost as much as possible. If you know the distance of the roads, can you calculate the minimum cost to connect all buildings with your cable? The cost of optical fiber is equal to the distance of any road.

Sample Input:
6 10
0 1 5
0 2 6
0 3 8
0 4 6
0 5 10
3 5 2
5 1 4
1 2 3
2 4 8
4 3 6

Sample Output:
20
*/

#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;
int parent[N];
int group_size[N];

void dsu_initialize(int n)
{
    for (int i = 0; i < n; i++)
    {
        parent[i] = -1;
        group_size[i] = 1;
    }
}

int dsu_find(int node)
{
    if (parent[node] == -1)
    {
        return node;
    }

    int leader = dsu_find(parent[node]);
    parent[node] = leader;
    return leader;
}

void dsu_union_by_size(int node1, int node2)
{
    int leader1 = dsu_find(node1);
    int leader2 = dsu_find(node2);

    if (group_size[leader1] > group_size[leader2])
    {
        parent[leader2] = leader1;
        group_size[leader1] += group_size[leader2];
    }
    else
    {
        parent[leader1] = leader2;
        group_size[leader2] += group_size[leader1];
    }
}

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

bool compare(Edge a, Edge b)
{
    return a.cost < b.cost;
}

int main()
{
    int node, edge;
    cin >> node >> edge;

    dsu_initialize(node);

    vector<Edge> edgeList;

    while (edge--)
    {
        int u, v, cost;
        cin >> u >> v >> cost;

        edgeList.push_back(Edge(u, v, cost));
    }

    sort(edgeList.begin(), edgeList.end(), compare);

    int totalCost = 0;

    for (Edge edge : edgeList)
    {
        // cout << edge.u << " " << edge.v << " " << edge.cost << endl;

        int leader_U = dsu_find(edge.u);
        int leader_V = dsu_find(edge.v);

        if (leader_U == leader_V)
        {
            continue;
        }
        else
        {
            dsu_union_by_size(edge.u, edge.v);
            totalCost += edge.cost;
        }
    }
    cout << totalCost << endl;

    return 0;
}