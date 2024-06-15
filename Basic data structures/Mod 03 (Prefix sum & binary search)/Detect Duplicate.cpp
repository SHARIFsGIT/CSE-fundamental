#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int array[n];
    for (int i = 0; i < n; i++)
    {
        cin >> array[i];
    }

    int x;
    cin >> x;

    int l = 0;
    int r = n - 1;

    bool flag = false;
    while (l <= r)
    {
        int mid_index = (l + r) / 2;
        if (array[mid_index] == x)
        {
            if ((mid_index != 0 && array[mid_index - 1] == x) || (mid_index != n - 1 && array[mid_index + 1] == x))
            {
                flag = true;
                break;
            }
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

    cout << (flag ? "true" : "false") << endl;

    return 0;
}