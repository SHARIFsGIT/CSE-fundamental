#include <bits/stdc++.h>
using namespace std;

const int N = 105;
vector<int> v[N];
int dis_from_source[N];
int dis_from_destination[N];
bool visited[N];

void bfs(int source, int track)
{
    queue<int> q;
    q.push(source);

    if (track == 1)
    {
        dis_from_source[source] = 0;
    }
    else
    {
        dis_from_destination[source] = 0;
    }

    visited[source] = true;

    while (!q.empty())
    {
        int parent = q.front();
        q.pop();

        for (auto child : v[parent])
        {
            if (!visited[child])
            {
                q.push(child);
                visited[child] = true;
                if (track == 1)
                {
                    dis_from_source[child] = dis_from_source[parent] + 1;
                }
                else
                {
                    dis_from_destination[child] = dis_from_destination[parent] + 1;
                }
            }
        }
    }
}

int main()
{
    int t;
    cin >> t;

    int cases = 1;

    while (t--)
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

        int source, destination;
        cin >> source >> destination;

        for (int i = 0; i < node; i++)
        {
            visited[i] = false;
            dis_from_source[i] = -1;
        }
        bfs(source, 1);

        for (int i = 0; i < node; i++)
        {
            visited[i] = false;
            dis_from_destination[i] = -1;
        }
        bfs(destination, 2);

        int answer = INT_MIN;
        for (int i = 0; i < node; i++)
        {
            int value = dis_from_source[i] + dis_from_destination[i];
            answer = max(answer, value);
        }

        cout << "Case " << cases++ << ": " << answer << endl;

        for (int i = 0; i < node; i++)
        {
            v[i].clear();
        }
    }

    return 0;
}
