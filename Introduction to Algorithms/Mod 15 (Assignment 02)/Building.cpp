#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const int MAX_NODES = 1e5 + 10;

int parent[MAX_NODES];
ll groupSize[MAX_NODES];

class Edge
{
public:
    ll u, v, weight;
    Edge(ll u, ll v, ll weight)
    {
        this->u = u;
        this->v = v;
        this->weight = weight;
    }
};

bool compareEdges(const Edge &a, const Edge &b)
{
    return a.weight < b.weight;
}

void initializeDSU(int n)
{
    for (int i = 1; i <= n; ++i)
    {
        parent[i] = -1;
        groupSize[i] = 1;
    }
}

int findDSU(int node)
{
    if (parent[node] == -1)
    {
        return node;
    }
    return parent[node] = findDSU(parent[node]);
}

void unionBySize(int node1, int node2)
{
    int leaderA = findDSU(node1);
    int leaderB = findDSU(node2);

    if (leaderA != leaderB)
    {
        if (groupSize[leaderA] > groupSize[leaderB])
        {
            parent[leaderB] = leaderA;
            groupSize[leaderA] += groupSize[leaderB];
        }
        else
        {
            parent[leaderA] = leaderB;
            groupSize[leaderB] += groupSize[leaderA];
        }
    }
}

void calculateMST()
{
    int numNodes, numEdges;
    cin >> numNodes >> numEdges;

    initializeDSU(numNodes);
    vector<Edge> edges;

    while (numEdges--)
    {
        int u, v, w;
        cin >> u >> v >> w;
        edges.push_back(Edge(u, v, w));
    }

    sort(edges.begin(), edges.end(), compareEdges);

    ll totalCost = 0;
    for (const Edge &edge : edges)
    {
        int leaderU = findDSU(edge.u);
        int leaderV = findDSU(edge.v);

        if (leaderU != leaderV)
        {
            unionBySize(edge.u, edge.v);
            totalCost += edge.weight;
        }
    }

    int disjointSets = 0;
    for (int i = 1; i <= numNodes; ++i)
    {
        if (parent[i] == -1)
        {
            disjointSets++;
        }
    }

    if (disjointSets > 1)
    {
        cout << -1 << endl;
    }
    else
    {
        cout << totalCost << endl;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int testCases = 1;

    while (testCases--)
    {
        calculateMST();
    }

    return 0;
}