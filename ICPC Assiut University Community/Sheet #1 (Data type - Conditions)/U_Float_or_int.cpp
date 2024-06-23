#include <bits/stdc++.h>
using namespace std;

int main()
{
    float n;
    cin >> n;

    if (n == floor(n))
    {
        cout << "int " << n << endl;
    }
    else
    {
        int integer = floor(n);
        float remaining = n - integer;
        cout << "float " << integer << " " << setprecision(3) << remaining << endl;
    }

    return 0;
}