#include <bits/stdc++.h>
using namespace std;

int n, m;

char graph[1001][1001];

bool visited[1001][1001];

int dx[4] = {-1, 0, 1, 0}; // Row move
int dy[4] = {0, 1, 0, -1}; // Column move

bool valid(int x, int y)
{
    if (x >= 0 && x < n && y >= 0 && y < m && graph[x][y] == '.')
    {
        return true;
    }
    else
    {
        return false;
    }
}

void bfs(int source_i, int source_j)
{
    queue<pair<int, int>> q;
    q.push({source_i, source_j});

    visited[source_i][source_j] = true;

    while (!q.empty())
    {
        pair<int, int> node = q.front();
        q.pop();

        int node_row = node.first;
        int node_col = node.second;

        for (int i = 0; i < 4; i++)
        {
            int child_i = node_row + dx[i]; // Child row
            int child_j = node_col + dy[i]; // Child column

            if (valid(child_i, child_j) && visited[child_i][child_j] == false)
            {
                visited[child_i][child_j] = true;
                q.push({child_i, child_j});
            }
        }
    }
}

void dfs(int source_i, int source_j)
{
    visited[source_i][source_j] = true;

    for (int i = 0; i < 4; i++)
    {
        int child_i = source_i + dx[i]; // Child row
        int child_j = source_j + dy[i]; // Child column

        if (valid(child_i, child_j) && visited[child_i][child_j] == false)
        {
            visited[child_i][child_j] = true;
            dfs(child_i, child_j);
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
            cin >> graph[i][j];
        }
    }

    // dfs(0, 0);

    // cout << visited[1][1] << endl;

    int count = 0;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (graph[i][j] == '.' && visited[i][j] == false)
            {
                // dfs(i, j);
                bfs(i, j);
                count++;
            }
        }
    }
    cout << count << endl;

    return 0;
}