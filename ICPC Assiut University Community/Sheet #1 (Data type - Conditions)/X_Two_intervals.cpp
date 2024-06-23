#include <bits/stdc++.h>
using namespace std;

int main()
{
    int l1, r1, l2, r2;
    cin >> l1 >> r1 >> l2 >> r2;

    if (r1 < l2 || r2 < l1)
    {
        cout << -1 << endl;
    }
    else
    {
        int start = max(l1, l2);
        int end = min(r1, r2);
        cout << start << " " << end << endl;
    }

    return 0;
}