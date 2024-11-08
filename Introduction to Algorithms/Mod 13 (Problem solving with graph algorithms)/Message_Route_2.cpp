#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;

vector<int> graph[N];
bool visited[N];
int parent_node[N];

void bfs(int source)
{
    queue<int> q;
    q.push(source);

    visited[source] = true;

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
                parent_node[child] = parent;
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
    memset(parent_node, -1, sizeof(parent_node));

    bfs(1);

    int x = node;
    vector<int> path;

    while (x != -1)
    {
        path.push_back(x);
        x = parent_node[x];
    }

    reverse(path.begin(), path.end());

    if (path.size() == 1)
    {
        cout << "IMPOSSIBLE" << endl;
    }
    else
    {
        cout << path.size() << endl;
        
        for (int i : path)
        {
            cout << i << " ";
        }
        cout << endl;
    }

    return 0;
}
