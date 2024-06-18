#include <bits/stdc++.h>
using namespace std;

int main()
{
    int test;
    cin >> test;

    for (int i = 0; i < test; i++)
    {
        int players;
        cin >> players;

        int runs[players];
        for (int i = 0; i < players; i++)
        {
            cin >> runs[i];
        }

        sort(runs, runs + players);

        cout << runs[players - 1] << endl;
    }

    return 0;
}