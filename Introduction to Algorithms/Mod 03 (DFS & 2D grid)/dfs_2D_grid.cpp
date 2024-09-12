#include <bits/stdc++.h>
using namespace std;

int n, m;

char arr[20][20];

bool visit[20][20];

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

void dfs(int source_i, int source_j)
{
    cout << source_i << " " << source_j << endl;

    visit[source_i][source_j] = true;

    for (int i = 0; i < 4; i++)
    {
        int child_i = source_i + v[i].first;
        int child_j = source_j + v[i].second;

        if (valid(child_i, child_j) == true && visit[child_i][child_j] == false)
        {
            dfs(child_i, child_j);
        }

        // cout << child_i << " " << child_j << endl;
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

    dfs(source_i, source_j);

    return 0;
}

/*
Time Complexity: O(n*m)
*/