#include <bits/stdc++.h>
using namespace std;

int n, m;

bool visit[20][20];

char arr[20][20];

int distances[20][20];

vector<pair<int, int>> v = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

bool valid(int i, int j)
{
    if (i < 0 || i >= n || j < 0 || j >= m)
    {
        return false;
    }
    else
    {
        return true;
    }
}

void bfs(int source_i, int source_j)
{
    queue<pair<int, int>> q;
    q.push({source_i, source_j});

    visit[source_i][source_j] = true;

    distances[source_i][source_j] = 0;

    while (!q.empty())
    {
        pair<int, int> parent = q.front();
        q.pop();

        // cout << parent.first << " " << parent.second << endl;

        for (int i = 0; i < 4; i++)
        {
            int child_i = parent.first + v[i].first;
            int child_j = parent.second + v[i].second;

            if (valid(child_i, child_j) == true && visit[child_i][child_j] == false)
            {
                q.push({child_i, child_j});

                visit[child_i][child_j] = true;

                distances[child_i][child_j] = distances[parent.first][parent.second] + 1;
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
            cin >> arr[i][j];
        }
    }

    int source_i, source_j;
    cin >> source_i >> source_j;

    memset(visit, false, sizeof(visit));

    memset(distances, -1, sizeof(distances));

    bfs(source_i, source_j);

    cout << distances[0][3] << endl;

    return 0;
}

/*
Time Complexity: O(n*m)
*/