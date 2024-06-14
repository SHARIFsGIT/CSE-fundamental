#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, q;
    cin >> n >> q;

    int array[n];
    for (int i = 0; i < n; i++)
    {
        cin >> array[i];
    }

    sort(array, array + n);

    while (q--)
    {
        int x;
        cin >> x;

        bool flag = false;
        // for (int i = 0; i < n; i++)
        // {
        //     if (array[i] == x)
        //     {
        //         flag = true;
        //         break;
        //     }
        // }

        // Binary search:
        int l = 0, r = n - 1;
        while (l <= r)
        {
            int mid_index = (l + r) / 2;
            if (array[mid_index] == x)
            {
                flag = true;
                break;
            }
            else if (x > array[mid_index])
            {
                l = mid_index + 1;
            }
            else
            {
                r = mid_index - 1;
            }
        }

        cout << (flag ? "found" : "not found") << endl;
    }

    return 0;
}