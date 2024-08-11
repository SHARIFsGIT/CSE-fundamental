#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;

    int diff = a ^ b;
    int count = 0;

    while (diff)
    {
        if (diff & 1)
        {
            count++;
        }
        diff >>= 1;
    }
    cout << count << endl;

    return 0;
}