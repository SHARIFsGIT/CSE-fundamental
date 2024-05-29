#include <bits/stdc++.h>
using namespace std;

int main()
{
    string str;
    cin >> str;

    cout << str[0] << endl;
    cout << str.at(2) << endl;
    cout << str[str.size() - 1] << endl;
    cout << str.back() << endl;
    cout << str.front() << endl;
    return 0;
}