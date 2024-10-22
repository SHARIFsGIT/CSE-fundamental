#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;
int parentArray[N];

int group_size[N];
int level_size[N];

void dsu_initialize(int n)
{
    for (int i = 0; i < n; i++)
    {
        parentArray[i] = -1;

        group_size[i] = 1;
        level_size[i] = 0;
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

// Use dsu_union_by_size or dsu_union_by_level
void dsu_union_by_level(int node1, int node2)
{
    int leader1 = dsu_find(node1);
    int leader2 = dsu_find(node2);

    if (level_size[leader1] > level_size[leader2])
    {
        parentArray[leader2] = leader1;
    }
    else if (level_size[leader1] < level_size[leader2])
    {
        parentArray[leader1] = leader2;
    }
    else
    {
        parentArray[leader1] = leader2;
        level_size[leader2]++;
    }
}

int main()
{
    dsu_initialize(7);

    dsu_union_by_level(1, 2);
    dsu_union_by_level(2, 3);
    dsu_union_by_level(4, 5);
    dsu_union_by_level(5, 6);
    dsu_union_by_level(1, 4);

    cout << dsu_find(1) << endl;
    cout << dsu_find(4) << endl;

    return 0;
}