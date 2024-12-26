#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;
int parentArray[N];

int group_size[N];

void dsu_initialize(int n)
{
    for (int i = 1; i <= n; i++)
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
    return parentArray[node];
}

void dsu_union_by_size(int node1, int node2)
{
    int leader1 = dsu_find(node1);
    int leader2 = dsu_find(node2);

    if (leader1 == leader2)
    {
        return;
    }

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
    int n, m;
    cin >> n >> m;

    dsu_initialize(n);

    while (m--)
    {
        int a, b;
        cin >> a >> b;

        dsu_union_by_size(a, b);
    }

    vector<int> leaders;
    for (int i = 1; i <= n; i++)
    {
        if (parentArray[i] == -1)
        {
            leaders.push_back(i);
        }
    }

    cout << leaders.size() - 1 << endl;

    for (int i = 1; i < leaders.size(); i++)
    {
        cout << leaders[i] << " " << leaders[i - 1] << endl;
    }

    return 0;
}