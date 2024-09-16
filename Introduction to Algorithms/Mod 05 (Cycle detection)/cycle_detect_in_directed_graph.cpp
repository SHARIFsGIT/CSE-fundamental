#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;

bool visit[N];

bool path_visit[N];

vector<int> adj[N];

bool answer;

void dfs(int source)
{
    visit[source] = true;
    path_visit[source] = true;

    cout << source << endl;

    for (int child : adj[source])
    {
        if (path_visit[child] == true)
        {
            answer = true;
        }

        if (!visit[child])
        {
            dfs(child);
        }
    }
    path_visit[source] = false;
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
    }

    memset(visit, false, sizeof(visit));
    memset(path_visit, false, sizeof(path_visit));

    answer = false;

    for (int i = 0; i < node; i++)
    {
        if (!visit[i])
        {
            dfs(i);
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