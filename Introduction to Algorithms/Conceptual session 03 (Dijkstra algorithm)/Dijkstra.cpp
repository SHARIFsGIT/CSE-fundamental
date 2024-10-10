#include <bits/stdc++.h>
using namespace std;

vector<pair<int, int>> adj[100005];

const long long int INF = 1e18;
long long int distances[100005];

long long int parentArray[100005];

int node, edge;

void dijkstra(int source)
{
    for (int i = 1; i <= node; i++)
    {
        distances[i] = INF;
    }

    distances[source] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({distances[source], source});

    while (!pq.empty())
    {
        pair<int, int> parent = pq.top();

        int current_distance = parent.first;
        int current_node = parent.second;

        pq.pop();

        for (auto child : adj[current_node])
        {
            int child_distance = child.first;
            int child_node = child.second;

            if (distances[current_node] + child_distance < distances[child_node])
            {
                distances[child_node] = distances[current_node] + child_distance;
                pq.push({distances[child_node], child_node});

                parentArray[child_node] = current_node;
            }
        }
    }
}

int main()
{
    cin >> node >> edge;

    while (edge--)
    {
        int u, v, w;
        cin >> u >> v >> w;

        adj[u].push_back({w, v});
        adj[v].push_back({w, u});
    }

    int source = 1;

    dijkstra(source);

    // for (int i = 1; i <= node; i++)
    // {
    //     cout << distances[i] << " ";
    // }

    int current = node;

    vector<int> path;

    while (true)
    {
        path.push_back(current);

        if (current == source)
        {
            break;
        }

        current = parentArray[current];
    }

    reverse(path.begin(), path.end());

    for (auto child : path)
    {
        cout << child << " ";
    }

    return 0;
}