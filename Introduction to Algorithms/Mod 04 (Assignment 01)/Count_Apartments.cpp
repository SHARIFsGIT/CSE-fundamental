#include <bits/stdc++.h>
using namespace std;

char graph[1005][1005];

bool visit[1005][1005];

int n, m;

vector<pair<int, int>> d = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

bool check_cell(int i, int j)
{
    return (i >= 0 && i < n && j >= 0 && j < m);
}

void dfs(int si, int sj)
{
    visit[si][sj] = true;

    for (int i = 0; i < 4; i++)
    {
        int child_i = si + d[i].first;
        int child_j = sj + d[i].second;

        if (check_cell(child_i, child_j) && graph[child_i][child_j] != '#' && visit[child_i][child_j] == false)
        {
            dfs(child_i, child_j);
        }
    }
}

int main()
{
    cin >> n >> m;

    memset(visit, false, sizeof(visit));

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> graph[i][j];
        }
    }

    int x = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (graph[i][j] != '#' && visit[i][j] == false)
            {
                x++;
                dfs(i, j);
            }
        }
    }
    cout << x << endl;
    return 0;
}