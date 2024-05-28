#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        int N;
        cin >> N;

        int S;
        cin >> S;

        int array[N];
        for (int i = 0; i < N; i++)
        {
            cin >> array[i];
        }

        int flag = 0;
        for (int i = 0; i < N; i++)
        {
            for (int j = i + 1; j < N; j++)
            {
                for (int k = j + 1; k < N; k++)
                {
                    if (array[i] + array[j] + array[k] == S)
                    {
                        flag = 1;
                    }
                }
            }
        }

        (flag) ? cout << "YES" << endl : cout << "NO" << endl;
    }

    return 0;
}