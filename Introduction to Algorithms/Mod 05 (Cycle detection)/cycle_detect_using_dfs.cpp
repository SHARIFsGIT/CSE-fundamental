#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;

bool visit[N];

vector<int> adj[N];

int parent_array[N];

bool answer;

void dfs(int source)
{
    visit[source] = true;

    cout << source << endl;

    for (int child : adj[source])
    {
        if (visit[child] && parent_array[source] != child)
        {
            answer = true;
        }

        if (!visit[child])
        {
            parent_array[child] = source;
            
            dfs(child);
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
            dfs(i);
        }
    }

    for (int i = 0; i < node; i++)
    {
        cout << parent_array[i] << " ";
    }

    cout << endl;

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