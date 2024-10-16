#include <bits/stdc++.h>
using namespace std;

const int N = 100;

vector<pair<int, int>> v[N];

int distances[N];

void dijkstra(int source)
{
    queue<pair<int, int>> q;
    q.push({source, 0});

    distances[source] = 0;

    while (!q.empty())
    {
        pair<int, int> parent = q.front();
        q.pop();

        int node = parent.first;
        int cost = parent.second;

        for (int i = 0; i < v[node].size(); i++)
        {
            pair<int, int> child = v[node][i];

            int childNode = child.first;
            int childCost = child.second;

            if ((cost + childNode) < distances[childNode])
            {
                // Path relaxation:
                distances[childNode] = cost + childCost;
                q.push({childNode, distances[childNode]});
            }
        }
    }
}

int main()
{
    int node, edge;
    cin >> node >> edge;

    while (edge--)
    {
        int a, b, c;
        cin >> a >> b >> c;

        v[a].push_back({b, c});
        v[b].push_back({a, c});
    }

    for (int i = 0; i < node; i++)
    {
        distances[i] = INT_MAX;
    }

    dijkstra(0);

    for (int i = 0; i < node; i++)
    {
        cout << i << "-->" << distances[i] << endl;
    }

    return 0;
}