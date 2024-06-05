#include <bits/stdc++.h>
using namespace std;

int main()
{
    string str;
    cin >> str;

    string replace = "EGYPT";
    int length = replace.length();
    int count = 0;
    while (str.find(replace) != -1)
    {
        str.replace(str.find(replace), length, " ");
    }
    cout << str << endl;

    return 0;
}