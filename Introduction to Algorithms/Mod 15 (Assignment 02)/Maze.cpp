#include <bits/stdc++.h>
using namespace std;

int n, m;

const int N = 1e3 + 10;

bool visited[N][N];
char grid[N][N];

int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

map<pair<int, int>, pair<int, int>> parents;

bool valid(int child_i, int child_j)
{
    if (child_i >= 0 && child_i < n && child_j >= 0 && child_j < m && (grid[child_i][child_j] == '.' || grid[child_i][child_j] == 'D'))
    {
        return true;
    }
    return false;
}

void bfs(int source_i, int source_j)
{
    visited[source_i][source_j] = true;

    queue<pair<int, int>> q;
    q.push({source_i, source_j});

    while (!q.empty())
    {
        pair<int, int> node = q.front();
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int child_i = node.first + dx[i];
            int child_j = node.second + dy[i];

            if (valid(child_i, child_j) && !visited[child_i][child_j])
            {
                visited[child_i][child_j] = true;
                q.push({child_i, child_j});

                parents[{child_i, child_j}] = {node.first, node.second};
            }
        }
    }
}

int main()
{
    cin >> n >> m;

    memset(visited, false, sizeof(visited));

    int source_i = 0, source_j = 0, x = 0, y = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> grid[i][j];
            if (grid[i][j] == 'R')
            {
                source_i = i;
                source_j = j;
            }
            if (grid[i][j] == 'D')
            {
                x = i;
                y = j;
            }
        }
    }

    bfs(source_i, source_j);

    int sti = x, stj = y;

    if (visited[x][y])
    {
        while (grid[sti][stj] != 'R')
        {
            if (grid[sti][stj] != 'D')
            {
                grid[sti][stj] = 'X';
            }
            auto parent = parents[{sti, stj}];
            sti = parent.first;
            stj = parent.second;
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cout << grid[i][j];
        }
        cout << endl;
    }

    return 0;
}