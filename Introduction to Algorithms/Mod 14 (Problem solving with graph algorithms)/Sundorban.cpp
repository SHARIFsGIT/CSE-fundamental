#include <bits/stdc++.h>
using namespace std;

int n;

char input[50][50];
bool visited[50][50];
int distances[50][50];

vector<pair<int, int>> dist;

bool valid(int child_i, int child_j)
{
    return (0 <= child_i && child_i < n && 0 <= child_j && child_j < n);
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
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int child_i = parent.first + dist[i].first;
            int child_j = parent.second + dist[i].second;

            if (valid(child_i, child_j) && !visited[child_i][child_j] && input[child_i][child_j] != 'T')
            {
                q.push({child_i, child_j});

                visited[child_i][child_j] = true;

                distances[child_i][child_j] = distances[parent.first][parent.second] + 1;
            }
        }
    }
}

int main()
{
    dist.push_back({-1, 0});
    dist.push_back({1, 0});
    dist.push_back({0, -1});
    dist.push_back({0, 1});

    while (cin >> n)
    {
        int source_i, source_j;
        int destination_i, destination_j;

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                cin >> input[i][j];

                if (input[i][j] == 'S')
                {
                    source_i = i;
                    source_j = j;
                }

                else if (input[i][j] == 'E')
                {
                    destination_i = i;
                    destination_j = j;
                }
            }
        }
        memset(visited, false, sizeof(visited));
        memset(distances, -1, sizeof(distances));

        bfs(source_i, source_j);

        cout << distances[destination_i][destination_j] << endl;
    }

    return 0;
}