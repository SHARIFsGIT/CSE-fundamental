#include <bits/stdc++.h>
using namespace std;

const int N = 1005;

long long int distances[N];

vector<pair<int, long long int>> adj[N];

class compare
{
public:
    bool operator()(pair<int, long long int> a, pair<int, long long int> b)
    {
        return a.second > b.second;
    }
};

void dijkstra(int source)
{
    priority_queue<pair<int, long long int>, vector<pair<int, long long int>>, compare> q;

    q.push({source, 0});

    distances[source] = 0;

    while (!q.empty())
    {
        pair<int, long long int> parent = q.top();
        q.pop();

        if (parent.second > distances[parent.first])
        {
            continue;
        }
        for (auto child : adj[parent.first])
        {
            int child_node = child.first;
            long long int child_cost = child.second;

            if (parent.second + child_cost < distances[child_node])
            {
                distances[child_node] = parent.second + child_cost;

                q.push({child_node, distances[child_node]});
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
        int a, b;
        long long int w;

        cin >> a >> b >> w;
        adj[a].push_back({b, w});
    }

    int source;
    cin >> source;

    for (int i = 1; i <= node; i++)
    {
        distances[i] = 1e18 + 5;
    }

    dijkstra(source);

    int q;
    cin >> q;

    while (q--)
    {
        int v;
        long long int w;
        cin >> v >> w;

        cout << (distances[v] <= w ? "YES\n" : "NO\n");
    }

    return 0;
}