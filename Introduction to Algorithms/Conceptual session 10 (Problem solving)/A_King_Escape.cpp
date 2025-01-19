#include <bits/stdc++.h>
using namespace std;

const int maxN = 1009;
int visited[maxN][maxN];

int n;

int dx[8] = {1, 0, -1, 0, -1, 1, -1, 1};
int dy[8] = {0, 1, 0, -1, -1, 1, 1, -1};

bool isValid(int x, int y)
{
    return (x >= 1 && x <= n && y >= 1 && y <= n);
}

void bfs(int kx, int ky)
{
    queue<pair<int, int>> Q;
    Q.push({kx, ky});

    visited[kx][ky] = true;

    while (!Q.empty())
    {
        int x = Q.front().first;
        int y = Q.front().second;

        Q.pop();

        for (int i = 0; i < 8; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (isValid(nx, ny) && !visited[nx][ny])
            {
                visited[nx][ny] = true;
                Q.push({nx, ny});
            }
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;

    int qx, qy;
    cin >> qx >> qy;

    int kx, ky;
    cin >> kx >> ky;

    int tx, ty;
    cin >> tx >> ty;

    for (int i = 0; i < 8; i++)
    {
        int DX, DY;

        DX = dx[i] + qx;
        DY = dy[i] + qy;

        while (isValid(DX, DY))
        {
            visited[DX][DY] = true;
            DX += dx[i];
            DY += dy[i];
        }
    }

    bfs(kx, ky);

    if (visited[tx][ty])
    {
        cout << "YES" << endl;
    }
    else
    {
        cout << "NO" << endl;
    }

    return 0;
}