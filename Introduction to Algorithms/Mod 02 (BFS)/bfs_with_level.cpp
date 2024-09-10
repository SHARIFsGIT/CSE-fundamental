#include <bits/stdc++.h>
using namespace std;

vector<int> v[1005];

bool visited[1005];

int level[1005];

void bfs(int source)
{
    queue<int> q;
    q.push(source);

    visited[source] = true;
    level[source] = 0;

    while (!q.empty())
    {
        int parent = q.front();
        q.pop();

        for (auto child : v[parent])
        {
            if (visited[child] == false)
            {
                q.push(child);
                visited[child] = true;
                level[child] = level[parent] + 1;
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
    cin >> source;

    memset(visited, false, sizeof(visited));
    memset(level, -1, sizeof(level));

    bfs(source);

    for (int i = 0; i < node; i++)
    {
        cout << i << " " << level[i] << endl;
    }

    return 0;
}