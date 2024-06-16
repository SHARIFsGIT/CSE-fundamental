#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<int> array(n);
    for (int i = 0; i < n; i++)
    {
        cin >> array[i];
    }

    sort(array.begin(), array.end());

    int q;
    cin >> q;

    while (q--)
    {
        int find_value;
        cin >> find_value;

        int l = 0;
        int r = n - 1;

        bool flag = false;
        while (l <= r)
        {
            int mid_index = (l + r) / 2;
            if (array[mid_index] == find_value)
            {
                flag = true;
                break;
            }
            else if (find_value > array[mid_index])
            {
                l = mid_index + 1;
            }
            else
            {
                r = mid_index - 1;
            }
        }

        cout << (flag ? "YES" : "NO") << endl;
    }
    return 0;
}