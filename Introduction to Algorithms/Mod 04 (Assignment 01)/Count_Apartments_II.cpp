#include <bits/stdc++.h>
using namespace std;

char graph[1005][1005];

bool visit[1005][1005];

int n, m;

int cell = 0;

vector<pair<int, int>> d = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

bool check_cell(int i, int j)
{
    return (i >= 0 && i < n && j >= 0 && j < m);
}

void dfs(int si, int sj)
{
    cell++;

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

    vector<int> room;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (graph[i][j] != '#' && !visit[i][j])
            {
                dfs(i, j);
                room.push_back(cell);

                cell = 0;
            }
        }
    }

    if (room.size())
    {
        sort(room.begin(), room.end());

        for (auto x : room)
        {
            cout << x << ' ';
        }
    }
    else
    {
        cout << '0' << endl;
    }
    
    return 0;
}