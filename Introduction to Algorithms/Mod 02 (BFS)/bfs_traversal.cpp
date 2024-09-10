#include <bits/stdc++.h>
using namespace std;

vector<int> v[1005];

bool visited[1005];

void bfs(int source)
{
    queue<int> q;
    q.push(source);

    visited[source] = true;

    while (!q.empty())
    {
        int parent = q.front();
        q.pop();

        cout << parent << endl;

        // for (int i = 0; i < v[parent].size(); i++)
        // {
        //     int child = v[parent][i];
        //     cout << child << endl;
        // }

        for (auto child : v[parent])
        {
            if (visited[child] == false)
            {
                q.push(child);
                visited[child] = true;
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

    bfs(source);

    return 0;
}

/*
Time complexity: O(V+E)
Space complexity: O(V)
*/