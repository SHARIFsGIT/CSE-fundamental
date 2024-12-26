#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;
int parentArray[N];

int group_size[N];

int components, max_size;

void dsu_initialize(int n)
{
    for (int i = 0; i < n; i++)
    {
        parentArray[i] = -1;

        group_size[i] = 1;
    }
    max_size = INT_MIN;
    components = n;
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

    if (leader1 == leader2)
    {
        return;
    }

    if (group_size[leader1] > group_size[leader2])
    {
        parentArray[leader2] = leader1;
        group_size[leader1] += group_size[leader2];
        max_size = max(max_size, group_size[leader1]);
    }
    else
    {
        parentArray[leader1] = leader2;
        group_size[leader2] += group_size[leader1];
        max_size = max(max_size, group_size[leader2]);
    }
    components--;
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
        cout << components << " " << max_size << endl;
    }
    

    return 0;
}