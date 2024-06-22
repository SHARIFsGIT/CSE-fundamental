#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a, b, c;
    cin >> a >> b >> c;

    int array[3] = {a, b, c};

    sort(array, array + 3);

    for (int i = 0; i < 3; i++)
    {
        cout << array[i] << endl;
    }

    cout << endl;

    cout << a << endl
         << b << endl
         << c << endl;

    return 0;
}