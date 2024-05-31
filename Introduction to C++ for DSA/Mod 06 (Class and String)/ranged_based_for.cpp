#include <bits/stdc++.h>
using namespace std;

int main()
{
    string str;
    cin >> str;

    // Index with elements:
    // for (int i = 0; i < str.size(); i++)
    // {
    //     cout << str[i] << endl;
    // }

    // Only elements:
    for (char character : str)
    {
        cout << character << endl;
    }

    return 0;
}