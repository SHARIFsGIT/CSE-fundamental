#include <bits/stdc++.h>
using namespace std;

const int N = 1e3 + 7;

vector<int> graph[N];

int main()
{
    int node, edge;
    cin >> node >> edge;
    while (edge--)
    {
        int x, y;
        cin >> x >> y;

        graph[x].push_back(y);
        graph[y].push_back(x);
    }

    int q;
    cin >> q;

    while (q--)
    {
        int a;
        cin >> a;

        vector<int> result;

        for (auto child : graph[a])
        {
            result.push_back(child);
        }

        sort(result.begin(), result.end(), greater<int>());

        if (result.size())
        {
            for (auto x : result)
            {
                cout << x << " ";
            }
            cout << endl;
        }
        else
        {
            cout << -1 << endl;
        }
    }
    
    return 0;
}