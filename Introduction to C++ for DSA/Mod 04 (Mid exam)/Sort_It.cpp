#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N;
    cin >> N;

    long long int A[N];
    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
    }

    // ascending order
    sort(A, A + N);
    for (int i = 0; i < N; i++)
    {
        cout << A[i] << " ";
    }

    cout << endl;

    // descending order
    sort(A, A + N, greater<int>());
    for (int i = 0; i < N; i++)
    {
        cout << A[i] << " ";
    }

    return 0;
}