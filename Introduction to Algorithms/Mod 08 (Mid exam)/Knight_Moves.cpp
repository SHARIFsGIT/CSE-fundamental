#include <bits/stdc++.h>
using namespace std;

bool visited[105][105];

int distances[105][105];

int n, m;

vector<pair<int, int>> d = {{2, 1}, {2, -1}, {1, -2}, {1, 2}, {-2, 1}, {-2, -1}, {-1, -2}, {-1, 2}};

bool valid(int i, int j)
{
    return !(i < 0 || i >= n || j < 0 || j >= m);
}

void bfs(int source_i, int source_j)
{
    queue<pair<int, int>> q;
    q.push({source_i, source_j});

    visited[source_i][source_j] = true;

    distances[source_i][source_j] = 0;

    while (!q.empty())
    {
        pair<int, int> parent = q.front();

        int a = parent.first;
        int b = parent.second;

        q.pop();

        for (int i = 0; i < 8; i++)
        {
            int child_i = a + d[i].first;
            int child_j = b + d[i].second;

            if (valid(child_i, child_j) && !visited[child_i][child_j])
            {
                q.push({child_i, child_j});

                visited[child_i][child_j] = true;

                distances[child_i][child_j] = distances[a][b] + 1;
            }
        }
    }
}

int main()
{
    int t;
    cin >> t;

    while (t--)
    {

        cin >> n >> m;

        int ki, kj, qi, qj;
        cin >> ki >> kj >> qi >> qj;

        memset(visited, false, sizeof(visited));
        memset(distances, -1, sizeof(distances));

        bfs(ki, kj);

        cout << distances[qi][qj] << endl;
    }

    return 0;
}