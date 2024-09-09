#include <bits/stdc++.h>
using namespace std;

int main()
{
    int node, edge;
    cin >> node >> edge;

    int matrix[node][node];
    memset(matrix, 0, sizeof(matrix));

    for (int i = 0; i < edge; i++)
    {
        int a, b;
        cin >> a >> b;

        matrix[a][b] = 1;
        matrix[b][a] = 1;
    }

    for (int i = 0; i < node; i++)
    {
        for (int j = 0; j < node; j++)
        {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }

    if (matrix[3][4] == 1)
    {
        cout << "Conncctct" << endl;
    }
    else
    {
        cout << "Not concctct" << endl;
    }

    return 0;
}