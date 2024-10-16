#include <bits/stdc++.h>
using namespace std;

vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

char grid[1005][1005];
bool visited[1005][1005];
int rows, cols;

bool isValid(int i, int j)
{
    if (i < 0 || i >= rows || j < 0 || j >= cols || grid[i][j] == '-' || visited[i][j])
    {
        return false;
    }
    return true;
}

int dfs(int row, int col)
{
    visited[row][col] = true;
    int regionSize = 1;

    for (auto direction : directions)
    {
        int newRow = row + direction.first;
        int newCol = col + direction.second;

        if (isValid(newRow, newCol))
        {
            regionSize += dfs(newRow, newCol);
        }
    }

    return regionSize;
}

void findSmallestRegion()
{
    cin >> rows >> cols;

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            cin >> grid[i][j];
        }
    }

    memset(visited, false, sizeof(visited));

    int minSize = INT_MAX;
    bool foundRegion = false;

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            if (grid[i][j] == '.' && !visited[i][j])
            {
                int regionSize = dfs(i, j);
                minSize = min(minSize, regionSize);
                foundRegion = true;
            }
        }
    }

    if (!foundRegion)
    {
        cout << -1 << endl;
    }
    else
    {
        cout << minSize << endl;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int testCases = 1;

    while (testCases--)
    {
        findSmallestRegion();
    }

    return 0;
}