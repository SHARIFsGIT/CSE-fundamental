#include <bits/stdc++.h>
using namespace std;

int *get_array(int N)
{
    int *a = new int[N];
    for (int i = 0; i < N; i++)
    {
        cin >> a[i];
    }
    return a;
}

int main()
{
    int N;
    cin >> N;

    int *a = get_array(N);
    for (int i = 0; i < N; i++)
    {
        cout << a[i] << " ";
    }
    return 0;
}