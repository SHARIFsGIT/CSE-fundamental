#include <bits/stdc++.h>
using namespace std;

/*

Input:
3 3

0 1
0 2
1 2

*/

vector<int> arr[100];

int main()
{
    int node, edge;
    cin >> node >> edge;

    while (edge--)
    {
        int u, v;
        cin >> u >> v;

        arr[u].push_back(v);
        arr[v].push_back(u);
    }

    for (int i = 0; i < node; i++)
    {
        cout << i << "-->";
        for (int j = 0; j < arr[i].size(); j++)
        {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}