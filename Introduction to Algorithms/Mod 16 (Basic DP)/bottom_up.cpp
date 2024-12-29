#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int array[n];

    array[0] = 0;
    array[1] = 1;

    // O(n) time | O(n) space
    for (int i = 2; i <= n; i++)
    {
        array[i] = array[i - 1] + array[i - 2];
    }

    cout << array[n] << endl;

    return 0;
}