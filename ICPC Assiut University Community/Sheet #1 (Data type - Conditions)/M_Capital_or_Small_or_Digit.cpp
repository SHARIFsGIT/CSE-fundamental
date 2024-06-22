#include <bits/stdc++.h>
using namespace std;

int main()
{
    char x;
    cin >> x;

    if (isdigit(x))
    {
        cout << "IS DIGIT" << endl;
    }
    else
    {
        cout << "ALPHA" << endl;
        cout << (islower(x) ? "IS SMALL" : "IS CAPITAL") << endl;
    }

    return 0;
}