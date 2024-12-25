#include <bits/stdc++.h>
using namespace std;

int parent[105];
int level[105];

void initialize(int sz)
{
    for (int i = 0; i <= sz; i++)
    {
        parent[i] = -1;
        level[i] = 0;
    }
}

int Find(int node)
{
    cout << "Calling node: " << node << endl;

    if (parent[node] == -1)
    {
        return node;
    }
    else
    {
        int leader = Find(parent[node]);
        parent[node] = leader;
        return leader;
    }
}

/* 
// Not optimized
void Union(int p, int q)
{
    int parent_P = Find(p);
    int parent_Q = Find(q);

    parent[parent_Q] = parent_P;
} 
*/

// Optimized
void UnionRank(int p, int q)
{
    int parent_P = Find(p);
    int parent_Q = Find(q);

    if (level[parent_P] > level[parent_Q])
    {
        parent[parent_Q] = parent_P;
    }
    else if (level[parent_P] < level[parent_Q])
    {
        parent[parent_P] = parent_Q;
    }
    else
    {
        parent[parent_Q] = parent_P;
        level[parent_P] += 1;
    }
    
}

int main()
{
    initialize(5);

    UnionRank(4, 5);
    UnionRank(3, 4);
    UnionRank(2, 3);
    UnionRank(1, 2);

    cout << "-------------" << endl;

    cout << Find(5) << endl;
    cout << "+++++++++++++" << endl;

    cout << Find(4) << endl;
    cout << "+++++++++++++" << endl;

    cout << Find(3) << endl;
    cout << "+++++++++++++" << endl;

    cout << Find(2) << endl;
    cout << "+++++++++++++" << endl;

    cout << Find(1) << endl;
    cout << "+++++++++++++" << endl;

    return 0;
}