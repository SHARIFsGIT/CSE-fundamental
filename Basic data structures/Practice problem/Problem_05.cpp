#include <bits/stdc++.h>
using namespace std;

vector<int> rightMaxVal(vector<int> &v)
{
    vector<int> findMax(v.size());
    int maxVal = 0;
    for (int i = v.size() - 1; i >= 0; i--)
    {
        findMax[i] = maxVal;
        maxVal = max(maxVal, v[i]);
    }
    return findMax;
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

    vector<int> result = rightMaxVal(v);

    for (int i = 0; i < n; i++)
    {
        cout << result[i] << " ";
    }

    return 0;
}