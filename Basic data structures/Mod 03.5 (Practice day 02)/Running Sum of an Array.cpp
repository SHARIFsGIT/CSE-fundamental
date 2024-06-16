#include <bits/stdc++.h>
using namespace std;

vector<int> prefix_sum(vector<int> &v)
{
    vector<int> result(v.size());
    
    result[0] = v[0];
    for (int i = 1; i < v.size(); i++)
    {
        result[i] = result[i - 1] + v[i];
    }
    return result;
}

int main()
{
    int n;
    cin >> n;

    vector<int> v(n);
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
    }

    vector<int> result = prefix_sum(v);

    for (int i = 0; i < result.size(); i++)
    {
        cout << result[i] << " ";
    }

    return 0;
}