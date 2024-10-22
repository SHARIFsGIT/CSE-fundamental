#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;
int parentArray[N];

int group_size[N];

void dsu_initialize(int n)
{
    for (int i = 0; i < n; i++)
    {
        parentArray[i] = -1;

        group_size[i] = 1;
    }

    // parentArray[1] = 2;
    // parentArray[2] = 3;
    // parentArray[5] = 6;
    // parentArray[6] = 7;
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

void dsu_union(int node1, int node2)
{
    int leader1 = dsu_find(node1);
    int leader2 = dsu_find(node2);

    parentArray[leader1] = leader2;
}

// Or use this dsu_union_by_size cause its optimized
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
    // dsu_initialize(8);
    // cout << dsu_find(1) << endl;

    // dsu_union(1, 5);
    // cout << dsu_find(1) << endl;

    dsu_initialize(7);

    dsu_union_by_size(1, 2);
    dsu_union_by_size(2, 3);

    dsu_union_by_size(4, 5);
    dsu_union_by_size(5, 6);

    cout << dsu_find(1) << endl;
    cout << dsu_find(4) << endl;

    dsu_union_by_size(1, 4);
    cout << dsu_find(1) << endl;
    cout << dsu_find(4) << endl;

    return 0;
}