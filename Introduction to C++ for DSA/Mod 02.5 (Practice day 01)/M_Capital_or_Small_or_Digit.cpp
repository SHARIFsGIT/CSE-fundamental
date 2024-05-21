#include <bits/stdc++.h>
using namespace std;

int main()
{
    char X;
    cin >> X;

    if (X >= '0' && X <= '9')
        cout << "IS DIGIT" << endl;

    else if ((X >= 'a' && X <= 'z') || (X >= 'A' && X <= 'Z'))
    {
        cout << "ALPHA" << endl;
        
        (X >= 'a' && X <= 'z') ? cout << "IS SMALL" << endl : cout << "IS CAPITAL" << endl;
    }

    return 0;
}