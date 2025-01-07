#include <bits/stdc++.h>
using namespace std;

const int N = 1e3 + 10;
bool visited[N][N];

int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

char graph[N][N];

int row, col;

map<pair<int, int>, pair<int, int>> par;

bool valid(int ci, int cj)
{
    if (ci >= 0 && ci < row && cj >= 0 && cj < col && !visited[ci][cj] && (graph[ci][cj] == '.' || graph[ci][cj] == 'B'))
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
    visited[source_i][source_j] = true;

    queue<pair<int, int>> q;
    q.push({source_i, source_j});

    while (!q.empty())
    {
        pair<int, int> node = q.front();
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int ci = node.first + dx[i];
            int cj = node.second + dy[i];

            if (valid(ci, cj))
            {
                visited[ci][cj] = true;
                q.push({ci, cj});
                par[{ci, cj}] = {node.first, node.second};

                if (graph[ci][cj] == 'B')
                {
                    return;
                }
            }
        }
    }
}

int main()
{
    cin >> row >> col;

    memset(visited, false, sizeof(visited));

    pair<int, int> start, end;

    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            cin >> graph[i][j];

            if (graph[i][j] == 'A')
            {
                start = {i, j};
            }

            if (graph[i][j] == 'B')
            {
                end = {i, j};
            }
        }
    }

    bfs(start.first, start.second);

    int current_i = end.first;
    int current_j = end.second;

    while (graph[current_i][current_j] != 'A')
    {
        auto parent = par[{current_i, current_j}];

        if (graph[current_i][current_j] != 'B')
        {
            graph[current_i][current_j] = '+';
        }
        
        current_i = parent.first;
        current_j = parent.second;
    }

    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            cout << graph[i][j];
        }
        cout << endl;
    }

    return 0;
}
