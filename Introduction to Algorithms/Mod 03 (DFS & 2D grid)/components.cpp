#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;

vector<int> v[N];

bool visit[N];

void dfs(int source)
{
    cout << source << endl;

    visit[source] = true;

    for (int child : v[source])
    {
        if (visit[child] == false)
        {
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

        v[a].push_back(b);
        v[b].push_back(a);
    }

    memset(visit, false, sizeof(visit));

    int count = 0;

    for (int i = 0; i < node; i++)
    {
        if (!visit[i])
        {
            dfs(i);
            count++;
        }
    }

    cout << "Component - " << count << endl;

    return 0;
}