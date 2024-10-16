#include <bits/stdc++.h>
using namespace std;

const int MAX_NODES = 1e5 + 10;
int parent[MAX_NODES];
int groupSize[MAX_NODES];

void initializeDSU(int n)
{
    for (int i = 1; i <= n; i++)
    {
        parent[i] = -1;
        groupSize[i] = 1;
    }
}

int findLeader(int node)
{
    if (parent[node] == -1)
    {
        return node;
    }
    parent[node] = findLeader(parent[node]);
    return parent[node];
}

void unionBySize(int node1, int node2)
{
    int leader1 = findLeader(node1);
    int leader2 = findLeader(node2);

    if (leader1 != leader2)
    {
        if (groupSize[leader1] > groupSize[leader2])
        {
            parent[leader2] = leader1;
            groupSize[leader1] += groupSize[leader2];
        }
        else
        {
            parent[leader1] = leader2;
            groupSize[leader2] += groupSize[leader1];
        }
    }
}

void detectCycles()
{
    int nodes, edges;
    cin >> nodes >> edges;

    initializeDSU(nodes);

    int cycleCount = 0;

    for (int i = 0; i < edges; i++)
    {
        int u, v;
        cin >> u >> v;

        int leaderU = findLeader(u);
        int leaderV = findLeader(v);

        if (leaderU == leaderV)
        {
            cycleCount++;
        }
        else
        {
            unionBySize(u, v);
        }
    }
    cout << cycleCount << endl;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int testCases = 1;

    while (testCases--)
    {
        detectCycles();
    }

    return 0;
}
