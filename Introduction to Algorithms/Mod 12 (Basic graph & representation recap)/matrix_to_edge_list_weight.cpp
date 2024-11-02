#include <bits/stdc++.h>
using namespace std;

class Edge
{
public:
    int u, v, cost;
    Edge(int u, int v, int cost)
    {
        this->u = u;
        this->v = v;
        this->cost = cost;
    }
};

int main()
{
    int n;
    cin >> n;

    int matrix[n][n];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> matrix[i][j];
        }
    }

    vector<Edge> edge_list;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (matrix[i][j] > 0)
            {
                edge_list.push_back(Edge(i, j, matrix[i][j]));
            }
        }
    }

    for (Edge edge : edge_list)
    {
        cout << edge.u << " " << edge.v << " " << edge.cost << endl;
    }

    return 0;
}