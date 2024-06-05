#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        string str;
        cin >> str;

        int sum1 = 0, sum2 = 0;
        for (int i = 0; i < 3; i++)
        {
            sum1 += str[i] - '0';
        }

        for (int j = 3; j < 6; j++)
        {
            sum2 += str[j] - '0';
        }

        cout << (sum1 == sum2 ? "YES" : "NO") << endl;
    }

    return 0;
}