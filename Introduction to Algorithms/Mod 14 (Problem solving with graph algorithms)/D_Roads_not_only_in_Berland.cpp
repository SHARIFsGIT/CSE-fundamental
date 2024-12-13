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
    int n;
    cin >> n;

    dsu_initialize(n);

    vector<pair<int, int>> remove;
    vector<pair<int, int>> create;

    for (int i = 1; i <= n - 1; i++)
    {
        int a, b;
        cin >> a >> b;

        int leader1 = dsu_find(a);
        int leader2 = dsu_find(b);

        if (leader1 == leader2)
        {
            remove.push_back({a, b});
        }
        else
        {
            dsu_union_by_size(a, b);
        }
    }
    cout << remove.size() << endl;

    for (int i = 2; i <= n; i++)
    {
        int leader1 = dsu_find(1);
        int leader2 = dsu_find(i);

        if (leader1 != leader2)
        {
            create.push_back({1, i});
            dsu_union_by_size(1, i);
        }
    }
    for (int i = 0; i < remove.size(); i++)
    {
        cout << remove[i].first << " " << remove[i].second << " " << create[i].first << " " << create[i].second << endl;
    }

    return 0;
}