#include <bits/stdc++.h>
using namespace std;

int main()
{
    string str;
    getline(cin, str);

    stringstream ss(str);
    string word;
    do
    {
        if (word == "Jessica")
        {
            cout << "YES" << endl;
            return 0;
        }
    } while (ss >> word);

    cout << "NO" << endl;
    return 0;
}