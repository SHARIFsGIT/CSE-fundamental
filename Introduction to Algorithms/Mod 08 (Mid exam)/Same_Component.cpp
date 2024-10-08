#include <bits/stdc++.h>
using namespace std;

int n, m;

char matrix[10005][10005];

bool visited[10005][10005];

vector<pair<int, int>> destination_irection = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

bool flag = false;

bool isValid(int i, int j)
{
    return (i >= 0 && i < n && j >= 0 && j < m && matrix[i][j] == '.' && !visited[i][j]);
}

void bfs(int source_i, int source_j, int destination_i, int destination_j)
{
    queue<pair<int, int>> q;
    q.push({source_i, source_j});

    visited[source_i][source_j] = true;

    while (!q.empty())
    {
        auto parent = q.front();
        q.pop();

        if (parent.first == destination_i && parent.second == destination_j)
        {
            flag = true;
            return;
        }

        for (int i = 0; i < 4; i++)
        {
            int child_i = parent.first + destination_irection[i].first;

            int child_j = parent.second + destination_irection[i].second;

            if (isValid(child_i, child_j))
            {
                visited[child_i][child_j] = true;

                q.push({child_i, child_j});
            }
        }
    }
}

int main()
{
    cin >> n >> m;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> matrix[i][j];
        }
    }

    int source_i, source_j, destination_i, destination_j;
    cin >> source_i >> source_j >> destination_i >> destination_j;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            visited[i][j] = false;
        }
    }

    bfs(source_i, source_j, destination_i, destination_j);

    cout << (flag ? "YES" : "NO") << endl;

    return 0;
}