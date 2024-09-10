#include <bits/stdc++.h>
using namespace std;

vector<int> v[1005];

bool visited[1005];

void bfs(int source, int destination)
{
    queue<pair<int, int>> q;
    q.push({source, 0});

    visited[source] = true;

    bool found = false;

    while (!q.empty())
    {
        pair<int, int> p = q.front();
        q.pop();

        int parent = p.first;
        int level = p.second;

        if (parent == destination)
        {
            cout << level << endl;
            found = true;
        }

        for (auto child : v[parent])
        {
            if (visited[child] == false)
            {
                q.push({child, level + 1});
                visited[child] = true;
            }
        }
    }
    
    if (!found)
    {
        cout << -1 << endl;
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

    bfs(source, 6);
    bfs(source, 9);

    return 0;
}