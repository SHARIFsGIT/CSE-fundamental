#include <bits/stdc++.h>
using namespace std;

vector<int> v[1005];

bool visited[1005];

int level[1005];

int parent[1005];

void bfs(int source)
{
    queue<int> q;
    q.push(source);

    visited[source] = true;
    level[source] = 0;

    while (!q.empty())
    {
        int par = q.front();
        q.pop();

        for (auto child : v[par])
        {
            if (visited[child] == false)
            {
                q.push(child);
                visited[child] = true;
                level[child] = level[par] + 1;
                parent[child] = par;
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

        v[a].push_back(b);
        v[b].push_back(a);
    }

    int source;
    int destination;
    cin >> source >> destination;

    memset(visited, false, sizeof(visited));
    memset(level, -1, sizeof(level));
    memset(parent, -1, sizeof(parent));

    bfs(source);

    int x = destination;
    vector<int> path;

    while (x != -1)
    {
        path.push_back(x);
        x = parent[x];
    }

    reverse(path.begin(), path.end());
    for (int value : path)
    {
        cout << value << " ";
    }

    return 0;
}