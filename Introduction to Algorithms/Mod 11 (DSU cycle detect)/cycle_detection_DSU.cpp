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

int main()
{
    int node, edge;
    cin >> node >> edge;

    dsu_initialize(node);

    bool cycle = false;
    while (edge--)
    {
        int a, b;
        cin >> a >> b;

        int leader_a = dsu_find(a);
        int leader_b = dsu_find(b);

        if (leader_a == leader_b)
        {
            cycle = true;
        }
        else
        {
            dsu_union_by_size(a, b);
        }
    }

    if (cycle)
    {
        cout << "Cycle found" << endl;
    }
    else
    {
        cout << "Not found" << endl;
    }

    return 0;
}