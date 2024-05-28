#include <bits/stdc++.h>
using namespace std;

int *sort_it(int N)
{
    int* array = new int[N];
    for (int i = 0; i < N; i++)
    {
        cin >> array[i];
    }

    sort(array, array + N, greater<int>());

    return array;
}

int main()
{
    int N;
    cin >> N;

    int *sorted_array = sort_it(N);

    for (int i = 0; i < N; i++)
    {
        cout << sorted_array[i] << " ";
    }
    return 0;
}