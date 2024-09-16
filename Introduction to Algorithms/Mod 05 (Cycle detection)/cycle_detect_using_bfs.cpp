#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;

bool visit[N];

vector<int> adj[N];

int parent_array[N];

bool answer;

void bfs(int source)
{
    queue<int> q;
    q.push(source);

    visit[source] = true;

    while (!q.empty())
    {
        int parent = q.front();
        cout << parent << endl;
        q.pop();

        for (int child : adj[parent])
        {
            if (visit[child] && parent_array[parent] != child)
            {
                answer = true;
            }

            if (!visit[child])
            {
                visit[child] = true;
                parent_array[child] = parent;
                q.push(child);
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

        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    memset(visit, false, sizeof(visit));
    memset(parent_array, -1, sizeof(parent_array));

    answer = false;

    for (int i = 0; i < node; i++)
    {
        if (!visit[i])
        {
            bfs(i);
        }
    }

    if (answer)
    {
        cout << "Cyclic" << endl;
    }
    else
    {
        cout << "No cycles" << endl;
    }

    return 0;
}