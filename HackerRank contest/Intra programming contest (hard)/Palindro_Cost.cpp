#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        string str;
        int cost;
        cin >> str >> cost;

        int len = str.length();
        int total_cost = 0;

        for (int i = 0; i < len / 2; i++)
        {
            int difference = abs(str[i] - str[len - 1 - i]);
            total_cost += difference;
        }
        cout << ((total_cost <= cost) ? "YES" : "NO") << endl;
    }

    return 0;
}