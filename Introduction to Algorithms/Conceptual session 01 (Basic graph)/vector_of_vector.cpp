#include <bits/stdc++.h>
using namespace std;

int main()
{
    // Type 01:
    vector<vector<int>> name1;

    // Each index have a vector:
    name1.push_back(vector<int>({1, 2, 3}));
    name1.push_back(vector<int>({4, 5, 6}));
    name1[0].push_back(7);

    // row:
    cout << name1.size() << endl;

    // column:
    cout << name1[0].size() << endl;

    for (int i = 0; i < name1.size(); i++)
    {
        for (int j = 0; j < name1[i].size(); j++)
        {
            cout << name1[i][j] << " ";
        }
        cout << endl;
    }

    // Type 02:
    vector<vector<int>> name2;

    return 0;
}