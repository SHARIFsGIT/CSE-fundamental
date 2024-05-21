#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N;
    cin >> N;

    int array[N];
    for (int i = 0; i < N; i++)
    {
        cin >> array[i];
    }

    int maximum = INT_MIN;
    for (int i = 0; i < N; i++)
    {
        if (array[i] > maximum)
        {
            maximum = array[i];
        }
    }
    cout << maximum << endl;

    return 0;
}