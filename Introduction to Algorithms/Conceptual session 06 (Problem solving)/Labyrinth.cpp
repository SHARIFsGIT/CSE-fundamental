#include <bits/stdc++.h>
using namespace std;

int n, m;

bool visited[1005][1005];

char arr[1005][1005];

int distances[1005][1005];

pair<int, int> parentArray[1005][1005];

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

    visited[source_i][source_j] = true;

    distances[source_i][source_j] = 0;

    while (!q.empty())
    {
        pair<int, int> parent = q.front();

        int parent_i = parent.first;
        int parent_j = parent.second;

        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int child_i = parent_i + v[i].first;
            int child_j = parent_j + v[i].second;

            if (valid(child_i, child_j) == true && visited[child_i][child_j] == false && arr[child_i][child_j] != '#')
            {
                q.push({child_i, child_j});

                visited[child_i][child_j] = true;

                distances[child_i][child_j] = distances[parent_i][parent_j] + 1;

                parentArray[child_i][child_j] = {parent_i, parent_j};
            }
        }
    }
}

int main()
{
    int source_i, source_j, destination_i, destination_j;

    cin >> n >> m;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> arr[i][j];

            if (arr[i][j] == 'A')
            {
                source_i = i;
                source_j = j;
            }
            else if (arr[i][j] == 'B')
            {
                destination_i = i;
                destination_j = j;
            }
        }
    }

    memset(visited, false, sizeof(visited));

    memset(distances, -1, sizeof(distances));

    bfs(source_i, source_j);

    if (visited[destination_i][destination_j])
    {
        cout << "YES" << endl;
        cout << distances[destination_i][destination_j] << endl;

        pair<int, int> current = {destination_i, destination_j};

        vector<pair<int, int>> path;

        while (current.first != source_i || current.second != source_j)
        {
            path.push_back(current);

            current = parentArray[current.first][current.second];
        }

        path.push_back({source_i, source_j});

        reverse(path.begin(), path.end());

        string s = "";

        for (int i = 1; i < path.size(); i++)
        {
            if (path[i - 1].first == path[i].first)
            {
                if (path[i - 1].second + 1 == path[i].second)
                {
                    s += "R";
                }
                else
                {
                    s += "L";
                }
            }
            else
            {
                if (path[i - 1].first + 1 == path[i].first)
                {
                    s += "D";
                }
                else
                {
                    s += "U";
                }
            }
        }
        cout << s << endl;
    }
    else
    {
        cout << "NO" << endl;
    }

    return 0;
}