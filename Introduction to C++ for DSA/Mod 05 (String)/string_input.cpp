#include <bits/stdc++.h>
using namespace std;

int main()
{
    string str1;
    // cin.getline(str1, 100); -----> char str1[100];
    getline(cin, str1);
    cout << str1 << endl;
    cout << str1.size() << endl;

    int X;
    cin >> X;
    // cin.ignore();
    getchar();

    string str2;
    getline(cin, str2);
    cout << X << endl;
    cout << str2 << endl;

    return 0;
}