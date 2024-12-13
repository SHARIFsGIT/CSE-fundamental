#include <bits/stdc++.h>
using namespace std;

const int N = 25;
char arr[N][N];
bool visited[N][N];
int cnt;
int row, col;

vector<pair<int, int>> d = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

bool valid(int child_i, int child_j)
{
    if (child_i >= 0 && child_i < row && child_j >= 0 && child_j < col)
    {
        return true;
    }
    else
    {
        return false;
    }
}

void dfs(int source_i, int source_j)
{
    visited[source_i][source_j] = true;
    cnt++;
    for (int i = 0; i < 4; i++)
    {
        int child_i = source_i + d[i].first;
        int child_j = source_j + d[i].second;

        if (valid(child_i, child_j) && !visited[child_i][child_j] && arr[child_i][child_j] != '#')
        {
            dfs(child_i, child_j);
        }
    }
}

int main()
{
    int t;
    cin >> t;

    int cases = 1;

    while (t--)
    {
        cin >> col >> row;

        int source_i, source_j;

        for (int i = 0; i < row; i++)
        {
            for (int j = 0; j < col; j++)
            {
                cin >> arr[i][j];

                if (arr[i][j] == '@')
                {
                    source_i = i;
                    source_j = j;
                }
            }
        }
        memset(visited, false, sizeof(visited));

        cnt = 0;

        dfs(source_i, source_j);

        cout << "Case " << cases++ << ": " << cnt << endl;
    }

    return 0;
}