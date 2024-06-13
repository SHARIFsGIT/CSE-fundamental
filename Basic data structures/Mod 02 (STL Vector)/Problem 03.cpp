#include <bits/stdc++.h>
using namespace std;

int main()
{
    int array[] = {10, 20, 30, 40, 50};
    int array_length = sizeof(array) / sizeof(int);

    vector<int> v(array, array + array_length);
    for (int element : v)
    {
        cout << element << " ";
    }

    return 0;
}