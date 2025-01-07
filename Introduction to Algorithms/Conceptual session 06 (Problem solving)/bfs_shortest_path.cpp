#include <bits/stdc++.h>
using namespace std;

const int N = 1e3 + 10;
bool visited[N];

int parent[N];

vector<int> adj[N];

void bfs(int source)
{
    visited[source] = true;

    queue<int> q;
    q.push(source);
    q.push(5);

    while (!q.empty())
    {
        int node = q.front();
        q.pop();

        for (auto child : adj[node])
        {
            if (!visited[child])
            {
                q.push(child);
                parent[child] = node;
                visited[child] = true;
            }
        }
    }
}

int main()
{
    int nodes, edges;
    cin >> nodes >> edges;

    memset(visited, false, sizeof(visited));
    memset(parent, -1, sizeof(parent));

    for (int i = 0; i < edges; i++)
    {
        int a, b;
        cin >> a >> b;

        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    bfs(1);

    vector<int> path;

    int par = 4;

    while (par != -1)
    {
        path.push_back(par);
        par = parent[par];
    }

    reverse(path.begin(), path.end());

    for (auto p : path)
    {
        cout << p << " " << endl;
    }
    cout << endl;

    return 0;
}