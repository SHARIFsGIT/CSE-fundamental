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

    int isPalindrome = 1;
    for (int i = 0; i < N / 2; i++)
    {
        if (A[i] != A[N - i - 1])
        {
            isPalindrome = 0;
            break;
        }
    }

    (isPalindrome) ? cout << "YES" : cout << "NO";

    return 0;
}