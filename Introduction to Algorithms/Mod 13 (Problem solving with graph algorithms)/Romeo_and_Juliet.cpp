#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;

vector<int> graph[N];
bool visited[N];
int distances[N];

void bfs(int source)
{
    queue<int> q;
    q.push(source);

    visited[source] = true;
    distances[source] = 0;

    while (!q.empty())
    {
        int parent = q.front();
        q.pop();

        for (int child : graph[parent])
        {
            if (!visited[child])
            {
                visited[child] = true;
                q.push(child);
                distances[child] = distances[parent] + 1;
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
        cin >> a >> b;

        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    memset(visited, false, sizeof(visited));
    memset(distances, -1, sizeof(distances));

    int source, destination, k;
    cin >> source >> destination >> k;

    bfs(source);
    
    if (distances[destination] != -1 && distances[destination] <= k * 2)
    {
        cout << "YES" << endl;
    }
    else
    {
        cout << "NO" << endl;
    }

    return 0;
}