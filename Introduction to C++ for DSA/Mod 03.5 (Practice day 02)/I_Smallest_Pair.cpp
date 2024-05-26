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

        long long int A[N];
        for (int i = 0; i < N; i++)
        {
            cin >> A[i];
        }

        int minimun = INT_MAX;
        for (int i = 0; i < N - 1; i++)
        {
            for (int j = i + 1; j < N; j++)
            {
                int result = A[i] + A[j] + j - i;
                minimun = min(minimun, result);
            }
        }
        cout << minimun << endl;
    }

    return 0;
}