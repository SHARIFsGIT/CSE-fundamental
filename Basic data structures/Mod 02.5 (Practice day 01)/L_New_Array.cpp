#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<int> A(n);
    vector<int> B(n);
    vector<int> C;

    for (int i = 0; i < n; i++)
    {
        cin >> A[i];
    }

    for (int i = 0; i < n; i++)
    {
        cin >> B[i];
    }

    for (int i : B)
    {
        C.push_back(i);
    }

    for (int i : A)
    {
        C.push_back(i);
    }

    for (int element : C)
    {
        cout << element << " ";
    }

    return 0;
}