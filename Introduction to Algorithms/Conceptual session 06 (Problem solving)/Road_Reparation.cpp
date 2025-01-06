#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const int N = 1e5 + 10;

class Edge
{
public:
    int u, v, w;
    Edge(int u, int v, int w)
    {
        this->u = u;
        this->v = v;
        this->w = w;
    }
};

bool compare(Edge a, Edge b)
{
    if (a.w < b.w)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int parentArray[N];

int group_size[N];

void dsu_initialize(int n)
{
    for (int i = 0; i < n; i++)
    {
        parentArray[i] = -1;

        group_size[i] = 1;
    }
}

int dsu_find(int node)
{
    if (parentArray[node] == -1)
    {
        return node;
    }

    int leder = dsu_find(parentArray[node]);
    parentArray[node] = leder;
    return leder;
}

void dsu_union_by_size(int node1, int node2)
{
    int leader1 = dsu_find(node1);
    int leader2 = dsu_find(node2);

    if (group_size[leader1] > group_size[leader2])
    {
        parentArray[leader2] = leader1;
        group_size[leader1] += group_size[leader2];
    }
    else
    {
        parentArray[leader1] = leader2;
        group_size[leader2] += group_size[leader1];
    }
}

int main()
{
    int node, edge;
    cin >> node >> edge;

    dsu_initialize(node);

    vector<Edge> EdgeList;

    for (int i = 0; i < edge; i++)
    {
        int u, v, w;
        cin >> u >> v >> w;

        EdgeList.push_back(Edge(u, v, w));
    }

    sort(EdgeList.begin(), EdgeList.end(), compare);

    ll total_cost = 0;

    for (Edge ed : EdgeList)
    {
        int u_leader = dsu_find(ed.u);
        int v_leader = dsu_find(ed.v);

        if (u_leader != v_leader)
        {
            dsu_union_by_size(ed.u, ed.v);
            total_cost += ed.w;
        }
    }

    int main_leader = dsu_find(1);

    bool isConnected = true;

    for (int i = 1; i <= node; i++)
    {
        if (dsu_find(i) != main_leader)
        {
            isConnected = false;
            break;
        }
    }

    if (isConnected)
    {
        cout << total_cost << endl;
    }
    else
    {
        cout << "IMPOSSIBLE" << endl;
    }

    return 0;
}