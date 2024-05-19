#include <bits/stdc++.h>
using namespace std;

int main()
{
    char str[100];
    int a;
    cin >> a;
    // cin >> str;
    // cout << str << endl;
    // cout << strlen(str) << endl; // #include <string.h>

    // fgets(str, 100, stdin); // #include <string.h> with spaces
    // cout << str << endl;
    // cout << strlen(str) << endl;

    // cin.getline(str, 100);
    // cout << str << endl;
    // cout << strlen(str) << endl;

    getchar();
    cin.getline(str, 100);
    cout << a << endl;
    cout << str << endl;
    cout << strlen(str) << endl;

    return 0;
}