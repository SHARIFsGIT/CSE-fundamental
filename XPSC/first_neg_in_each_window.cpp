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

    int k;
    cin >> k;

    int i = 0, j = 0;
    queue<int> q;

    while (j < n)
    {
        if (array[j] < 0)
        {
            q.push(array[j]);
        }
        if (j < k - 1)
        {
            j++;
        }
        else
        {
            if (q.empty())
            {
                cout << 0 << " ";
            }
            else
            {
                cout << q.front() << " ";
            }
            if (array[i] < 0)
            {
                q.pop();
            }
            i++;
            j++;
        }
    }
    return 0;
}