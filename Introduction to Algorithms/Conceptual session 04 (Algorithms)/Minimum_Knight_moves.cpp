#include <bits/stdc++.h>
using namespace std;

int n, m;

bool visit[10][10];

int distances[10][10];

vector<pair<int, int>> v = {
    {2, 1}, {2, -1}, {-2, 1}, {-2, -1}, 
    {1, 2}, {-1, 2}, {1, -2}, {-1, -2}
};

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

        for (int i = 0; i < 8; i++)
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
    int t;
    cin >> t;

    while (t--)
    {
        n = 8, m = 8;

        string source, destination;
        cin >> source >> destination;

        int source_i, source_j, destination_i, destination_j;

        source_i = source[0] - 'a';
        source_j = source[1] - '1';
        destination_i = destination[0] - 'a';
        destination_j = destination[1] - '1';

        memset(visit, false, sizeof(visit));

        memset(distances, -1, sizeof(distances));

        bfs(source_i, source_j);

        cout << distances[destination_i][destination_j] << endl;
    }

    return 0;
}