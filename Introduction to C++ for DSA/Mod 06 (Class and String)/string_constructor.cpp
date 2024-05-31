#include <bits/stdc++.h>
using namespace std;

int main()
{
    string str1 = "hello world";
    cout << str1 << endl;

    // string is a class so we can use constructor
    string str2("how are you");
    cout << str2 << endl;

    string str3("I am fine", 4);
    cout << str3 << endl;

    string a = "What do you want to do";
    string str4(a, 4);
    cout << str4 << endl;

    string str5(5, 'S');
    cout << str5 << endl;

    return 0;
}