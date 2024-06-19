#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        string S;
        int K;
        cin >> S >> K;

        int len = S.length();
        int total_cost = 0;

        for (int i = 0; i < len / 2; i++)
        {
            int difference = abs(S[i] - S[len - 1 - i]);
            total_cost += difference;
        }
        cout << ((total_cost <= K) ? "YES" : "NO") << endl;
    }

    return 0;
}