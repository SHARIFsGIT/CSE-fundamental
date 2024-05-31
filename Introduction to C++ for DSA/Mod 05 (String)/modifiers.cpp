#include <bits/stdc++.h>
using namespace std;

int main()
{
    string str1 = "Hello, world";
    string str2 = "How are you?";

    // str1 = str1 + str2;
    // str1 += str2;
    str1.append(str2);
    cout << str1 << " " << str2 << endl;

    // str1[12] = 'A';
    // cout << str1 << endl;

    str1 += 'A';
    cout << str1 << endl;

    str1.push_back('B');
    cout << str1 << endl;

    str1.pop_back();
    cout << str1 << endl;

    str1.assign("Sharif");
    cout << str1 << endl;

    str1.replace(2, 0, "XYZ");
    cout << str1 << endl;

    str1.insert(2, "-");
    cout << str1 << endl;

    str1.erase(4, 1);
    cout << str1 << endl;

    str1.erase(3);
    cout << str1 << endl;

    return 0;
}