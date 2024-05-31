#include <bits/stdc++.h>
using namespace std;

int main()
{
    string str1;
    getline(cin, str1);
    // stringstream ss(str1);
    stringstream ss;
    ss << str1;

    string word;
    // ss >> word;
    // cout << word << endl;
    int count = 0;
    while (ss >> word)
    {
        cout << word << endl;
        count++;
    }
    cout << count << endl;

    return 0;
}