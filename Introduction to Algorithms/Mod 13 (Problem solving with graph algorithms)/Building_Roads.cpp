#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;
int parent[N];
int group_size[N];

void dsu_initialize(int n)
{
    for (int i = 1; i <= n; i++)
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

    while (edge--)
    {
        int u, v;
        cin >> u >> v;

        int leader1 = dsu_find(u);
        int leader2 = dsu_find(v);

        if (leader1 != leader2)
        {
            dsu_union_by_size(u, v);
        }
    }

    vector<int> leader;
    for (int i = 1; i <= node; i++)
    {
        leader.push_back(dsu_find(i));
    }

    sort(leader.begin(), leader.end());

    leader.erase(unique(leader.begin(), leader.end()), leader.end());

    cout << leader.size() - 1 << endl;

    for (int i = 0; i < leader.size() - 1; i++)
    {
        cout << leader[i] << " " << leader[i + 1] << endl;
    }

    return 0;
}