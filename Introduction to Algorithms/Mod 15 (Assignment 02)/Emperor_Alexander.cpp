#include <bits/stdc++.h>
using namespace std;

const int MAX_NODES = 1e5 + 10;
int parent[MAX_NODES];
int groupSize[MAX_NODES];

class Edge
{
public:
    int u, v, weight;
    Edge(int u, int v, int weight)
    {
        this->u = u;
        this->v = v;
        this->weight = weight;
    }
};

bool compareEdges(Edge a, Edge b)
{
    return a.weight < b.weight;
}

void initializeDSU(int n)
{
    for (int i = 1; i <= n; i++)
    {
        parent[i] = i;
        groupSize[i] = 1;
    }
}

int findLeader(int node)
{
    if (parent[node] == node)
        return node;
    return parent[node] = findLeader(parent[node]);
}

void unionBySize(int x, int y)
{
    int leaderX = findLeader(x);
    int leaderY = findLeader(y);

    if (leaderX != leaderY)
    {
        if (groupSize[leaderX] > groupSize[leaderY])
        {
            parent[leaderY] = leaderX;
        }
        else if (groupSize[leaderX] < groupSize[leaderY])
        {
            parent[leaderX] = leaderY;
        }
        else
        {
            parent[leaderX] = leaderY;
            groupSize[leaderY]++;
        }
    }
}

void findMST()
{
    int numNodes, numEdges;
    cin >> numNodes >> numEdges;

    initializeDSU(numNodes);

    vector<Edge> edgesList;

    for (int i = 0; i < numEdges; i++)
    {
        int u, v, weight;
        cin >> u >> v >> weight;
        edgesList.push_back(Edge(u, v, weight));
    }

    initializeDSU(numNodes);

    sort(edgesList.begin(), edgesList.end(), compareEdges);

    long long totalCost = 0;
    int edgesUsed = 0;

    for (Edge &edge : edgesList)
    {
        int leaderU = edge.u;
        int leaderV = edge.v;
        int leaderW = edge.weight;

        if (findLeader(leaderU) != findLeader(leaderV))
        {
            unionBySize(leaderU, leaderV);
            totalCost += leaderW;
            edgesUsed++;
        }
    }

    if (edgesUsed == numNodes - 1)
    {
        int redundantRoads = numEdges - edgesUsed;
        cout << redundantRoads << " " << totalCost << endl;
    }
    else
    {
        cout << "Not Possible" << endl;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int testCases = 1;

    while (testCases--)
    {
        findMST();
    }

    return 0;
}