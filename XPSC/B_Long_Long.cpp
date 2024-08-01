#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        long long int n;
        cin >> n;

        long long int total = 0, block = 0;
        bool found = true;

        for (int i = 0; i < n; i++)
        {
            long long int a;
            cin >> a;
            if (a < 0 && found)
            {
                block++;
                found = false;
            }
            if (a > 0)
            {
                found = true;
            }
            total += abs(a);
        }
        cout << total << " " << block << endl;
    }

    return 0;
}