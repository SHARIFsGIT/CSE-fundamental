#include <bits/stdc++.h>
using namespace std;

int main()
{
    int node, edge;
    cin >> node >> edge;

    vector<int> matrix[node];

    for (int i = 0; i < edge; i++)
    {
        int a, b;
        cin >> a >> b;

        matrix[a].push_back(b);
        matrix[b].push_back(a);
    }

    vector<int> v;
    for (int x : matrix[0])
    {
        cout << x << " ";
    }

    // cout << endl;

    // for (int i = 0; i < matrix[0].size(); i++)
    // {
    //     cout << matrix[0][i] << " ";
    // }

    return 0;
}